# Cómo trabajar en este repositorio

## Ramas

- `main` siempre debe funcionar. **Nadie hace push directo a `main`.**
- Cada tarea se hace en su propia rama, con el prefijo del área:

| Prefijo | Área | Ejemplo |
|---|---|---|
| `sw/` | Software principal | `sw/maquina-estados` |
| `ia/` | Modelos, voz, prompts | `ia/wake-word-hey-bmo` |
| `hw/` | PCB, firmware, conexiones | `hw/pcb-v1` |
| `cad/` | Carcasa 3D | `cad/frontal-v2` |
| `docs/` | Solo documentación | `docs/acta-semana-3` |

## Commits

- En español, en imperativo, y diciendo **qué** cambia: `Agrega detección de silencio con Silero`, `Corrige huella del pulsador SW5`.
- Un commit = un cambio lógico. No mezclar, por ejemplo, la PCB con el prompt de BMO.
- No subir archivos generados que se pueden reconstruir (ver `.gitignore`).

## Pull requests

1. Abre el PR hacia `main` con una descripción corta: qué hace, cómo se probó y capturas o fotos si aplica.
2. **Al menos una persona de otra área** lo revisa. Así todos conocen el proyecto completo.
3. Si el PR cambia algo de [`docs/contratos.md`](docs/contratos.md), deben aprobarlo **todas las áreas afectadas**.
4. Si el PR toma una decisión técnica importante, agrega un ADR en [`docs/decisiones/`](docs/decisiones/README.md).

## Versiones de piezas físicas

La PCB, la carcasa y el plano de medidas usan versiones `vMAYOR.MENOR`:

- **MAYOR** cambia cuando la pieza deja de ser compatible con la anterior (otro tamaño, otros agujeros, otros pines).
- **MENOR** cambia con ajustes compatibles (serigrafía, tolerancias, estética).

Cada versión fabricada o impresa se marca con un tag de git: `pcb-v1.0`, `cad-v2.1`.

## Archivos grandes

- Los modelos de IA (`.gguf`, pesos de Ollama, Whisper, voces de Piper) **no se suben**. Se documenta en `despliegue/README.md` cómo descargarlos.
- STL, STEP y `.blend` sí se suben. Si algún archivo supera **50 MB**, avísalo al equipo antes: se evaluará usar Git LFS.
- Las fotos para la documentación van comprimidas (JPG, ancho máximo de 1600 px).

## Reunión semanal

Cada semana se crea un acta en [`docs/reuniones/`](docs/reuniones/README.md) con lo hecho, lo pendiente, los bloqueos y las decisiones.
