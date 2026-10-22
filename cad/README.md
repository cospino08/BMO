# cad/ — Carcasa 3D

> Responsable: **Diseñador 3D**. Medidas de entrada: [`docs/hardware/medidas.md`](../docs/hardware/medidas.md). Tapas de los botones: sección 5.6 del [plan](../docs/plan.md).

## Estructura a llenar

```
cad/
├── README.md
├── fuentes/                       ← archivos editables (la fuente de verdad)
│   ├── carcasa.FCStd              ← modelo funcional paramétrico (FreeCAD) o enlace a Onshape en ENLACES.md
│   ├── estetica.blend             ← detalles en Blender: brazos, piernas, texturas
│   └── ENLACES.md                 ← enlaces a modelos en la nube (Onshape/Fusion), si se usan
├── stl/                           ← lo que se imprime
│   └── vX.Y/
│       ├── frontal.stl
│       ├── trasera.stl
│       ├── base.stl
│       ├── tapa_bateria.stl
│       ├── soporte_pi.stl
│       ├── soporte_pantalla.stl
│       ├── soporte_camara.stl
│       ├── boton_cruceta.stl
│       ├── boton_a.stl
│       ├── boton_b.stl
│       ├── boton_triangulo.stl
│       ├── boton_start_select.stl
│       ├── brazo_izq.stl / brazo_der.stl
│       ├── pierna_izq.stl / pierna_der.stl
│       └── IMPRESION.md           ← parámetros por pieza (ver abajo)
├── step/                          ← intercambio con el resto del equipo
│   └── vX.Y/carcasa_ensamblada.step
├── referencias/                   ← lo que se recibe o entrega a otras áreas
│   ├── frontal_vX.Y.dxf           ← contorno del frontal + agujeros de botones → para pcb/
│   ├── pcb_controles_vX.Y.step    ← recibido de pcb/fabricacion/
│   └── componentes/               ← STEP de los fabricantes (Pi 5, pantalla, cámara)
└── fotos/                         ← impresiones de prueba, problemas de encaje, acabado final
```

## IMPRESION.md (uno por versión)

| Pieza | Material | Capa (mm) | Relleno (%) | Soportes | Orientación | Tiempo | Filamento (g) | Notas |
|---|---|---|---|---|---|---|---|---|
| frontal.stl | | | | | | | | |

## Reglas

- **Unidades: mm.** Origen y ejes según [`medidas.md`](../docs/hardware/medidas.md).
- **Tolerancia** de encaje 0.2–0.3 mm por lado, a confirmar con una pieza de prueba y anotar aquí.
- Todo lo que encaja con un componente se modela con su **medida real** o el STEP del fabricante, nunca a ojo.
- Cada versión impresa se marca con un tag de git: `cad-v1.0`. Las versiones de STL no se sobrescriben.
- Los archivos fuente siempre se suben junto con sus STL exportados.
- Fotos de cada impresión de prueba en `fotos/` con nombre `vX.Y_pieza_descripcion.jpg`.

## Checklist

- [ ] S1–2: Bocetos y proporciones (en `fotos/` o `docs/img/`)
- [ ] S2: `referencias/frontal_v0.1.dxf` → entregado a Hardware
- [ ] S3: v1 + impresión de prueba de los soportes de pantalla y Pi
- [ ] S4–5: v2 con las medidas reales y el STEP de la PCB + impresión de prueba completa
- [ ] S5: Prueba térmica con la carcasa de prueba (con Hardware)
- [ ] S6: Impresión final + `IMPRESION.md`
- [ ] S7: Acabado (lijado, masilla, imprimación, pintura, barniz) con fotos
- [ ] S8: Ensamblaje → completar [`ensamblaje.md`](../docs/hardware/ensamblaje.md)
