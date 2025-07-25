# Request para obtener la pre-matricula del SERVICIO-PRE-REGISTRO 
import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings

# Función para obtener la lista de estudiantes en pre-registro desde el SERVICIO DE PRE-REGISTRO
def get_preMatriculas():
    try:
        # Construir la URL del endpoint del servicio de pre-registro
        url = f"{settings.url_api_sga_preRegistro}/pre_registration"

        # Realizar la solicitud GET al servicio
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener pre-matrículas. Código: {response.status_code}")
            return None

    except Exception as e:
        print("Excepción durante la solicitud:", e)
        return None

# Funcion borrar prematricula 
def delete_preMatricula(id:str):
    try:
        # Construir la URL del endpoint del servicio de pre-registro
        url = f"{settings.url_api_sga_preRegistro}/pre_registration/{id}"

        # Realizar la solicitud GET al servicio
        response = requests.delete(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al borrar pre-matrícula con id-{id} Código: {response.status_code}")
            return None

    except Exception as e:
        print("Excepción durante la solicitud:", e)
        return None
    


# Obtener el id de prematricula por Documento_identidad_estudiante     
def byStudent_document_getId_preMatricula(studentNumberDocument:str):
    try:
        # Construir la URL del endpoint del servicio de pre-registro
        url = f"{settings.url_api_sga_preRegistro}/pre_registration/getId/{studentNumberDocument}"

        # Realizar la solicitud GET al servicio
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener el ID de pre-matrículas. Código: {response.status_code}")
            return None

    except Exception as e:
        print("Excepción durante la solicitud:", e)
        return None
    
# obtener la prematricula por numero de estudiante 
def byStudent_document_get_preMatricula(studentNumberDocument:str):
    try:

        id_prematricula = byStudent_document_getId_preMatricula(studentNumberDocument)
        

        if id_prematricula is not None: 
            id = id_prematricula.get("id_")
            print(id)

            # Construir la URL del endpoint del servicio de pre-registro
            url = f"{settings.url_api_sga_preRegistro}/pre_registration/{id}"

            # Realizar la solicitud GET al servicio
            response = requests.get(url)

            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener prematricula con ID {id_prematricula}. Código: {response.status_code}")
                return None
        else:
            print(f"Error al obtener pre-matrícula")
            return None

    except Exception as e:
        print("Excepción durante la solicitud:", e)
        return None

   
# obtener la prematricula por id_prematricula 
def byId_get_preMatricula(id:str):
    try:

        # Construir la URL del endpoint del servicio de pre-registro
        url = f"{settings.url_api_sga_preRegistro}/pre_registration/{id}"

        # Realizar la solicitud GET al servicio
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # print(response.json())
            return response.json()
        else:
            print(f"Error al obtener prematricula con ID {id}. Código: {response.status_code}")
            return None

    except Exception as e:
        print("Excepción durante la solicitud:", e)
        return None
    

