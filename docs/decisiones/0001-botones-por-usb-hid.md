# 0001. Botones mediante Raspberry Pi Pico como teclado USB

- **Estado:** Propuesta
- **Fecha:** 2026-10-22
- **Autor/a:** Equipo (desde el plan inicial)
- **Áreas afectadas:** Hardware, Software, 3D

## Contexto

BMO necesita 9 botones físicos (cruceta, A, B, Triángulo, Start, Select). Los pines GPIO de la Pi 4 pueden quedar tapados por el HAT de batería y el ventilador, y la PCB debe poder probarse sin la Pi.

## Opciones consideradas

| Opción | A favor | En contra |
|---|---|---|
| A. Botones directo a los GPIO de la Pi 4 | Sin microcontrolador; más barato | Los GPIO pueden estar ocupados por los HATs; el software tiene que leer GPIO; no se puede probar en un PC |
| B. Pico como teclado USB (HID) | Se prueba en cualquier PC; no requiere drivers; el software solo lee teclas; independiente de los HATs | Un componente más; ocupa un puerto USB |

## Decisión

Opción **B**: una Raspberry Pi Pico con CircuitPython (`usb_hid` + `keypad`) en una PCB propia.

## Evidencia

Pendiente: prueba en protoboard en la semana 3 (paso 1 de la sección 5 del plan).

## Consecuencias

- El mapa de teclas queda fijo en [`contratos.md §1`](../contratos.md#1-botones--software-teclado-usb).
- La UI (Pygame) recibe los botones como eventos de teclado normales.
- Hay que reservar un puerto USB y espacio para el cable en la carcasa.
