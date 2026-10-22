# 0003. Raspberry Pi 4 y sin visión artificial por ahora

- **Estado:** Aceptada
- **Fecha:** 2026-10-22
- **Autor/a:** Equipo
- **Áreas afectadas:** Todas

## Contexto

El plan inicial seguía el video de referencia: Raspberry Pi 5 de 16 GB, SSD NVMe por PCIe y cámara con un modelo de visión (Moondream). El equipo trabajará con una **Raspberry Pi 4** y decidió **no incluir visión artificial** en esta etapa.

## Decisión

- Placa: **Raspberry Pi 4** (se recomienda 8 GB).
- **Sin cámara ni modelo de visión.** Se eliminan la herramienta `ver_camara`, el estado `MIRANDO`, el módulo `vision.py` y la cámara de la lista de materiales.
- El botón Triángulo pasa de "tomar foto" a **"repetir la última respuesta"**.

## Consecuencias

| Tema | Cambio |
|---|---|
| Modelos | `gemma3:270m` o `gemma3:1b` en lugar de `gemma3:4b`; Whisper `tiny` |
| Latencia | Objetivo provisional de < 6 s (antes < 4 s), a confirmar con el benchmark de la semana 2 |
| Almacenamiento | SSD por USB 3.0 (la Pi 4 no tiene PCIe) |
| Energía | 5V/3A (antes 5V/5A) |
| Refrigeración | Disipadores + ventilador de 5V por GPIO (no existe el Active Cooler oficial para Pi 4) |
| Pantalla | Conector DSI de 15 pines directo, sin adaptador |
| Herramientas por pregunta | Máximo 1 (antes 2), para no sumar llamadas al LLM |
| Riesgo principal | La velocidad del LLM pasa a probabilidad **alta** |

La arquitectura permite agregar visión más adelante como una herramienta nueva, sin rehacer el resto.
