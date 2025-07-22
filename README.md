# SGA-IE-JSMMC-MODULO-ADMINISTRATIVO-PRE-REGISTRO-SERVICIO

Módulo administrativo de pre-registro del Sistema de Gestión Académica (SGA), implementado con FastAPI, Python y MongoDB. Incluye registro de logs, gestión de solicitudes de pre-matrícula y observabilidad vía Prometheus.

---

## 📋 Endpoints

| Método  | Ruta                                           | Descripción                                           |
|--------:|-----------------------------------------------|-------------------------------------------------------|
| **GET**  | `/adm_pre_registro/custom_metrics`            | Métricas Prometheus (peticiones, latencia, errores)   |
| **GET**  | `/adm_pre_registro/log_pre_registros`         | Listar todos los logs de pre-registro                 |
| **GET**  | `/adm_pre_registro/pre_registros`             | Obtener todas las solicitudes de pre-registro         |
| **POST** | `/adm_pre_registro/prematricula/rechazar/{id}`| Rechazar una solicitud de pre-matrícula (`id` prematricula) |
| **POST** | `/adm_pre_registro/prematricula/aceptar/{id_preRegistro}/{id_curso}` | Aceptar pre-matrícula y crear estudiante en curso   |
| **GET**  | `/adm_pre_registro/prematricula/buscar/{numero_documento}` | Buscar pre-matrícula por número de documento estudiante |

---

## 🚀 Requisitos

- Python 3.10 o superior  
- pip  
- MongoDB (Atlas o local)  
- Conexión HTTP a los servicios SGA de Estudiante, Autenticación y Sedes

---

## 🛠️ Instalación

```bash
git clone https://github.com/lobo-ingesoft-II/SGA-IE-JSMMC-MODULO-ADMINISTRATIVO-PRE-REGISTRO-SERVICIO.git
cd SGA-IE-JSMMC-MODULO-ADMINISTRATIVO-PRE-REGISTRO-SERVICIO

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```
## ⚙️ Configuración
Copia .env.example a .env y ajusta:
```bash
MONGO_URI=<tu_mongodb_uri>
SERVIDOR_API_ESTUDIANTE_URL=http://localhost:8005
SERVIDOR_API_PRE_REGISTRO_URL=http://localhost:8010
SERVIDOR_API_SEDES_URL=http://localhost:8000
SERVIDOR_API_AUTENTICACION_URL=http://localhost:8009
```

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload --port 8013
```

- API disponible en http://localhost:8013

- Swagger UI en http://localhost:8013/docs

## 📈 Observabilidad

### 1. Realiza llamadas a cualquier endpoint bajo /adm_pre_registro/....

### 2. Consulta métricas Prometheus en:

```bash
http://localhost:8013/adm_pre_registro/custom_metrics
```

Encontrarás:

- http_requests_total{endpoint="…",method="…"}

- http_request_duration_seconds_bucket{endpoint="…",method="…",le="…"}

- http_request_errors_total{endpoint="…",method="…",status_code="…"}
