from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB
from app.schemas.log_preRegistro import log_preRegistro # Importar el modelo de datos para validación

# llamar a request de preRegistro 
from app.services.requests_preRegistro import byId_getPrematricula

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

def createDic_estudiante(id_prematricula, id_sede, id_curso):

    # primero traer la prematricula 
    document = byId_getPrematricula(id_prematricula)

    if document is not None:
        document_dict = document.model_dump()

        names = document_dict["nombres"]
        last_names = document_dict["apellidos"]
        type_document = document_dict["tipoDocumento"]
        number_document = document_dict["numeroDocumento"]
        cell = document_dict["telefono"]
        email = "No Corresponde"
        bird_date = document_dict["fechaNacimiento"]
    #     id_parent = 




    # else:



# class EstudianteBase(BaseModel):
#     nombres: str
#     apellidos: str
#     tipo_documento: str
#     documento_identidad: str
#     telefono: Optional[str] = None
#     email: EmailStr
#     fecha_nacimiento: Optional[date] = None
#     id_acudiente: Optional[int] = None
#     id_curso: Optional[int] = None
#     id_sede: int
#     estado_matricula: Optional[Literal['pre-matriculado', 'matriculado', 'retirado']] = 'pre-matriculado'


# def createPreRegistration(document:form_pre_registro):
       
#    # verificar que el documento tenga los campos necesarios 
#    # No se hace porque el modelo PreRegistrationModel ya tiene los campos necesarios definidos y validados

#     pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

#     # Convertir el modelo a un diccionario
#     document_dict = document.model_dump() # Convertir el modelo Pydantic a un diccionario

#     # No es necesario crear un ObjectId manualmente, MongoDB lo genera automáticamente al insertar el documento con insert_one

#     # Insertar el documento en la colección
#     result = pre_registration_collection.insert_one(document_dict)

#     # Convertir el ObjectId a string para que sea serializable
#     document_dict["_id"] = str(result.inserted_id)
#     return document_dict
