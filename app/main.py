from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import modulo_administrativo

# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
# from app.routers.pre_registration_route import REQUEST_COUNT_PRE_REGISTRATION_ROUTERS, REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS, ERROR_COUNT_PRE_REGISTRATION_ROUTERS


# Instancia de FastAPI
app = FastAPI()

# Importar las rutas
#Registrar rutas de estudiantes

app.include_router(modulo_administrativo.router,  prefix="/adm_pre_registro", tags=["administracion_preRegsitro"])

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)


# Middleware para observabilidad
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status = response.status_code
    except Exception as e:
        status = 500
        raise e
    finally:
        latency = time.time() - start_time
        endpoint = request.url.path
        method = request.method

        # REQUEST_COUNT_PRE_REGISTRATION_ROUTERS.labels(endpoint=endpoint, method=method).inc()
        # REQUEST_LATENCY_PRE_REGISTRATION_ROUTERS.labels(endpoint=endpoint, method=method).observe(latency)

        # if status >= 400:
        #     ERROR_COUNT_PRE_REGISTRATION_ROUTERS.labels(endpoint=endpoint, method=method, status_code=str(status)).inc()

    return response




if __name__ == '__main__':
    app.run(debug=True)