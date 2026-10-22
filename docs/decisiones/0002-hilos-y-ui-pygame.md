# 0002. Un programa Python con hilos y UI en Pygame

- **Estado:** Propuesta
- **Fecha:** 2026-10-22
- **Autor/a:** Equipo (propuesta inicial de arquitectura)
- **Áreas afectadas:** Software, IA

## Contexto

BMO debe animar la cara, escuchar sin parar, pensar y hablar al mismo tiempo, en una Pi 4 donde la RAM y la CPU se reservan para los modelos.

## Opciones consideradas

| Opción | A favor | En contra |
|---|---|---|
| A. Un programa Python, hilos + colas, UI en Pygame | Simple; poca RAM; un solo proceso que lanzar y depurar; las teclas llegan directo a la ventana | Pygame debe estar en el hilo principal; animaciones más básicas |
| B. Backend Python + UI web en Chromium kiosko (WebSocket) | Animaciones más ricas (CSS/JS); UI separada | Chromium consume 300–500 MB de RAM; dos procesos que coordinar |
| C. Varios procesos con mensajería (ZeroMQ/MQTT) | Aislamiento de fallos | Demasiado complejo para un equipo de 4 en 9 semanas |

## Decisión

Opción **A**. Detalle en [`arquitectura.md`](../arquitectura.md).

## Evidencia

Pendiente: medir la RAM y la CPU libres con el LLM cargado (semana 2). En la Pi 4 la opción B es aún más costosa; solo se reevalúa si sobran más de 2 GB de RAM y la cara necesita más animación, reevaluar B.

## Consecuencias

- La comunicación entre hilos es solo por `queue.Queue`.
- Las expresiones de la cara son sprites PNG en `software/bmo/ui/expresiones/`.
