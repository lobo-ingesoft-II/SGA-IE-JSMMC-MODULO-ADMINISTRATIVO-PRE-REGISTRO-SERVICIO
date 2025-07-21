
from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB
from app.schemas.log_preRegistro_schema import log_preRegistro # Importar el modelo de datos para validación

# llamar a los request  
from app.services.requests_preRegistro import byId_get_preMatricula
from app.services.requests_auth import by_document_get_acudiente
from app.services.request_sedes import byName_sede_get_sede

from app.schemas.acudiente_schema import AcudienteBase
from app.schemas.usuario_schema import CrearUsuario

def createDic_acudiente(id_prematricula):

    # primero traer la prematricula 
    document = byId_get_preMatricula(id_prematricula)


    if document is not None:
        document_dict = document["documento"]

        parentesco = document_dict["acudiente1Parentesco"]
        cell = document_dict["acudiente1Celular"]
        direccion = document_dict["direccionResidencia"]

        # Crear un diccionario con los datos del acudiente
        acudiente_data = {
            "parentesco": parentesco,
            "celular": cell,
            "direccion": direccion
        }
        

        return acudiente_data  # Retorna el diccionario con los datos del acudiente
    else:
        return None

def createDic_acudiente_with_id_usuario(id_prematricula, id_usuario):

    # primero traer la prematricula 
    document = byId_get_preMatricula(id_prematricula)


    if document is not None:
        document_dict = document["documento"]

        parentesco = document_dict["acudiente1Parentesco"]
        cell = document_dict["acudiente1Celular"]
        direccion = document_dict["direccionResidencia"]

        # Crear un diccionario con los datos del acudiente
        acudiente_data = {
            "id_usuario": id_usuario,
            "parentesco": parentesco,
            "celular": cell,
            "direccion": direccion
        }
        

        return acudiente_data  # Retorna el diccionario con los datos del acudiente
    else:
        return None

    

def createDic_usuario_rol_acudiente(id_prematricula):

    # primero traer la prematricula 
    document = byId_get_preMatricula(id_prematricula)

    if document is not None:
        document_dict = document["documento"]

        nombres = document_dict["acudiente1Nombres"]
        apellidos = document_dict["acudiente1Apellidos"]
        tipo_documento = "CC"
        documento_identidad = document_dict["acudiente1CC"]
        cell = document_dict["acudiente1Celular"]
        # USUARIO numero documento estudiante 
        email = f"{document_dict["numeroDocumento"]}@acudiente.com"
        # Contrasena numero de documento acudiente 
        contrasena = documento_identidad
        rol = "acudiente"

        # Crear un diccionario con los datos del usuario
        usuario_data = {
            "nombres": nombres,
            "apellidos": apellidos,
            "tipo_documento": tipo_documento,
            "documento_identidad": documento_identidad,
            "telefono": cell,
            "email": email,
            "contrasena": contrasena,
            "rol": rol,
            "datos_adicionales":  {}
        }

        return usuario_data  # Retorna el diccionario con los datos del usuario
    else:
        return None

def createDic_estudiante(id_prematricula, idAcudiente, idSede):

    # primero traer la prematricula 
    document = byId_get_preMatricula(id_prematricula)

    if document is not None:
        document_dict = document["documento"]

        names = document_dict["nombres"]
        last_names = document_dict["apellidos"]
        type_document = document_dict["tipoDocumento"]
        number_document = document_dict["numeroDocumento"]
        cell = document_dict["telefono"]
        email = f"{document_dict['numeroDocumento']}@estudiante.com"
        bird_date = document_dict["fechaNacimiento"]
        id_acudiente = idAcudiente
        id_curso = None
        id_sede = idSede
        estado_matricula = "matriculado"

        # Crear un diccionario con los datos del estudiante
        estudiante_data = {
            "nombres": names,
            "apellidos": last_names,
            "tipo_documento": type_document,
            "documento_identidad": number_document,
            "telefono": cell,
            "email": email,
            "fecha_nacimiento": bird_date,
            "id_acudiente": id_acudiente,
            "id_curso": id_curso,
            "id_sede": id_sede,
            "estado_matricula": estado_matricula
        }

        return estudiante_data  # Retorna el diccionario con los datos del estudiante
    else:
        return None

