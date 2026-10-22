# ia/ — Recursos de inteligencia artificial

> Responsable: **Desarrollador de IA**.
>
> Aquí van los recursos de IA que **no son código de BMO en ejecución**: prompts, entrenamiento de la wake word, benchmarks y documentos para RAG. El código que usa todo esto está en [`software/bmo/`](../software/README.md) (`voz/`, `llm.py`, `vision.py`).

## Estructura a llenar

```
ia/
├── README.md
├── prompts/
│   ├── sistema.md              ← prompt de sistema: personalidad de BMO + formato JSON de herramientas
│   ├── herramientas.md         ← descripción de cada herramienta tal como la lee el LLM
│   ├── preguntas_prueba.md     ← 20 preguntas fijas + respuesta esperada (para pruebas y latencia)
│   └── CHANGELOG.md            ← qué cambió en el prompt y por qué (con resultado de las 20 preguntas)
├── wakeword/
│   ├── README.md               ← cómo se entrenó: notebook, parámetros, cantidad de muestras
│   ├── entrenamiento.ipynb     ← notebook de openWakeWord (Colab) para "Hey BMO"
│   ├── hey_bmo.onnx            ← modelo entrenado (se sube: pesa poco)
│   ├── pruebas.md              ← tasa de activaciones falsas por hora y detecciones a 1, 2 y 3 m
│   ├── datos/                  ← (ignorado por git) muestras generadas
│   └── salida/                 ← (ignorado por git) archivos intermedios
├── benchmarks/
│   ├── README.md               ← metodología: hardware, temperatura, cómo repetirlo
│   ├── bench_llm.py            ← tokens/s, tiempo hasta la primera palabra y RAM de cada modelo
│   ├── bench_stt.py            ← tiempo de Whisper por modelo y motor, con audios de prueba
│   ├── bench_vision.py         ← tiempo y calidad: Moondream vs Gemma 3
│   ├── resultados/
│   │   └── AAAA-MM-DD_<prueba>.csv
│   └── informe.md              ← conclusiones → alimentan los ADR de modelos
└── notas_rag/
    ├── README.md               ← qué documentos puede consultar BMO y en qué formato
    └── *.md                    ← notas en texto (datos del equipo, del proyecto, de BMO)
```

## Formato de los resultados de benchmark

CSV con estas columnas (una fila por ejecución):

```
fecha,dispositivo,modelo,cuantizacion,prueba,tokens_por_s,primera_palabra_ms,total_ms,ram_mb,temp_c,throttled
```

- Siempre en la **Pi 5 real** (para referencia, también en PC, con `dispositivo=pc`).
- Mínimo **5 repeticiones** por combinación; se reporta la mediana.
- Anotar si la Pi estaba en la carcasa o abierta.

## Reglas del prompt de sistema

- Respuestas de **1 a 3 frases** (se van a escuchar, no a leer).
- Sin Markdown, emojis ni listas: Piper los leería en voz alta.
- Siempre en español, con la personalidad de BMO (juguetón, curioso, amable).
- Cualquier cambio se valida con las 20 preguntas de prueba y se anota en `CHANGELOG.md`.

## Checklist

- [ ] S1–2: Benchmarks LLM, STT y visión + `informe.md` → ADR de modelos
- [ ] S3: `hey_bmo.onnx` entrenado + `pruebas.md`
- [ ] S4: `sistema.md` v1 + `preguntas_prueba.md`
- [ ] S5: `herramientas.md`
- [ ] S6–7: Ajuste de personalidad (CHANGELOG)
- [ ] Opcional: `notas_rag/` con al menos 5 documentos
