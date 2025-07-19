from fastapi import APIRouter, Request # para crear rutas en FastAPI modulares
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB

from app.schemas.log_preRegistro import log_preRegistro # Importar el modelo de datos para validación

# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from prometheus_client import CollectorRegistry, generate_latest

# imporar las consultas 
from app.services.queryMongo import get_logs_preRegsitro
from app.services.requests_preRegistro import getPrematriculas, deletePrematricula

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
    response = getPrematriculas()
    if response is not None:
        return response
    else:
        raise HTTPException(status_code=500, detail="Error al obtener pre-registros")

# Ruta para el rechazo de solicitud de prematricula de un estudiante 
@router.post("/prematricula/rechazar/{id}", response_model=dict)
def rechazar_prematricula(id:str):
    response = deletePrematricula(id)
    if response is not None:
        return response
    else:
        raise HTTPException(status_code=500, detail=f"Error al borrar pre-registro con id: {id} ")
    

# Ruta para la aceptacion de solicitud de prematricula de un estudiante 
@router.post("/prematricula/aceptar/{id}/{id_sede}/{id_curso}", response_model=dict)
def aceptar_prematricula(id:str, id_sede:int, id_curso:int):

    
    response = deletePrematricula(id)
    if response is not None:
        return response
    else:
        raise HTTPException(status_code=500, detail=f"Error al borrar pre-registro con id: {id} ")
    
