# Documentación

Índice de toda la documentación del proyecto. Si creas un documento nuevo, agrégalo aquí.

| Documento | Qué contiene | Responsable | Se actualiza |
|---|---|---|---|
| [plan.md](plan.md) | Objetivo, roles, tareas por semana, plan de la PCB, cronograma, riesgos | Líder | Cada semana (casillas de tareas) |
| [arquitectura.md](arquitectura.md) | Cómo está construido el software: procesos, hilos, estados, flujo de datos | Líder | Cuando cambie el diseño |
| [contratos.md](contratos.md) | Interfaces entre áreas: teclas, funciones de Python, eventos, configuración, medidas | Líder (aprueban todos) | Solo por PR aprobado por las áreas afectadas |
| [decisiones/](decisiones/README.md) | Registro de decisiones técnicas (ADR) | Quien toma la decisión | Una por decisión |
| [hardware/bom.md](hardware/bom.md) | Lista de materiales y presupuesto | Hardware | Al comprar |
| [hardware/conexiones.md](hardware/conexiones.md) | Qué se conecta a qué en la Pi 4 | Hardware | Al cambiar el cableado |
| [hardware/medidas.md](hardware/medidas.md) | Plano de medidas de los componentes para la carcasa | Hardware + 3D | Al medir o cambiar un componente |
| [hardware/ensamblaje.md](hardware/ensamblaje.md) | Guía de montaje paso a paso con fotos | 3D + Hardware | Semana 8 |
| [reuniones/](reuniones/README.md) | Actas semanales | Líder | Cada semana |
| `img/` | Diagramas y fotos de la documentación | Todos | — |

## Reglas

- Todo en **Markdown** y en **español**.
- **Un tema por documento.** Si algo ya está en otro archivo, se enlaza; no se copia.
- **Fuentes de verdad:** las interfaces viven en `contratos.md`; el código de la Pico, en `firmware/`. Si el plan y estos archivos difieren, mandan estos.
- **Imágenes** en `img/`, con nombre descriptivo (`flujo-estados.png`, `pcb-v1-frente.jpg`), enlazadas con ruta relativa.
- **Diagramas** en texto (ASCII o [Mermaid](https://mermaid.js.org/), que GitHub muestra directamente) para poder editarlos y ver los cambios en git.
