# software/ — Programa principal de BMO

> Responsables: **Líder** (estados, agente, UI, herramientas) e **IA** (voz, LLM).
> Diseño: [`docs/arquitectura.md`](../docs/arquitectura.md). Interfaces: [`docs/contratos.md`](../docs/contratos.md).

Programa Python que corre en la Raspberry Pi 4. Se ejecuta con `python -m bmo`.

## Estructura a llenar

```
software/
├── README.md                 ← este archivo
├── pyproject.toml            ← dependencias y metadatos (Líder, S1)
├── config.example.yaml       ← copia de contratos §4; se copia como config.yaml (Líder, S1)
├── bmo/
│   ├── __init__.py
│   ├── __main__.py           ← punto de entrada: carga la config, lanza los hilos y abre la UI (Líder)
│   ├── config.py             ← lee y valida config.yaml (Líder)
│   ├── eventos.py            ← clase Evento y cola compartida (Líder)
│   ├── estados.py            ← máquina de estados: estados, transiciones y qué hacer en cada una (Líder)
│   ├── agente.py             ← hilo Agente: bucle de eventos, llamada al LLM, ejecución de herramientas (Líder)
│   ├── errores.py            ← ErrorBMO y utilidades de log (Líder)
│   ├── llm.py                ← pensar(): Ollama con streaming, JSON de herramientas, división en frases (IA)
│   ├── voz/
│   │   ├── __init__.py
│   │   ├── audio.py          ← captura continua del micrófono y búfer circular (IA)
│   │   ├── wake.py           ← DetectorWake con openWakeWord (IA)
│   │   ├── stt.py            ← escuchar(): VAD (Silero) + Whisper (IA)
│   │   └── tts.py            ← hablar() / detener_habla(): cola + Piper + reproducción (IA)
│   ├── herramientas/
│   │   ├── __init__.py       ← registro automático de herramientas (Líder)
│   │   ├── notas.py          ← consultar_notas → RAG sobre ia/notas_rag/ (IA)
│   │   ├── hora.py           ← hora_fecha (Líder)
│   │   └── web.py            ← buscar_web, opcional; sin internet devuelve "sin conexión" (Líder)
│   └── ui/
│       ├── __init__.py
│       ├── cara.py           ← ventana Pygame: dibuja la expresión según el estado y publica TECLA_* (Líder)
│       └── expresiones/      ← sprites PNG, uno o varios por estado (Líder / 3D para el arte)
├── tests/
│   ├── simulados/            ← versiones falsas de stt, llm, tts y wake con la misma firma (Líder + IA)
│   ├── test_estados.py       ← transiciones válidas e inválidas
│   ├── test_llm_parseo.py    ← lectura del JSON del LLM y división en frases
│   └── test_herramientas.py  ← registro y ejecución de herramientas
└── scripts/
    ├── probar_microfono.py   ← graba 5 s y reproduce (diagnóstico de audio)
    ├── probar_botones.py     ← muestra en pantalla cada tecla recibida
    └── prueba_latencia.py    ← mide cada etapa con ia/prompts/preguntas_prueba.md
```

## Reglas

- **Python 3.11+** (el que trae Raspberry Pi OS Bookworm).
- Las dependencias van en `pyproject.toml` con versión mínima. Nada se instala "a mano" sin documentarlo.
- **Ningún valor fijo** (modelos, umbrales, rutas) en el código: todo sale de `config.yaml`.
- **Comunicación entre hilos solo por colas.**
- Cada función pública de un contrato lleva una *docstring* breve.
- Formato y análisis con `ruff` (`ruff format` y `ruff check`) antes de cada PR.
- `pytest` debe pasar en un PC **sin hardware** (usando `tests/simulados/`).

## Cómo ejecutar (completar en S2)

```bash
cd software
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp config.example.yaml config.yaml
python -m bmo                 # en la Pi
python -m bmo --simulado      # en un PC, sin micrófono (entrada y salida por texto)
pytest
```

## Checklist

- [ ] S1: `pyproject.toml`, `config.example.yaml`, estructura de carpetas
- [ ] S2: `eventos.py`, `estados.py`, `agente.py` y modo `--simulado` funcionando en PC
- [ ] S3: `ui/cara.py` con 5 expresiones
- [ ] S4: Registro de herramientas + `hora.py`
- [ ] S4: Módulos de voz (IA) cumpliendo el contrato
- [ ] S5–6: Integración en la Pi
- [ ] S7: Scripts de diagnóstico y `prueba_latencia.py`
- [ ] Tests pasando en PC
