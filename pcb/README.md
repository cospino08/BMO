# pcb/ — PCB de controles (KiCad)

> Responsable: **Ingeniero de Hardware**. Paso a paso, componentes y conexiones: **sección 5 del [plan](../docs/plan.md)**. Mapa de pines: [contratos §1](../docs/contratos.md#1-botones--software-teclado-usb).

## Estructura a llenar

```
pcb/
├── README.md
├── kicad/
│   ├── bmo_controles.kicad_pro     ← proyecto KiCad (8 o superior)
│   ├── bmo_controles.kicad_sch     ← esquemático
│   ├── bmo_controles.kicad_pcb     ← diseño de la placa
│   ├── sym-lib-table / fp-lib-table← tablas de librerías del proyecto (rutas relativas a ../librerias)
│   └── frontal.dxf                 ← copia del DXF del frontal usado (de cad/referencias/)
├── librerias/
│   ├── bmo.kicad_sym               ← símbolos propios (si se crean)
│   ├── bmo.pretty/                 ← huellas propias (si se crean)
│   └── RPi_Pico/                   ← librería oficial de la Pico (submódulo o copia con su licencia)
└── fabricacion/
    └── v1.0/
        ├── bmo_controles_v1.0_gerbers.zip   ← lo que se envía al fabricante
        ├── bmo_controles_v1.0.step          ← modelo 3D para cad/
        ├── bmo_controles_v1.0_esquema.pdf   ← esquemático en PDF para revisar sin KiCad
        ├── bom.csv                          ← lista de componentes exportada desde KiCad
        ├── capturas/                        ← vista 3D frente/dorso, visor de Gerber
        └── NOTAS.md                         ← fabricante, opciones, fecha de pedido, costo, problemas encontrados
```

## Reglas

- **Rutas relativas** en las tablas de librerías: el proyecto debe abrir igual en cualquier computador.
- **Nunca** se modifica una carpeta `fabricacion/vX.Y/` ya pedida. Los cambios van en una versión nueva.
- Cada versión pedida se marca con un tag de git: `pcb-v1.0`.
- El PDF del esquemático se regenera en cada versión (*Archivo → Trazar → PDF*) para que el resto del equipo lo revise.
- La versión aparece en la serigrafía de la placa (`BMO CTRL v1.0`).

## Revisión antes de pedir (otra persona del equipo)

- [ ] ERC sin errores
- [ ] DRC sin errores, con las reglas del fabricante configuradas
- [ ] Cada botón conectado al GPIO de la tabla 5.4 del plan
- [ ] Orientación de los pulsadores verificada (el par de patas correcto)
- [ ] Posición de los botones coincide con el DXF del frontal
- [ ] Agujeros de montaje coinciden con los postes de la carcasa
- [ ] El conector USB de la Pico apunta hacia la Pi y hay espacio para el cable
- [ ] Gerbers revisados en el visor
- [ ] STEP entregado al 3D y probado en el modelo de la carcasa

## Checklist

- [ ] S3: Protoboard funcionando (ver `firmware/`)
- [ ] S4: Esquemático + PCB + revisión → `fabricacion/v1.0/` → pedido
- [ ] S5: STEP entregado a `cad/referencias/`
- [ ] S6–7: Placa recibida, soldada y probada; problemas anotados en `NOTAS.md`
