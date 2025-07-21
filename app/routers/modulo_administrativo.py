from fastapi import APIRouter, Request # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB

from app.schemas.log_preRegistro_schema import log_preRegistro # Importar el modelo de datos para validación

# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from prometheus_client import CollectorRegistry, generate_latest

# imporar las consultas 
from app.services.queryMongo import get_logs_preRegsitro,create_log_preRegistro
from app.services.requests_preRegistro import get_preMatriculas, delete_preMatricula

from app.services.creation_dataDic import createDic_acudiente, createDic_estudiante, createDic_usuario_rol_acudiente
from app.services.requests_auth import create_usuario, by_document_get_acudiente, delete_usuario
from app.services.request_sedes import byName_sede_get_sede
from app.services.requests_preRegistro import byId_get_preMatricula, byStudent_document_get_preMatricula
from app.services.requests_estudiante import create_estudiante


router = APIRouter() 

# Metricas 
REQUEST_COUNT_PRE_REGISTRATION_ROUTERS = Counter(
    "http_requests_total", 
    "TOTAL PETICIONES HTTP router-pre_registration",
    ["method", "endpoint"]
)

REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS = Histogram(
    "http_request_duration_seconds", 
    "DURACION DE LAS PETICIONES router-pre_registration",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]  
)

# 3. Errores por endpoint
ERROR_COUNT_PRE_REGISTRATION_ROUTERS = Counter(
    "http_request_errors_total",
    "TOTAL ERRORES HTTP (status >= 400)",
    ["endpoint", "method", "status_code"]
)

# Ruta para observabilidad 
@router.get("/custom_metrics")
def custom_metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT_PRE_REGISTRATION_ROUTERS)
    registry.register(REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS)
    registry.register(ERROR_COUNT_PRE_REGISTRATION_ROUTERS)
    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)


# Ruta para obtener todos los logs 
@router.get("/log_pre_registros", response_model=dict)
def logs_preRegsitro():
    documents = get_logs_preRegsitro()
    return {"coleccion": documents}


# Ruta para mostrar todos los preRegistro en el momento 
@router.get("/pre_registros", response_model=dict)
def get_pre_registros():
    response = get_preMatriculas()
    if response is not None:
        return response
    else:
        raise HTTPException(status_code=500, detail="Error al obtener pre-registros")

# Ruta para el rechazo de solicitud de prematricula de un estudiante 
@router.post("/prematricula/rechazar/{id}", response_model=dict)
def rechazar_prematricula(id:str):

    try:
    # Crear log de pre-registro
        document = byId_get_preMatricula(id)
        if document is None:
            raise HTTPException(status_code=404, detail="Pre-matricula no encontrada")
        
        document = document["documento"] # Obtener el dic de prematricula
        numeroEstudiante = document["numeroDocumento"]
        create_log_preRegistro(opcion="rechazado", id_preRegistro=id, numeroDocumento_estudiante=numeroEstudiante, dic_preRegistro=document )

        # Borrar la prematricula
        response = delete_preMatricula(id)
        if response is not None:
            return response
        else:
            raise HTTPException(status_code=500, detail=f"Error al borrar pre-registro con id: {id} ")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el log de pre-registro: {str(e)}")


    


# Ruta para la aceptacion de solicitud de prematricula de un estudiante 
@router.post("/prematricula/aceptar/{id_preRegistro}/{id_curso}", response_model=dict)
def aceptar_prematricula(id_preRegistro:str,id_curso:int):

    try:
        # Primero se debe de crear el diccionario del usuario
        dic_usuario = createDic_usuario_rol_acudiente(id_preRegistro)
        dic_acudiente  = createDic_acudiente(id_preRegistro)
 
        
        # Verificar diccionario del usuario
        if dic_usuario is None:
            raise HTTPException(status_code=500, detail="Error al crear el diccionario del usuario - Pre Registro no encontrado")
        if dic_acudiente is None:
            raise HTTPException(status_code=500, detail="Error al crear el diccionario del acudiente - Pre Registro no encontrado")

        # Agregar el diccionario del acudiente al diccionario del usuario
        dic_usuario["datos_adicionales"] = dic_acudiente

        # Crear el usuario en la base de datos
        dic_usuario_acudiente = create_usuario(dic_usuario)
        if dic_usuario_acudiente is None:
            raise HTTPException(status_code=500, detail="Error al crear el usuario y acudiente en la base de datos")
        
        print("USUARIO CREADO")
        id_usuario = dic_usuario_acudiente["id_usuario"]

        # Ese metodo Crea de una vez el acudiente !!

        # Ahora se crea el diccionario del estudiante 
            # buscar Id del acudiente y sede 
        document = byId_get_preMatricula(id_preRegistro)
        if document is None:
            delete_usuario(id_usuario)  # borrar el usuario creado si no se encuentra la prematricula
            raise HTTPException(status_code=404, detail="Prematricula no encontrada buscando id acudiente y sede")
            


        document = document["documento"] # Obtener el dic de prematricula
        numeroEstudiante = document["numeroDocumento"]

        acudiente = by_document_get_acudiente(document["acudiente1CC"])
        if acudiente is None:
            delete_usuario(id_usuario)  # borrar el usuario creado si no se encuentra la prematricula
            raise HTTPException(status_code=404, detail="Acudiente no encontrado")
        
        id_acudiente = acudiente["id_acudiente"] 

        # Trear el id de la sede 
        sede = byName_sede_get_sede(document["sede"])
        if sede is None:
            delete_usuario(id_usuario)  # borrar el usuario creado si no se encuentra la prematricula
            raise HTTPException(status_code=404, detail="Sede no encontrada")
        
        id_sede = sede["id_sede"] 

        # print("id_sede: ", id_sede)

        dic_estudiante = createDic_estudiante(id_preRegistro, id_acudiente, id_sede, id_curso)

        if dic_estudiante is None:
            delete_usuario(id_usuario)  # borrar el usuario creado si no se encuentra la prematricula
            raise HTTPException(status_code=500, detail="Error al crear el diccionario del estudiante")
        
        # Crear el estudiante en la base de datos
        estudiante = create_estudiante(dic_estudiante)
        # id_estudiante = estudiante.get("id_estudiante")

        if estudiante is None:
            delete_usuario(id_usuario)  # borrar el usuario creado si no se encuentra la prematricula
            raise HTTPException(status_code=500, detail="Error al crear el estudiante en la base de datos")
        
        else:
            # Ahora se debe de borrar la prematricula
            response = delete_preMatricula(id_preRegistro)
            if response is None:
                raise HTTPException(status_code=500, detail=f"Error al borrar pre-registro con id: {id} ")
            
            # Crear log de pre-registro
            id_preRegistro__ = id_preRegistro
            create_log_preRegistro(opcion="aceptado", id_preRegistro=id_preRegistro__, numeroDocumento_estudiante=numeroEstudiante, dic_preRegistro=document )
            
            # Por ultimo message de exito
            return {"message": "Prematricula aceptada y estudiante creado exitosamente", "estudiante": estudiante}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")


    
# Ruta para buscar prematriculas por numero de documento del estudiante 
@router.get("/prematricula/buscar/{numero_documento}", response_model=dict)
def buscar_prematricula(numero_documento: str):
    try:
        # Buscar la prematricula por numero de documento
        document = byStudent_document_get_preMatricula(numero_documento)
        
        if document is not None:
            return document  # Retorna el diccionario con los datos de la prematricula
        else:
            raise HTTPException(status_code=404, detail="Prematricula no encontrada")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar prematricula: {str(e)}")