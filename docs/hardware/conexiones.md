# Conexiones del sistema

> Responsable: Hardware. Se actualiza cada vez que cambie el cableado. Si cambia algo que afecte a la carcasa (posición de un cable o conector), avisar al 3D.

## Diagrama

```
                                   ┌──────────────────────────────┐
  Batería / UPS HAT ══ 5V/5A ═════►│                              │
  (o fuente 27 W USB-C)            │                              │
                                   │        Raspberry Pi 5        │
  HAT M.2 + NVMe ◄═══ PCIe (FFC) ══│ PCIe                         │
  Active Cooler ◄──── FAN ─────────│ FAN                          │
  Camera Module 3 ◄── 22→15 pines ─│ CAM/DISP 0                   │
  Pantalla 5" ◄────── DSI 22 pines │ CAM/DISP 1   (o micro-HDMI 0)│
                                   │                              │
  Micrófono USB ◄──────────────────│ USB 2.0 (negro, arriba)      │
  Parlante USB ◄───────────────────│ USB 2.0 (negro, abajo)       │
  PCB botones (Pico) ◄─ micro-USB ─│ USB 3.0 (azul, arriba)       │
  (libre / teclado de depuración)  │ USB 3.0 (azul, abajo)        │
                                   └──────────────────────────────┘
```

## Tabla de conexiones

| Desde | Puerto en la Pi 5 | Cable / conector | Notas |
|---|---|---|---|
| Fuente o UPS | USB-C o pines de 5V del GPIO (según el HAT) | — | **Debe entregar 5A.** Si no, la Pi limita los USB a 600 mA. Verificar con `vcgencmd get_throttled` (`0x0` = OK) |
| SSD NVMe | PCIe (FFC 16 pines) | FFC incluido con el HAT M.2 | Activar el arranque desde NVMe (ver [`despliegue/`](../../despliegue/README.md)) |
| Active Cooler | FAN (4 pines JST) | Incluido | Obligatorio con el LLM a carga máxima |
| Camera Module 3 | CAM/DISP 0 | FFC **22→15 pines** | La cara de contactos se orienta según la serigrafía de la Pi |
| Pantalla 5" (DSI) | CAM/DISP 1 | FFC **22 pines** (o adaptador 22→15) | Si la pantalla es HDMI: micro-HDMI 0 + cable o adaptador en ángulo |
| Táctil de la pantalla | USB o I2C (según el modelo) | Según el fabricante | Completar al recibir la pantalla |
| Micrófono USB | USB 2.0 | Directo | Lejos del parlante y del ventilador para evitar eco y ruido |
| Parlante USB | USB 2.0 | Directo | |
| PCB de botones | USB 3.0 | micro-USB → USB-A en ángulo | Detalle de los pines: sección 5.4 del [plan](../plan.md) |

## Pendientes de verificar al recibir los componentes

- [ ] El HAT de batería y el HAT M.2 se apilan sin chocar (altura, pines, FFC)
- [ ] El HAT de batería mantiene 5A con el LLM a carga máxima + USB conectados
- [ ] Modelo exacto de la pantalla y su conexión (DSI o HDMI, táctil por USB o I2C)
- [ ] Largo necesario de cada FFC dentro de la carcasa
- [ ] Fotos del cableado real en `docs/img/` (`conexiones-v1.jpg`)
