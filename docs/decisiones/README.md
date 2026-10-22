# Registro de decisiones técnicas (ADR)

Un ADR (*Architecture Decision Record*) es un documento corto que explica **por qué** se eligió algo. Sirve para que, dentro de un mes, nadie tenga que adivinar por qué se usa Pygame y no Chromium, o la Pico y no los GPIO de la Pi.

## Cuándo escribir uno

- Al elegir entre tecnologías o modelos (por ejemplo, `gemma3:1b` vs `4b`).
- Al decidir algo que afecta a otra área (conexiones, medidas, contratos).
- Al descartar algo del plan original.

## Cómo

1. Copia [`0000-plantilla.md`](0000-plantilla.md) como `NNNN-titulo-corto.md`, usando el número siguiente.
2. Complétalo y súbelo en un PR. El estado empieza en **Propuesta**.
3. Cuando el equipo lo aprueba, pasa a **Aceptada**.
4. Los ADR no se borran. Si una decisión cambia, se escribe uno nuevo y el anterior queda como **Reemplazada por NNNN**.

## Índice

| N.º | Decisión | Estado | Área |
|---|---|---|---|
| [0001](0001-botones-por-usb-hid.md) | Botones mediante Raspberry Pi Pico como teclado USB | Propuesta | Hardware |
| [0002](0002-hilos-y-ui-pygame.md) | Un programa Python con hilos y UI en Pygame | Propuesta | Software |
| [0003](0003-raspberry-pi-4-sin-vision.md) | Raspberry Pi 4 y sin visión artificial por ahora | Aceptada | Todas |

**Pendientes (semana 2, según los benchmarks):** modelo LLM, motor de Whisper.
