# API_PRE_REGISTRO/app/backend/session.py

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Importa la constante; si prefieres, puedes seguir usando settings.mongo_uri
from app.backend.config import MONGO_URI

# Crear cliente MongoDB
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

# Seleccionar la base de datos
db = client["GestionAdministrativa_db"]

try:
    client.admin.command("ping")
    print("Conexión a MongoDB exitosa.")
except Exception as e:
    print("Error al conectar a MongoDB:", e)
