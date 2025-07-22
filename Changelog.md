# Changelog

Todas las modificaciones importantes a este proyecto se documentan en este archivo, agrupadas por fecha de publicación.

## [0.2.0] – 2025-07-21
### Added
- Middleware y endpoint de observabilidad Prometheus (`/adm_pre_registro/custom_metrics`) para peticiones, latencia y errores (commit `5280a45`, `6490087`).
- Actualización de `.gitignore` para ignorar byte-code de Python y carpetas `__pycache__` (commit `6490087`).

### Changed
- (—)

### Fixed
- (—)

---

## [0.1.0] – 2025-07-20
### Added
- Esquema inicial del servicio administrativo de pre-registro (commit `b84d24c`).
- Creación de rutas y esquemas básicos para pre-registro (commit `15fa9f0`, `ce6ef80`, `fd59eac`, `3e00641`).
- Funcionalidad de trazabilidad y logs en MongoDB (`logs_prematricula`) (commit `de1492e`).
- Políticas de branching Gitflow y reglas de protección (`gitflow-branch-policy.yml`) (commits `292bee4`, `1f18e3b`, `38548d3`).

### Changed
- Ajuste de puerto para el servicio de sedes (commit `68dd4f6`).

### Fixed
- (—)
