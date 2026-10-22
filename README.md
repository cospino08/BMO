# BMO — Agente IA local con cuerpo físico

BMO es un asistente de inteligencia artificial que funciona **100 % en local** sobre una Raspberry Pi 4. Escucha, piensa y habla sin depender de la nube, con cara animada en pantalla, botones físicos y una carcasa impresa en 3D inspirada en BMO de *Hora de Aventura*.

| Capacidad | Tecnología |
|---|---|
| Palabra de activación ("Hey BMO") | openWakeWord |
| Voz → texto | faster-whisper / whisper.cpp |
| Razonamiento | Gemma 3 (270M o 1B) vía Ollama |
| Texto → voz | Piper |
| Botones | PCB propia + Raspberry Pi Pico como teclado USB |
| Carcasa | FreeCAD/Onshape (funcional) + Blender (estética), impresión 3D |

> **Estado:** planificación (semana 1). Sin visión artificial por ahora ([ADR 0003](docs/decisiones/0003-raspberry-pi-4-sin-vision.md)). Ver el [plan del proyecto](docs/plan.md).

---

## Estructura del repositorio

```
BMO/
├── README.md            ← estás aquí
├── CONTRIBUTING.md      ← cómo trabajar en el repo (ramas, commits, revisiones)
├── docs/                ← toda la documentación del proyecto
│   ├── plan.md          ← plan, roles, cronograma, riesgos
│   ├── arquitectura.md  ← cómo está construido el software
│   ├── contratos.md     ← interfaces entre áreas (fuente de verdad)
│   ├── decisiones/      ← registro de decisiones técnicas (ADR)
│   ├── hardware/        ← lista de materiales, conexiones, medidas, ensamblaje
│   ├── reuniones/       ← actas semanales
│   └── img/             ← diagramas y fotos usados en la documentación
├── software/            ← programa principal de BMO (Python) que corre en la Pi
├── ia/                  ← prompts, entrenamiento de wake word, benchmarks, notas RAG
├── firmware/            ← código de la Raspberry Pi Pico (botones → teclado USB)
├── pcb/                 ← proyecto KiCad y archivos de fabricación de la PCB
├── cad/                 ← modelos 3D de la carcasa (fuentes, STL, STEP)
└── despliegue/          ← instalación en la Pi: sistema operativo, dependencias, servicio
```

Cada carpeta tiene su propio `README.md` que explica **qué va ahí, quién la mantiene, en qué formato y cuándo se considera completa**.

## Equipo y carpetas

| Rol | Carpetas principales |
|---|---|
| Líder de Proyecto / Arquitecto de Software | `docs/`, `software/` (estados, agente, UI), `despliegue/` |
| Ingeniero de Hardware y Electrónica | `pcb/`, `firmware/`, `docs/hardware/` |
| Diseñador 3D y Modelador | `cad/`, `docs/hardware/medidas.md`, `docs/hardware/ensamblaje.md` |
| Desarrollador de IA | `ia/`, `software/bmo/voz/`, `software/bmo/llm.py` |

## Por dónde empezar

1. Lee el [plan](docs/plan.md) y busca la sección de tu rol.
2. Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de tu primer commit.
3. Lee los [contratos](docs/contratos.md): es lo que los demás esperan de tu parte.
4. Abre el `README.md` de tu carpeta y sigue su checklist.

## Documentos clave

- [Plan del proyecto](docs/plan.md)
- [Arquitectura del software](docs/arquitectura.md)
- [Contratos entre áreas](docs/contratos.md)
- [Decisiones técnicas](docs/decisiones/README.md)
- [Lista de materiales](docs/hardware/bom.md)
- [Conexiones del sistema](docs/hardware/conexiones.md)
