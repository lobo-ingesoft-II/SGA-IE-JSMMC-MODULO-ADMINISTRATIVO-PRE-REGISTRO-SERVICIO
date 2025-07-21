import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings
from app.schemas.estudiante_schema import EstudianteBase
from datetime import date, datetime


# Funcion para crear un estudiante en el SERVICIO-ESTUDIANTE 
def create_estudiante(estudiante_data:dict):

    try:
        # Validar usando Pydantic
        estudiante = EstudianteBase(**estudiante_data)

        # Convertir a dict para requests (puedes usar .model_dump() si estás en Pydantic v2)
        estudiante_dict = estudiante.model_dump()

        # ...antes de enviar dic_estudiante...
        if isinstance(estudiante_dict.get("fecha_nacimiento"), (date, datetime)):
            estudiante_dict["fecha_nacimiento"] = estudiante_dict["fecha_nacimiento"].isoformat()


        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_estudiante

        # *POST* /estudiantes/
        url = url_servidor + f"/estudiantes/"  
    
        # Realizar la solicitud POST aL servicio 
        response = requests.post(url, json=estudiante_dict)
        # response.body
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        if response.status_code in (200,201):

            data = response.json()  # Obtener los datos en formato JSON
            return data  # Retorna el objeto completo del profesor
       
        else:
            return None
    
    except Exception as e:
        print("Error de validación Pydantic:", e)
        return None


