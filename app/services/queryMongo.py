from app.backend.session import db # Importar la base de datos desde el archivo de sesión
from fastapi import HTTPException # para manejar excepciones HTTP
from bson import ObjectId # para manejar ObjectId de MongoDB
from app.schemas.log_preRegistro import log_preRegistro # Importar el modelo de datos para validación


def get_logs_preRegsitro():
    # Obtener la colección de <prematriculas>
    pre_registration_collection = db["logs_prematricula"]

    # Obtener todos los documentos de la colección
    documents = list(pre_registration_collection.find())

    # Convertir los ObjectId a string para que sean serializables (Es decir evita errorres ya que JSON no puede entender ObjectId)
    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return documents

# def getPrematricula_byId(id:str):
#     pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

#     try:
#         objeto_Id = ObjectId(id) # Primero convertimos el id a ObjectId  porque MongoDB utiliza este tipo de dato para los identificadores únicos, Si no da error.
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")

#     # Buscar el Objeto o documento por su ID
#     document = pre_registration_collection.find_one({"_id": objeto_Id})

#     # Convertir los ObjectId a string para que sean serializables (Es decir evita errorres ya que JSON no puede entender ObjectId)
#     if document:
#         document["_id"] = str(document["_id"])
#         return document
#     else:
#         raise HTTPException(status_code=404, detail="Documento no encontrado")


# def getId_preRegistration_byStudentNumber(studentNumber:str):
#     pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

#     # Buscar documento por su numero Documento 
#     document = pre_registration_collection.find_one({"numeroDocumento": studentNumber})

#     if not document:    
#         raise HTTPException(status_code=404, detail="Documento o numeroDocumento no encontrado")
    
#     # Encontrar el id 
#     idStudent =  str(document["_id"])

#     # pasar el id en formato JSON
#     return idStudent

# def deletePreRegistration_byId(id:str):
#     pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

#     try:
#         objeto_Id = ObjectId(id)  # Convertir el id a ObjectId
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")
    
#     # Buscar el documento por su ID
#     document = pre_registration_collection.find_one({"_id": objeto_Id})

#     if not document:    
#         raise HTTPException(status_code=404, detail="Documento no encontrado")
#     # Eliminar el documento
#     pre_registration_collection.delete_one({"_id": objeto_Id}) 

#     return True


# def put_preRegistration(document:form_pre_registro, id:str):
#     # verificar que el documento tenga los campos necesarios 
#     # No se hace porque el modelo PreRegistrationModel ya tiene los campos necesarios definidos y validados

#     pre_registration_collection = db["prematriculas"] # Obtener la colección de <prematriculas>

#     # Convertir el modelo a un diccionario
#     document_dict = document.model_dump() # Convertir el modelo Pydantic a un diccionario

#     try:
#         objeto_Id = ObjectId(id)  # Convertir el id a ObjectId
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"ID inválido, error: {str(e)}")
    
#     filter = {"_id": objeto_Id}

#     # Hacer un remplazo con un filtro 
#     resultado = pre_registration_collection.replace_one(filter, document_dict)

#     if resultado.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Documento no encontrado")
    
#     return(True)

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
