# Plano de medidas de los componentes

> Responsable: Hardware (mide). Consume: 3D (modela). Versión actual: **v0.0** (sin medir).
>
> Reglas:
> - Todas las medidas en **mm**, tomadas con calibre sobre el componente **real**. Una medida sacada de la ficha técnica se marca como `(FT)` y se reemplaza al recibir la pieza.
> - Cada cambio sube la versión y se anota en el historial (abajo).
> - Ejes: **X** = ancho (izquierda → derecha, mirando a BMO de frente), **Y** = alto, **Z** = profundidad (frente → atrás).

## Componentes

| Componente | X | Y | Z | Agujeros de montaje (diámetro / posición) | Conectores y por qué lado salen | Espacio extra para cables | Medido por | Fecha |
|---|---|---|---|---|---|---|---|---|
| Raspberry Pi 4 | 85 (FT) | 56 (FT) | | M2.5, 58 x 49 (FT) | USB/Ethernet: lado corto; USB-C y micro-HDMI: lado largo | | | |
| Pi 4 + disipadores + ventilador + HAT batería (pila completa) | | | | | | | | |
| SSD + adaptador USB | | | | | | | | |
| Pantalla 5" (módulo completo) | | | | | | | | |
| Área visible de la pantalla | | | — | — | — | — | | |
| Micrófono USB | | | | | | | | |
| Parlante USB | | | | | | | | |
| Batería (si va separada del HAT) | | | | | | | | |
| PCB de botones v1 | | | | M2.5 x 4 | USB de la Pico: ver el STEP | | | |
| Pulsador 6x6 (altura total con vástago) | 6 | 6 | | — | — | — | | |
| Pulsador 12x12 (altura total) | 12 | 12 | | — | — | — | | |

## Requisitos para la carcasa

| Requisito | Valor |
|---|---|
| Tolerancia de encaje (holgura por lado) | 0.2–0.3 mm (confirmar con la impresión de prueba) |
| Radio mínimo de curvatura de los FFC | |
| Separación mínima del ventilador a la pared | |
| Acceso sin desarmar | USB-C de carga, botón de encendido, SSD (o tapa) |
| Posición del micrófono | Lejos del parlante y del ventilador; con orificio hacia el frente |

## Historial

| Versión | Fecha | Cambio | Autor/a |
|---|---|---|---|
| v0.0 | 2026-10-22 | Plantilla creada con datos de las fichas técnicas | |
