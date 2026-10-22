# Lista de materiales (BOM) y presupuesto

> Responsable: Hardware (el 3D completa su sección). Documento vivo: se actualiza al comprar. **Verificar la compatibilidad antes de pagar** (ver [conexiones.md](conexiones.md) y la sección 2 del [plan](../plan.md)).

## Electrónica principal

| # | Componente | Especificación mínima | Cant. | Proveedor / enlace | Precio unit. | Total | Comprado | Recibido |
|---|---|---|---|---|---|---|---|---|
| 1 | Raspberry Pi 4 | 8 GB RAM (mínimo 4 GB) | 1 | | | | [ ] | [ ] |
| 2 | Refrigeración | Disipadores + ventilador 5V (conexión a GPIO) | 1 | | | | [ ] | [ ] |
| 3 | SSD | SATA o NVMe pequeño, ≥ 128 GB | 1 | | | | [ ] | [ ] |
| 4 | Adaptador / carcasa USB 3.0 para el SSD | Compatible con UASP y arranque en Pi 4 | 1 | | | | [ ] | [ ] |
| 5 | HAT/UPS de batería | Salida 5V/3A sostenida; que deje libres los pines 5V/GND | 1 | | | | [ ] | [ ] |
| 6 | Fuente | Oficial 15 W USB-C (5.1V/3A) | 1 | | | | [ ] | [ ] |
| 7 | Pantalla táctil | 5", 800x480, IPS; DSI 15 pines o micro-HDMI; preferir táctil que no use USB | 1 | | | | [ ] | [ ] |
| 8 | microSD | ≥ 32 GB, solo para pruebas iniciales | 1 | | | | [ ] | [ ] |
| 9 | Micrófono | USB, compacto, omnidireccional | 1 | | | | [ ] | [ ] |
| 10 | Parlante | USB, con amplificador integrado | 1 | | | | [ ] | [ ] |

> Sin cámara por ahora ([ADR 0003](../decisiones/0003-raspberry-pi-4-sin-vision.md)).

## PCB de controles

Detalle y huellas en la sección 5.3 del [plan](../plan.md) y en [`pcb/README.md`](../../pcb/README.md).

| # | Componente | Especificación | Cant. | Precio unit. | Total | Comprado |
|---|---|---|---|---|---|---|
| 11 | Raspberry Pi Pico (o Pico H) | RP2040 | 1 (+1 de repuesto) | | | [ ] |
| 12 | Tira hembra 1x20 | 2.54 mm | 2 | | | [ ] |
| 13 | Pulsador táctil 6x6 THT | Altura según el frontal | 8 (+4) | | | [ ] |
| 14 | Pulsador táctil 12x12 THT | | 1 (+1) | | | [ ] |
| 15 | LED 3 mm | | 1 (+2) | | | [ ] |
| 16 | Resistencia 330 Ω 1/4 W | | 1 (+2) | | | [ ] |
| 17 | Fabricación de la PCB | 2 capas, 1.6 mm, 5 unidades + envío | 1 | | | [ ] |
| 18 | Cable micro-USB → USB-A | Corto, en ángulo | 1 | | | [ ] |

## Carcasa (completa: 3D)

| # | Material | Especificación | Cant. | Precio unit. | Total | Comprado |
|---|---|---|---|---|---|---|
| 19 | Filamento | PLA o PETG, color base | 1–2 kg | | | [ ] |
| 20 | Masilla de relleno | | 1 | | | [ ] |
| 21 | Imprimación (primer) | En aerosol | 1 | | | [ ] |
| 22 | Pintura | Turquesa BMO, + colores de los botones | | | | [ ] |
| 23 | Barniz | Mate o satinado | 1 | | | [ ] |
| 24 | Lijas | Granos 120, 220, 400 | | | | [ ] |
| 25 | Insertos roscados | M2.5 | 20 | | | [ ] |
| 26 | Tornillos y separadores | M2.5, varios largos | 1 juego | | | [ ] |
| 27 | Imanes de neodimio | Para brazos y piernas (medida según el diseño) | | | | [ ] |

## Resumen

| Categoría | Total |
|---|---|
| Electrónica principal | |
| PCB de controles | |
| Carcasa | |
| **Total del proyecto** | |
| Presupuesto aprobado | |
