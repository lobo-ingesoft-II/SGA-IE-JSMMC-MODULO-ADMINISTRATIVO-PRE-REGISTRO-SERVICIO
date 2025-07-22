import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings

def byName_sede_get_sede(name_sede:str):
    try:
       
        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_sedes

        # *get* /sedes/get_by_name/{name_sede}
        url = url_servidor + f"/sedes/get_by_name/{name_sede}"  
    
        # Realizar la solicitud POST aL servicio 
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