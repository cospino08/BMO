# Conexiones del sistema

> Responsable: Hardware. Se actualiza cada vez que cambie el cableado. Si cambia algo que afecte a la carcasa (posición de un cable o conector), avisar al 3D.

## Diagrama

```
                                   ┌──────────────────────────────┐
  Batería / UPS HAT ══ 5V/3A ═════►│                              │
  (o fuente oficial 15 W USB-C)    │                              │
                                   │        Raspberry Pi 4        │
  Ventilador 5V ◄──── GPIO 5V/GND ─│ pines 4 (5V) y 6 (GND)       │
  Pantalla 5" ◄────── DSI 15 pines │ DISPLAY      (o micro-HDMI 0)│
                                   │                              │
  SSD (adaptador USB) ◄────────────│ USB 3.0 (azul)               │
  PCB botones (Pico) ◄─ micro-USB ─│ USB 3.0 (azul)               │
  Micrófono USB ◄──────────────────│ USB 2.0 (negro)              │
  Parlante USB ◄───────────────────│ USB 2.0 (negro)              │
                                   └──────────────────────────────┘
```

## Tabla de conexiones

| Desde | Puerto en la Pi 4 | Cable / conector | Notas |
|---|---|---|---|
| Fuente o UPS | USB-C o pines de 5V del GPIO (según el HAT) | — | **Debe entregar 5V/3A.** Verificar con `vcgencmd get_throttled` (`0x0` = OK) |
| SSD | USB 3.0 | Adaptador o carcasa USB 3.0 | Activar el arranque por USB (ver [`despliegue/`](../../despliegue/README.md)). Si el adaptador da problemas, revisar compatibilidad UASP |
| Ventilador 5V | GPIO pin 4 (5V) y pin 6 (GND) | Conector Dupont de 2 pines | Verificar que el HAT de batería deje esos pines libres o los replique |
| Pantalla 5" (DSI) | Conector DISPLAY | FFC de 15 pines | Si la pantalla es HDMI: micro-HDMI 0 + cable o adaptador en ángulo |
| Táctil de la pantalla | USB o I2C (según el modelo) | Según el fabricante | Si usa USB, no quedan puertos libres: considerar un hub USB pequeño o una pantalla con táctil por I2C/DSI |
| Micrófono USB | USB 2.0 | Directo | Lejos del parlante y del ventilador para evitar eco y ruido |
| Parlante USB | USB 2.0 | Directo | |
| PCB de botones | USB 3.0 | micro-USB → USB-A en ángulo | Detalle de los pines: sección 5.4 del [plan](../plan.md) |

## Pendientes de verificar al recibir los componentes

- [ ] El HAT de batería mantiene 3A con el LLM a carga máxima + USB conectados
- [ ] El HAT de batería deja libres los pines 5V/GND para el ventilador
- [ ] Modelo exacto de la pantalla y su conexión (DSI o HDMI, táctil por USB, I2C o DSI)
- [ ] Si el táctil usa USB: decidir hub o cambio de pantalla (faltaría un puerto)
- [ ] Largo necesario de cada cable dentro de la carcasa
- [ ] Fotos del cableado real en `docs/img/` (`conexiones-v1.jpg`)
