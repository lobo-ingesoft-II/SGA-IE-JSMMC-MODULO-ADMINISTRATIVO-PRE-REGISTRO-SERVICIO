import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings
from app.schemas.estudiante import EstudianteBase

# Funcion para crear un estudiante en el SERVICIO-ESTUDIANTE 
def CrearEstudiante(estudiante_data:dict):

    try:
        # Validar usando Pydantic
        estudiante = EstudianteBase(**estudiante_data)

        # Convertir a dict para requests (puedes usar .model_dump() si estás en Pydantic v2)
        estudiante_dict = estudiante.model_dump()

        # Crear la URL del servidor de la API de pre-registro 
        url_servidor = settings.url_api_sga_estudiante

        # *POST* /estudiantes/
        url = url_servidor + f"/estudiantes/"  
    
        # Realizar la solicitud POST aL servicio 
        response = requests.post(url, json=estudiante)
        response.body
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        
        if response.status_code == (200,201):

            data = response.json()  # Obtener los datos en formato JSON
            return data  # Retorna el objeto completo del profesor
       
        else:
            return None
    
    except Exception as e:
        print("Error de validación Pydantic:", e)
        return None




# # Registrar rutas
# app.include_router(estudiantes.router, prefix="/estudiantes", tags=["Estudiantes"])
# 
# @router.post("/", response_model=EstudianteResponse)
# def create(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
#     # Validar acudiente
#     if estudiante.id_acudiente is not None:
#         response = requests.get(f"{API_AUTH_URL}/{estudiante.id_acudiente}")
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Acudiente no válido")

#     # Validar curso
#     if estudiante.id_curso is not None:
#         response = requests.get(f"{API_CURSOS_URL}/{estudiante.id_curso}")
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Curso no válido")

#     # Validar sede
#     response = requests.get(f"{API_SEDES_URL}/{estudiante.id_sede}")
#     if response.status_code != 200:
#         raise HTTPException(status_code=400, detail="Sede no válida")

#     return create_estudiante(db, estudiante)



