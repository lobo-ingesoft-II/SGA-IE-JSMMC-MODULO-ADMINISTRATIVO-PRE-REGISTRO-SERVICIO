import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings
from app.schemas.acudiente_schema import AcudienteBase
from app.schemas.usuario_schema import CrearUsuario


def create_acudiente(acudiente_data:dict):
    try:
        # Validar usando Pydantic
        acudiente = AcudienteBase(**acudiente_data)

        # Convertir a dict para requests (puedes usar .model_dump() si estás en Pydantic v2)
        acudiente_dict = acudiente.model_dump()

        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_autenticacion

        # *POST* /acudiente/
        url = url_servidor + f"/acudiente/register"  
    
        # Realizar la solicitud POST aL servicio 
        response = requests.post(url, json=acudiente_dict)
        # response.body
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        if response.status_code in (200 , 201):

            data = response.json()  # Obtener los datos en formato JSON
            return data  # Retorna el objeto completo del profesor
       
        else:
            return None
    
    except Exception as e:
        print("Error de validación Pydantic:", e)
        return None
    
def by_document_get_acudiente(numberDocument:str):
    try:
        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_autenticacion

        # *POST* /acudiente/
        url = url_servidor + f"/acudiente/get_by_document/{numberDocument}"  

        # Realizar la solicitud get al servicio 
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        if response.status_code == 200:

            data = response.json()  # Obtener los datos en formato JSON
            return data  # Retorna el objeto completo del profesor
        
        else:
            return None

    except Exception as e:
        print("Error de validación Pydantic:", e)
        return None
    
def create_usuario(usuario_data:dict):
    try:
        # Validar usando Pydantic
        usuario = CrearUsuario(**usuario_data)

        # Convertir a dict para requests (puedes usar .model_dump() si estás en Pydantic v2)
        usuario_dict = usuario.model_dump()

        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_autenticacion

        # *POST* /acudiente/
        url = url_servidor + f"/admin/usuarios"  
    
        # Realizar la solicitud POST aL servicio 
        response = requests.post(url, json=usuario_dict)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        print("Response status code:", response.status_code)
        import json
        print("JSON a enviar:", json.dumps(usuario_dict, ensure_ascii=False))
        if response.status_code in (200,201):

            data = response.json()  # Obtener los datos en formato JSON
            return data  # Retorna el objeto completo del profesor
       
        else:
            return None
    
    except Exception as e:
        print("Error de validación Pydantic:", e)
        return None

def delete_usuario(id_usuario:int):
    try:
        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_autenticacion

        # *DELETE* /acudiente/
        url = url_servidor + f"/admin/usuarios/{id_usuario}"  
    
        # Realizar la solicitud DELETE al servicio 
        response = requests.delete(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        if response.status_code in (200,204,201):  # No content
            return True
        
        else:
            return False
    
    except Exception as e:
        print("Error de validación Pydantic:", e)
        return False