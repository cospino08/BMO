# firmware/ — Raspberry Pi Pico (botones → teclado USB)

> Responsable: **Ingeniero de Hardware**. Decisión: [ADR 0001](../docs/decisiones/0001-botones-por-usb-hid.md). Mapa de teclas: [contratos §1](../docs/contratos.md#1-botones--software-teclado-usb).

**Fuente de verdad del firmware.** El código de la sección 5.7 del plan es una copia de referencia; si difieren, manda este.

## Estructura

```
firmware/
├── README.md
└── pico/
    ├── code.py        ← firmware principal (CircuitPython)
    ├── boot.py        ← (opcional) configurar USB, p. ej. ocultar la unidad CIRCUITPY en producción
    └── VERSION        ← versión de CircuitPython y de adafruit_hid usadas (crear al probar)
```

## Instalación

1. Con la Pico desconectada, mantén **BOOTSEL** apretado, conéctala por USB y suelta el botón. Aparece la unidad `RPI-RP2`.
2. Copia el `.uf2` de CircuitPython para *Raspberry Pi Pico* (descargar de circuitpython.org). La Pico se reinicia como `CIRCUITPY`.
3. Descarga el *Adafruit CircuitPython Library Bundle* de la **misma versión mayor** y copia la carpeta `adafruit_hid` a `CIRCUITPY/lib/`.
4. Copia `pico/code.py` a la raíz de `CIRCUITPY`.
5. Anota las versiones usadas en `pico/VERSION`.

## Prueba

- En un PC: abre un editor de texto y presiona cada botón.
- En la Pi: `sudo evtest` → elige el teclado de CircuitPython → cada botón debe generar `KEY_*` *press* y *release* una sola vez.

## Si se cambia un botón o un pin

1. Actualiza `PINES` y `TECLAS` en `code.py` (el **mismo orden** en ambas listas).
2. Actualiza [contratos §1](../docs/contratos.md#1-botones--software-teclado-usb) y la tabla 5.4 del plan, en el mismo PR.
3. Si cambia el pin físico, también cambia la PCB → nueva versión en `pcb/`.

## Checklist

- [x] `code.py` inicial
- [ ] Probado en protoboard (S3)
- [ ] `VERSION` completo
- [ ] Probado en la PCB v1 (S6–7)
- [ ] Probado en la Pi con `evtest`
