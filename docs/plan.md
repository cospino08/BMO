# 🤖 Plan de Proyecto: Agente IA Embodied (BMO Local)

> Asistente de IA local con cuerpo físico estilo BMO, basado en Raspberry Pi 5 con modelos locales de lenguaje, visión y voz, y controles físicos propios. Todo funciona **sin conexión a internet**; la búsqueda web es un extra opcional.
>
> Referencia: video "I made a real BMO local AI agent with a Raspberry Pi and Ollama" (brenpoly).
>
> **Documentos vivos:** las interfaces entre áreas se mantienen en [contratos.md](contratos.md), la arquitectura en [arquitectura.md](arquitectura.md), la lista de materiales en [hardware/bom.md](hardware/bom.md) y el firmware en [`firmware/pico/code.py`](../firmware/pico/code.py). Si este plan y esos archivos difieren, mandan esos archivos.

---

## Índice

1. [Objetivo y criterios de éxito](#1-objetivo-y-criterios-de-éxito)
2. [Correcciones técnicas al plan original](#2-correcciones-técnicas-al-plan-original)
3. [Plan por miembro del equipo](#3-plan-por-miembro-del-equipo)
4. [Contratos entre áreas](#4-contratos-entre-áreas)
5. [Plan detallado de la PCB de controles](#5-plan-detallado-de-la-pcb-de-controles)
6. [Materiales y presupuesto](#6-materiales-y-presupuesto)
7. [Cronograma general](#7-cronograma-general)
8. [Riesgos](#8-riesgos)

---

## 1. Objetivo y criterios de éxito

Construir un BMO que **escuche, piense, vea y hable** en local, con cara animada en pantalla y botones físicos funcionales.

El proyecto se considera terminado cuando BMO:

- [ ] Arranca solo al encender y muestra su cara.
- [ ] Se activa con "Hey BMO" (menos de 1 activación falsa por hora).
- [ ] Empieza a responder en **menos de 4 s** después de que el usuario termina de hablar.
- [ ] Describe lo que ve con la cámara cuando se le pide.
- [ ] Funciona con el cable de red desconectado.
- [ ] Dura más de 1 hora con batería sin que la Pi baje su velocidad por temperatura o energía.
- [ ] Todos los botones responden.

---

## 2. Correcciones técnicas al plan original

| Tema | Problema | Solución |
|---|---|---|
| Cámara / pantalla | La Pi 5 usa conectores MIPI de 22 pines, no de 15 | Comprar cables adaptadores 22→15. Se recomienda la Camera Module 3 |
| NVMe + batería | El HAT M.2 y el HAT de batería pueden chocar entre sí. La Pi 5 necesita 5V/5A | Verificar que sean compatibles **antes de comprar**. Probar `vcgencmd get_throttled` |
| Calor | El LLM a carga máxima en una carcasa cerrada hace que la Pi baje su velocidad | Active Cooler obligatorio y ventilación diseñada en la carcasa |
| "Sin nube" | DuckDuckGo necesita internet | Búsqueda web como herramienta opcional que falla sin romper nada. RAG = documentos locales |
| Visión | Moondream puede sobrar | Comparar contra `gemma3:4b`, que ya acepta imágenes |
| CAD | Blender no maneja bien medidas y tolerancias | Piezas funcionales en FreeCAD/Onshape/Fusion; estética en Blender |
| Cronograma | El software empezaba en la semana 6 | El software arranca en la semana 1, en paralelo |
| Roles | Faltaban responsables de la cara animada y del audio | Cara: Líder. Audio: Desarrollador de IA |

---

## 3. Plan por miembro del equipo

### 3.1 Líder de Proyecto / Arquitecto de Software

**Misión:** que todas las piezas funcionen juntas como un solo BMO y que el proyecto llegue a tiempo.

**Responsabilidades**
- Máquina de estados: `INACTIVO → ESCUCHANDO → PENSANDO → HABLANDO → INACTIVO`, más `MIRANDO` (cámara) y `ERROR`. Permitir interrumpir a BMO mientras habla.
- Repositorio Git, estructura del proyecto en Python, `config.yaml` y logs.
- Sistema de herramientas: el LLM elige la herramienta respondiendo en JSON estructurado (parámetro `format` con esquema en Ollama). Herramientas: `ver_camara`, `consultar_notas`, `hora_fecha` y `buscar_web` (opcional).
- Cara de BMO en pantalla (Pygame o Chromium en modo kiosko) con una expresión por estado.
- Seguimiento semanal: tablero de tareas, riesgos, presupuesto y reunión corta.

**Tareas**
- [ ] S1: Documento de arquitectura y contratos entre módulos (sección 4)
- [ ] S1: Crear repositorio y tablero de tareas
- [ ] S2: Bucle de estados en PC con módulos simulados (entrada y salida por texto)
- [ ] S3: Cara de BMO con 5 expresiones
- [ ] S4: Sistema de herramientas con 2 herramientas funcionando
- [ ] S5–6: Integración con los módulos reales de IA en la Pi (banco de pruebas)
- [ ] S6: Leer los botones (teclas) desde el bucle principal
- [ ] S7: Inicio automático con `systemd` y reinicio automático si falla
- [ ] S8–9: Prueba de 1 hora sin cuelgues y demo final

**Recibe:** módulos de IA y mapa de teclas (Hardware). **Entrega:** contratos, bucle principal y UI.

---

### 3.2 Ingeniero de Hardware y Electrónica

**Misión:** que la energía, el audio, la cámara, la pantalla y los botones funcionen de forma confiable dentro de la carcasa.

**Responsabilidades**
- Verificar la compatibilidad de los componentes antes de comprar.
- Banco de pruebas: Raspberry Pi OS de 64 bits, arranque desde NVMe y acceso por SSH para el equipo.
- Pruebas de energía y temperatura con el LLM a carga máxima (`vcgencmd measure_temp`, `vcgencmd get_throttled`).
- PCB de controles completa. Ver la **sección 5**.
- Plano de medidas reales para el Diseñador 3D.

**Tareas**
- [ ] S1: Lista de materiales con enlaces, revisión de compatibilidad y compra
- [ ] S2: Banco de pruebas funcionando con NVMe y SSH
- [ ] S2: Informe de autonomía de batería y temperatura (10 min a carga máxima)
- [ ] S3: Botones en protoboard enviando teclas por USB (pasos 1–2 de la sección 5)
- [ ] S4: PCB diseñada, revisada y **pedida** (pasos 3–9)
- [ ] S5: Plano de medidas entregado a 3D, más el STEP de la PCB
- [ ] S6–7: PCB soldada y probada (pasos 10–12)
- [ ] S8: Montaje en la carcasa junto al Diseñador 3D

**Recibe:** espacio disponible en la carcasa (3D). **Entrega:** mapa de teclas (Líder), Pi por SSH (IA), medidas y STEP (3D).

---

### 3.3 Diseñador 3D y Modelador

**Misión:** una carcasa fiel a BMO que ventile bien, sea fácil de abrir y tenga buen acabado.

**Responsabilidades**
- Modelo funcional en CAD paramétrico: soportes para Pi, pantalla, cámara, parlante, micrófono, PCB y batería. Insertos roscados M2.5. Acceso al USB-C y a la NVMe.
- Modelo estético en Blender: brazos y piernas con imanes, rejillas y detalles.
- Flujo de aire: entrada abajo y salida arriba, alineada con el Active Cooler.
- Impresiones de prueba de las piezas críticas. Tolerancia de encaje ≈0.2–0.3 mm.
- Acabado: lijado (de grano 120 a 400), masilla, imprimación, pintura turquesa y barniz.
- Diseñar las **tapas de los botones** (cruceta, botón rojo, triángulo, botón verde) según la sección 5.6.

**Tareas**
- [ ] S1–2: Bocetos, proporciones y medidas provisionales tomadas de las fichas técnicas
- [ ] S2: Exportar el **contorno del frontal en DXF** para el Ingeniero de Hardware (paso 5 de la PCB)
- [ ] S3: Modelo v1 e impresión de prueba de los soportes de pantalla y Pi
- [ ] S4–5: Modelo v2 con las medidas reales y el STEP de la PCB, más impresión de prueba completa
- [ ] S5: Prueba de temperatura dentro de la carcasa de prueba
- [ ] S6: Impresión final
- [ ] S7: Post-procesado y pintura
- [ ] S8: Ensamblaje

**Recibe:** medidas y STEP de la PCB (Hardware). **Entrega:** STL/STEP versionados en el repositorio y la carcasa terminada.

---

### 3.4 Desarrollador de IA y Prompt Engineering

**Misión:** que BMO escuche, piense, vea y hable **rápido**, todo en la Pi.

**Responsabilidades**
- Comparar modelos **en la Pi 5**: `gemma3:1b` vs `gemma3:4b`, y Moondream vs Gemma 3 con imagen. Medir tokens por segundo, tiempo hasta la primera palabra y uso de RAM.
- Voz a texto: `faster-whisper` o `whisper.cpp` (modelos `tiny`/`base`). Detectar el fin de la frase con VAD (Silero).
- Palabra de activación: entrenar "Hey BMO" con openWakeWord usando voces sintéticas generadas con Piper.
- Texto a voz: Piper con una voz en español. Leer la respuesta **frase por frase mientras se genera**.
- Audio: volumen y eco. Evitar que BMO se escuche a sí mismo y se active solo.
- Personalidad: prompt de sistema de BMO, respuestas cortas y 20 preguntas de prueba.
- RAG local (opcional) con `nomic-embed-text`.

**Tareas**
- [ ] S1–2: Informe comparativo de modelos en la Pi
- [ ] S3: Palabra de activación entrenada y probada en ambiente real
- [ ] S4: Ciclo de voz completo: activación → transcripción → LLM → voz
- [ ] S5: Visión integrada como herramienta
- [ ] S6–7: Optimización (`keep_alive`, respuesta por partes) y ajuste de la personalidad
- [ ] S8–9: Pruebas con ruido, distintas voces y distancias

**Recibe:** Pi en el banco de pruebas (Hardware) y contratos (Líder). **Entrega:** `wake.py`, `stt.py`, `llm.py`, `tts.py`, `vision.py`.

---

## 4. Contratos entre áreas

> Resumen. La versión vigente y completa está en [contratos.md](contratos.md).

Se definen en la semana 1. Ninguna de estas interfaces se cambia sin avisar al resto del equipo.

**Botones → Software (teclado USB)**

| Botón | Tecla | Acción en BMO |
|---|---|---|
| Cruceta ↑ ↓ ← → | Flechas | Navegar menús / mover la cara |
| A (rojo grande) | `Enter` | Hablar (push-to-talk) / confirmar |
| B (verde) | `Esc` | Cancelar / interrumpir a BMO |
| Triángulo (azul) | `F1` | Tomar foto y describirla |
| Start | `F2` | Menú |
| Select | `F3` | Cambiar modo / volumen |

**Módulos de IA → Bucle principal (Python)**

```python
escuchar_activacion() -> None          # bloquea hasta oír "Hey BMO"
escuchar() -> str                      # graba hasta el silencio y devuelve el texto
pensar(texto, historial) -> Iterator[str]   # va entregando frases
hablar(frase: str) -> None
detener_habla() -> None
ver(pregunta: str) -> str              # foto + descripción
```

**Estados → UI:** evento `estado_cambiado(nuevo_estado)`. La cara traduce cada estado en una expresión.

**Hardware → 3D:** plano de medidas con número de versión, más el STEP de la PCB. Si cambia algo, se avisa al Diseñador 3D.

---

## 5. Plan detallado de la PCB de controles

### 5.1 Qué hace la PCB

Es una placa ubicada detrás del frontal de BMO, debajo de la pantalla. Lleva **9 pulsadores** y una **Raspberry Pi Pico** (microcontrolador RP2040). La Pico se conecta por USB a la Raspberry Pi 5 y se presenta como un **teclado USB**: cada botón envía una tecla. No necesita drivers.

```
 [Botón] ──► GPIO de la Pico ──► firmware (CircuitPython) ──► USB HID ──► Raspberry Pi 5 ──► software de BMO
```

**¿Por qué usar una Pico y no conectar los botones a los GPIO de la Pi?**
- La PCB se puede probar en cualquier PC.
- No ocupa los pines de la Pi, que pueden estar tapados por los HATs.
- El software solo lee teclas, lo que lo hace más simple y fácil de probar.

### 5.2 Diseño del frontal (vista desde adelante)

```
 ┌─────────────────────────────────────────────────┐
 │                 (pantalla arriba)               │
 ├─────────────────────────────────────────────────┤
 │      ┌───┐                                      │
 │      │ ↑ │                    ▲  (Triángulo)    │
 │  ┌───┼───┼───┐                                 │
 │  │ ← │   │ → │          ●  (B, verde)           │
 │  └───┼───┼───┘                                 │
 │      │ ↓ │                       ⬤  (A, rojo)   │
 │      └───┘                                      │
 │   ▬ Select   ▬ Start                     ○ LED  │
 └─────────────────────────────────────────────────┘
```

> La posición exacta sale del DXF del frontal entregado por el Diseñador 3D. **No se inventan coordenadas en KiCad.**

### 5.3 Lista de componentes (BOM de la PCB)

| Ref. | Cant. | Componente | Especificación | Huella KiCad (sugerida) |
|---|---|---|---|---|
| U1 | 1 | Raspberry Pi Pico (o Pico H) | RP2040, 3.3 V | Pico en 2 tiras 1x20, filas a 17.78 mm (0.7") |
| J1, J2 | 2 | Tira de pines **hembra** 1x20 | Paso 2.54 mm | `PinSocket_1x20_P2.54mm_Vertical` |
| SW1–SW4 | 4 | Pulsador táctil (cruceta) | 6x6 mm, THT, 4 pines | `SW_PUSH_6mm` |
| SW5 | 1 | Pulsador táctil grande (A) | 12x12 mm, THT, 4 pines | `SW_PUSH_12mm` |
| SW6–SW9 | 4 | Pulsador táctil (B, Triángulo, Start, Select) | 6x6 mm, THT, 4 pines | `SW_PUSH_6mm` |
| D1 | 1 | LED 3 mm (indicador) | Color a elección | `LED_D3.0mm` |
| R1 | 1 | Resistencia para el LED | 330 Ω, 1/4 W | `R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal` |
| H1–H4 | 4 | Agujeros de montaje | Para tornillo M2.5 | `MountingHole_2.7mm_M2.5` |
| — | 1 | Cable micro-USB → USB-A | Corto (15–20 cm), ideal en ángulo | — |
| — | 4 | Tornillos M2.5 + separadores | Según la carcasa | — |

**Notas sobre los componentes**
- **Altura de los pulsadores:** elegirla junto con el Diseñador 3D. La tapa impresa debe sobresalir del frontal unos 1–2 mm. Los 6x6 vienen en alturas de 4.3 a 13 mm.
- **Sin resistencias pull-up:** se usan las internas de la Pico.
- **Sin condensadores antirrebote:** el rebote se filtra en el firmware con `keypad`.
- **Pico en tiras hembra:** permite sacarla para reemplazarla o reprogramarla. Si falta espacio en profundidad, se puede soldar directo a la PCB.
- **Opción más compacta:** la **Waveshare RP2040-Zero**, con USB-C y menor tamaño. Tiene otra distribución de pines, así que hay que rehacer la tabla 5.4.
- **Herramientas:** soldador de 60 W con punta fina, estaño con flux, multímetro, pinzas y alcohol isopropílico.

### 5.4 Tabla de conexiones

Cada pulsador va **entre un GPIO y GND**. El GPIO tiene activada la resistencia pull-up interna: en reposo lee `1` y al presionar lee `0`.

| Botón | Ref. | Red (net) en KiCad | GPIO Pico | Pin físico Pico | Otro terminal |
|---|---|---|---|---|---|
| ↑ Arriba | SW1 | `BTN_UP` | GP2 | 4 | GND |
| ↓ Abajo | SW2 | `BTN_DOWN` | GP3 | 5 | GND |
| ← Izquierda | SW3 | `BTN_LEFT` | GP4 | 6 | GND |
| → Derecha | SW4 | `BTN_RIGHT` | GP5 | 7 | GND |
| A (rojo) | SW5 | `BTN_A` | GP6 | 9 | GND |
| B (verde) | SW6 | `BTN_B` | GP7 | 10 | GND |
| Triángulo | SW7 | `BTN_TRI` | GP8 | 11 | GND |
| Start | SW8 | `BTN_START` | GP9 | 12 | GND |
| Select | SW9 | `BTN_SELECT` | GP10 | 14 | GND |
| LED | D1 + R1 | `LED_STATUS` | GP15 | 20 | GP15 → R1 (330 Ω) → ánodo D1 (+, pata larga); cátodo D1 (−) → GND |

**Pines GND de la Pico:** 3, 8, 13, 18, 23, 28, 33 y 38. Conectarlos **todos** a la red `GND`.

**Pines que NO se conectan:** VBUS (40), VSYS (39), 3V3_EN (37), 3V3 (36) y RUN (30). La Pico se alimenta por su propio USB.

**Diagrama de conexión (se repite igual para cada botón)**

```
              Pico                          Pulsador 6x6 (4 patas)
          ┌──────────┐                      ┌─────────────┐
          │      GP2 ├──── BTN_UP ──────────┤ 1         2 │   1 y 2 están unidas por dentro
          │          │                      │    [ ● ]    │
          │      GND ├──── GND ─────────────┤ 3         4 │   3 y 4 están unidas por dentro
          └──────────┘                      └─────────────┘
       (pull-up interno)        Al presionar: el par 1-2 se conecta con el par 3-4
```

> ⚠️ **Orientación de los pulsadores de 4 patas:** antes de diseñar, verifica con el multímetro (modo continuidad) cuáles patas están unidas en tu modelo. Si giras el pulsador 90° en la PCB, el botón queda **siempre presionado**. La huella `SW_PUSH_6mm` de KiCad ya numera las patas correctamente; solo hay que respetar el símbolo.

### 5.5 Paso a paso

#### Paso 1 — Probar en protoboard (semana 3)
1. Instala CircuitPython en la Pico: mantén **BOOTSEL** apretado, conéctala al PC, suelta el botón y arrastra el archivo `.uf2` de circuitpython.org a la unidad `RPI-RP2`.
2. Copia la carpeta `adafruit_hid` (del *Adafruit CircuitPython Library Bundle*) a `CIRCUITPY/lib/`.
3. Arma en la protoboard **2 o 3 botones** según la tabla 5.4.
4. Copia el `code.py` de la sección 5.7 y comprueba que el PC recibe las teclas (por ejemplo, en un editor de texto).

✅ **Listo cuando:** cada botón escribe su tecla una sola vez por pulsación.

#### Paso 2 — Medir los componentes reales
1. Con un calibre, mide el pulsador 6x6, el de 12x12, el LED y la Pico.
2. Anota la altura total de cada pulsador y la profundidad disponible detrás del frontal.
3. Entrega estas medidas al Diseñador 3D.

#### Paso 3 — Crear el proyecto en KiCad
1. Usa KiCad 8 o superior. Crea el proyecto con *Archivo → Nuevo proyecto* → `bmo_controles`.
2. Para la Pico, usa uno de estos:
   - Símbolo y huella de la librería oficial de Raspberry Pi (*RP2040 / Pico KiCad library* en GitHub). Impórtala en *Preferencias → Administrar librerías de símbolos/huellas*.
   - O dos conectores `Conn_01x20` con la huella `PinSocket_1x20_P2.54mm_Vertical`, separados exactamente **17.78 mm**.

#### Paso 4 — Esquemático
1. Coloca los símbolos: Pico (U1), 9× `SW_Push` (SW1–SW9), `LED` (D1), `R` (R1), 4× `MountingHole` (H1–H4).
2. Haz las conexiones de la tabla 5.4. Usa **etiquetas de red** (`BTN_UP`, etc.) en lugar de cables largos; el esquema queda más limpio.
3. Usa el símbolo de poder `GND` en todos los pines GND de la Pico y en un terminal de cada pulsador.
4. Marca los pines sin uso con la **X de "no conectar"**.
5. Agrega *Herramientas → Anotar esquemático*.
6. Agrega notas de texto con el nombre de la tecla de cada botón.
7. Ejecuta el **ERC** (comprobación de reglas eléctricas) y corrige todos los errores.

#### Paso 5 — Asignar huellas y definir el contorno
1. Usa *Herramientas → Asignar huellas* según la tabla 5.3.
2. Actualiza la PCB desde el esquemático (`F8`).
3. Importa el **DXF del frontal** que entregó el Diseñador 3D en la capa `Edge.Cuts`: *Archivo → Importar → Gráficos*.
   - Si aún no existe, dibuja un rectángulo provisional de **95 x 45 mm**.
   - Apunta a **≤ 100 x 100 mm**: es el tamaño más barato en la mayoría de los fabricantes.
4. Esquinas redondeadas de radio 2 mm.

#### Paso 6 — Ubicar los componentes
1. **Pulsadores en la cara frontal (F.Cu)**, en la posición exacta de los agujeros del frontal según el DXF.
2. **Cruceta:** los 4 pulsadores en cruz, a **~9–10 mm del centro**. La tapa impresa en forma de cruz se balancea sobre un pivote central y aprieta uno a la vez.
3. **Pico en la cara trasera (B.Cu)**, con el **conector USB apuntando hacia donde está la Pi 5** y espacio para el cable.
4. LED en su agujero del frontal y R1 cerca del LED.
5. Agujeros de montaje en las 4 esquinas, a ≥ 3 mm del borde, coordinados con los postes de la carcasa.
6. Revisa la vista 3D (`Alt+3`) para detectar choques.

#### Paso 7 — Rutear
1. PCB de **2 capas**.
2. Ancho de pista de señal: **0.3 mm**. Hay muy poca corriente.
3. Rutea primero las señales `BTN_*` y `LED_STATUS`. Usa pistas lo más directas posible y codos de 45°.
4. Agrega un **relleno de cobre GND en ambas caras**: *Zona → red GND*. Une los GND de los pulsadores con vías (taladro de 0.4 mm).
5. Presiona `B` para recalcular las zonas.

#### Paso 8 — Revisión (DRC)
1. Configura las reglas del fabricante en *Configuración de placa*. Valores seguros:
   - Pista mínima de 0.15 mm y separación mínima de 0.15 mm.
   - Taladro mínimo de 0.3 mm y anillo mínimo de 0.15 mm.
2. Ejecuta el **DRC** hasta que no quede ningún error ni red sin conectar.
3. Agrega serigrafía:
   - Nombre de cada botón, ref. de cada componente y "+" del LED.
   - Nombre del proyecto y versión (`BMO CTRL v1.0`).
4. **Revisión cruzada:** otro miembro del equipo compara la PCB contra la tabla 5.4.

#### Paso 9 — Exportar y pedir (máximo en la semana 4)
1. Exporta el **STEP** de la PCB (*Archivo → Exportar → STEP*) y entrégalo al Diseñador 3D.
2. Para la fabricación, *Archivo → Fabricación → Gerbers*:
   - Capas: `F.Cu`, `B.Cu`, `F.Mask`, `B.Mask`, `F.Silkscreen`, `B.Silkscreen`, `Edge.Cuts`.
   - Genera también los **archivos de taladrado** (formato Excellon).
3. Comprime todo en un `.zip` y revísalo en el **Visor de Gerber** de KiCad o en el del fabricante.
4. Pídela a JLCPCB, PCBWay o similar:
   - 2 capas, 1.6 mm de grosor, terminación HASL sin plomo, 5 unidades (cantidad mínima habitual).
   - El color es libre; el verde es el más rápido.
5. El envío tarda **1 a 2 semanas**. Mientras tanto se sigue trabajando con la protoboard.

#### Paso 10 — Soldar (semana 6)
Suelda de **menor a mayor altura**:
1. R1 (la resistencia).
2. D1: la pata larga (+) va en el pad marcado "+". Déjalo a la altura del frontal.
3. Los pulsadores, todos bien a ras de la PCB para que queden alineados.
4. Las tiras hembra J1 y J2. Truco: insértalas en la Pico, ponla en la PCB y suelda; así quedan alineadas.
5. Inserta la Pico.

Limpia el flux con alcohol isopropílico.

#### Paso 11 — Probar
1. **Sin la Pico conectada,** mide con el multímetro:
   - Que no haya corto entre GND y las señales `BTN_*`.
   - Que haya continuidad en cada botón **solo al presionarlo**.
2. Conecta la Pico al PC: el LED debe encenderse al arrancar.
3. Presiona cada botón y verifica su tecla en un editor de texto.
4. En la Raspberry Pi: `sudo apt install evtest && sudo evtest`. Elige el dispositivo del teclado y verifica los eventos.

✅ **Listo cuando:** los 9 botones envían la tecla correcta, sin repeticiones y sin quedarse pegados.

#### Paso 12 — Integrar
1. Monta la PCB en la carcasa con separadores M2.5.
2. Conecta el cable USB a la Pi 5.
3. Confirma con el Líder que el software reacciona a cada tecla según la tabla de la sección 4.

### 5.6 Tapas de los botones (coordinar con 3D)

| Botón | Forma | Color | Nota |
|---|---|---|---|
| Cruceta | Cruz con pivote central | Amarillo | Debe tener un tope para no hundirse de más |
| A | Círculo grande (~14 mm) | Rojo | Sobre el pulsador de 12x12 |
| B | Círculo pequeño (~8 mm) | Verde | |
| Triángulo | Triángulo (~10 mm) | Azul | |
| Start / Select | Píldora alargada | Gris | Pueden ir hundidas para evitar pulsaciones accidentales |

Cada tapa lleva un **reborde** por dentro del frontal para que no se salga, y un vástago que apoya sobre el pulsador.

### 5.7 Firmware (`code.py` en la Pico, CircuitPython)

```python
import board
import digitalio
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Mismo orden que la tabla 5.4
PINES = (
    board.GP2,   # Arriba
    board.GP3,   # Abajo
    board.GP4,   # Izquierda
    board.GP5,   # Derecha
    board.GP6,   # A (rojo)
    board.GP7,   # B (verde)
    board.GP8,   # Triángulo
    board.GP9,   # Start
    board.GP10,  # Select
)

TECLAS = (
    Keycode.UP_ARROW,
    Keycode.DOWN_ARROW,
    Keycode.LEFT_ARROW,
    Keycode.RIGHT_ARROW,
    Keycode.ENTER,
    Keycode.ESCAPE,
    Keycode.F1,
    Keycode.F2,
    Keycode.F3,
)

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
led.value = True  # encendido = firmware funcionando

teclado = Keyboard(usb_hid.devices)
# pull=True activa los pull-up internos; keypad ya filtra el rebote
botones = keypad.Keys(PINES, value_when_pressed=False, pull=True)

while True:
    evento = botones.events.get()
    if evento:
        tecla = TECLAS[evento.key_number]
        if evento.pressed:
            teclado.press(tecla)
            led.value = False  # parpadeo al presionar
        else:
            teclado.release(tecla)
            led.value = True
```

### 5.8 Checklist de la PCB

- [ ] Botones en protoboard funcionando con el firmware
- [ ] Componentes medidos y medidas entregadas a 3D
- [ ] DXF del frontal recibido
- [ ] Esquemático completo y ERC sin errores
- [ ] PCB ubicada según el DXF, vista 3D revisada
- [ ] DRC sin errores, revisión cruzada hecha
- [ ] STEP entregado a 3D
- [ ] Gerbers revisados y PCB pedida
- [ ] PCB recibida, soldada y probada con multímetro
- [ ] Los 9 botones probados en la Pi con `evtest`
- [ ] Montada en la carcasa

---

## 6. Materiales y presupuesto

> Completar los precios al momento de comprar. Verificar la compatibilidad de la sección 2 **antes** de pagar.

| Categoría | Componente | Cant. | Precio unit. | Total | Responsable | Comprado |
|---|---|---|---|---|---|---|
| Cerebro | Raspberry Pi 5 16 GB | 1 | | | Hardware | [ ] |
| Cerebro | Active Cooler | 1 | | | Hardware | [ ] |
| Almacenamiento | HAT M.2 + SSD NVMe (≥256 GB) | 1 | | | Hardware | [ ] |
| Energía | HAT/UPS de batería compatible con 5V/5A | 1 | | | Hardware | [ ] |
| Energía | Fuente oficial 27 W USB-C | 1 | | | Hardware | [ ] |
| Pantalla | Pantalla táctil 5" 800x480 + cable para Pi 5 | 1 | | | Hardware | [ ] |
| Cámara | Camera Module 3 + cable 22→15 pines | 1 | | | Hardware | [ ] |
| Audio | Micrófono USB compacto | 1 | | | Hardware | [ ] |
| Audio | Parlante USB | 1 | | | Hardware | [ ] |
| Controles | Componentes de la sección 5.3 | 1 juego | | | Hardware | [ ] |
| Controles | Fabricación de la PCB (5 unid. + envío) | 1 | | | Hardware | [ ] |
| Carcasa | Filamento PLA/PETG | 1–2 kg | | | 3D | [ ] |
| Carcasa | Masilla, imprimación, pintura, barniz, lijas | 1 juego | | | 3D | [ ] |
| Carcasa | Insertos roscados M2.5, tornillos, imanes | 1 juego | | | 3D | [ ] |
| | | | | **Total:** | | |

**Software (gratuito):** Raspberry Pi OS 64 bits, Python, Ollama, Gemma 3, Moondream, faster-whisper / whisper.cpp, openWakeWord, Piper, KiCad, FreeCAD/Onshape, Blender.

---

## 7. Cronograma general

| Sem. | Líder / Software | Hardware y Electrónica | Diseño 3D | IA |
|---|---|---|---|---|
| 1 | Arquitectura, contratos, repositorio | Revisión de compatibilidad y compra | Bocetos y proporciones | Comparación de modelos en PC |
| 2 | Bucle de estados con módulos simulados | Banco de pruebas, energía y temperatura | Medidas provisionales y DXF del frontal | Comparación de modelos en la Pi |
| 3 | Cara de BMO | Botones en protoboard | Modelo v1 e impresión de prueba | Palabra de activación |
| 4 | Sistema de herramientas | **PCB diseñada y pedida** | Modelo v2 | Ciclo de voz completo |
| 5 | Integración en el banco de pruebas | Medidas finales y STEP | Impresión de prueba completa y prueba térmica | Visión |
| 6 | Integración completa | Soldar y probar la PCB | Impresión final | Optimización |
| 7 | `systemd` y robustez | Cableado interno | Pintura | Personalidad |
| 8 | Pruebas de punta a punta | **Ensamblaje (todo el equipo)** | **Ensamblaje** | Pruebas con ruido |
| 9 | Prueba de 1 h, corrección de errores, demo | Calibración | Retoques | Ajuste final |

---

## 8. Riesgos

| Riesgo | Prob. | Impacto | Mitigación | Responsable |
|---|---|---|---|---|
| El LLM es demasiado lento en la Pi | Media | Alto | Medir en la semana 2. Alternativas: `gemma3:1b`, respuestas cortas, respuesta por partes | IA |
| La batería no entrega 5A | Media | Alto | Probar en la semana 2. Alternativa: usarlo enchufado | Hardware |
| La PCB llega tarde o con errores | Baja | Medio | Pedirla en la semana 4, protoboard como respaldo, revisión cruzada | Hardware |
| Pulsadores girados en la PCB | Media | Medio | Verificar con multímetro y usar la huella oficial (5.4) | Hardware |
| Calentamiento dentro de la carcasa | Media | Alto | Prueba térmica con la impresión de prueba en la semana 5 | 3D + Hardware |
| Activaciones falsas o BMO se escucha a sí mismo | Media | Medio | Silenciar el micrófono mientras habla y ajustar el umbral | IA |
| Retrasos por dependencias entre áreas | Media | Medio | Contratos en la semana 1, revisión semanal | Líder |
