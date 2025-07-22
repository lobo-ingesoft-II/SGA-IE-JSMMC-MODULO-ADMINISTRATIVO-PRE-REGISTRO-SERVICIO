from pydantic import BaseModel, Field # esta librería permite definir modelos de datos y validarlos automáticamente

# OJO NO NECESITA CONSTRUCTOR, Pydantic maneja la creación de instancias automáticamente
class log_preRegistro(BaseModel):
    opcion: str
    id_preRegistro: str
    numeroDocumento_estudiante: str
    dic_preRegistro: dict = Field(default=None)  # Este campo es opcional, puede ser None o un diccionario con datos adicionales