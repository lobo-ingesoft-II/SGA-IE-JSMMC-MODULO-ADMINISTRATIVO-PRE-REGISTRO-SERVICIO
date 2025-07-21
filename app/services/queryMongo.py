from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB
from app.schemas.log_preRegistro_schema import log_preRegistro # Importar el modelo de datos para validación

# llamar a request de preRegistro 
from app.services.requests_preRegistro import byId_get_preMatricula
from app.schemas.acudiente_schema import AcudienteBase
from app.schemas.usuario_schema import CrearUsuario

# Logs 
def get_logs_preRegsitro():
    # Obtener la colección de <prematriculas>
    pre_registration_collection = db["logs_prematricula"]

    # Obtener todos los documentos de la colección
    documents = list(pre_registration_collection.find())

    # Convertir los ObjectId a string para que sean serializables (Es decir evita errorres ya que JSON no puede entender ObjectId)
    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return documents

  
 