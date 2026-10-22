# Contratos entre áreas

> **Fuente de verdad.** Lo que está aquí es lo que cada área promete entregar y lo que puede esperar de las demás. Para cambiarlo: PR aprobado por **todas** las áreas afectadas (ver [CONTRIBUTING.md](../CONTRIBUTING.md)).
>
> Versión: **v0.2** (propuesta, semana 1). Cambios v0.2: Raspberry Pi 4 y sin visión ([ADR 0003](decisiones/0003-raspberry-pi-4-sin-vision.md)).

## 1. Botones → Software (teclado USB)

Responsable: Hardware (firmware). Consume: Líder (UI).

| Botón | GPIO Pico | Tecla enviada | Evento en BMO | Acción |
|---|---|---|---|---|
| Cruceta ↑ | GP2 | `↑` | `TECLA_ARRIBA` | Navegar / mover la mirada |
| Cruceta ↓ | GP3 | `↓` | `TECLA_ABAJO` | Navegar / mover la mirada |
| Cruceta ← | GP4 | `←` | `TECLA_IZQ` | Navegar / bajar volumen |
| Cruceta → | GP5 | `→` | `TECLA_DER` | Navegar / subir volumen |
| A (rojo) | GP6 | `Enter` | `TECLA_A` | Hablar sin wake word / confirmar |
| B (verde) | GP7 | `Esc` | `TECLA_B` | Cancelar / callar a BMO |
| Triángulo | GP8 | `F1` | `TECLA_REPETIR` | Repetir la última respuesta |
| Start | GP9 | `F2` | `TECLA_MENU` | Abrir menú |
| Select | GP10 | `F3` | `TECLA_MODO` | Cambiar modo |

- Una pulsación = **una** tecla presionada y soltada. El firmware filtra el rebote (≥ 20 ms).
- Mantener presionado **no repite** la tecla. Si la UI necesita repetición, la implementa ella.

## 2. Módulos de IA → Agente (Python)

Responsable: IA. Consume: Líder (agente). Todos los módulos están en `software/bmo/`.

```python
# voz/wake.py
class DetectorWake:
    def __init__(self, config: dict, cola_eventos: Queue): ...
    def iniciar(self) -> None          # empieza a escuchar en su hilo; publica Evento("WAKE")
    def pausar(self) -> None           # mientras BMO habla
    def reanudar(self) -> None

# voz/stt.py
def escuchar(max_segundos: float = 15.0) -> str
    # graba desde el búfer hasta el silencio y transcribe; "" si no se oyó nada

# llm.py
def pensar(texto: str, historial: list[dict], herramientas: list[dict]) -> Iterator[Parte]
    # Parte = PideHerramienta(nombre, argumentos) | Frase(texto) | Fin()
    # entrega frases completas, nunca medias palabras

# voz/tts.py
def hablar(frase: str) -> None         # encola; no bloquea
def detener_habla() -> None            # vacía la cola y corta el audio en < 200 ms
def esta_hablando() -> bool
```

> Sin visión por ahora ([ADR 0003](decisiones/0003-raspberry-pi-4-sin-vision.md)).

**Reglas para todos los módulos:**
- Leen su configuración de `config.yaml` y nunca usan valores fijos en el código.
- **Nunca lanzan excepciones hacia el agente:** ante un error registran el log y devuelven un valor vacío o lanzan `ErrorBMO` con un mensaje para mostrar.
- Cada uno tiene una versión simulada en `software/tests/simulados/` con la misma firma.

## 3. Eventos

Responsable: Líder. Todo lo que pasa en BMO es un `Evento(tipo: str, datos: dict | None)` en la cola de eventos.

| Evento | Lo publica | Datos |
|---|---|---|
| `WAKE` | Audio | — |
| `TECLA_*` | UI | — |
| `TEXTO_LISTO` | Agente (tras `escuchar`) | `{"texto": str}` |
| `SILENCIO_TIMEOUT` | Agente | — |
| `FRASE` | Agente | `{"texto": str}` |
| `FIN_HABLA` | Voz | — |
| `ERROR` | Cualquiera | `{"mensaje": str}` |
| `estado_cambiado` | Agente → UI | `{"estado": str}` |

Estados válidos: `INACTIVO`, `ESCUCHANDO`, `PENSANDO`, `HABLANDO`, `ERROR`.

## 4. Configuración

Archivo `software/config.yaml`. Cada clave nueva se agrega aquí y en `config.example.yaml`.

```yaml
general:
  idioma: es
  nivel_log: INFO
audio:
  microfono: "default"        # nombre según `arecord -l`
  parlante: "default"         # nombre según `aplay -l`
  volumen: 70                 # 0–100
wake:
  modelo: ia/wakeword/hey_bmo.onnx
  umbral: 0.5
vad:
  silencio_fin_s: 0.8
  max_grabacion_s: 15
stt:
  motor: whisper.cpp          # o faster-whisper
  modelo: tiny
llm:
  url: http://localhost:11434
  modelo: gemma3:1b           # o gemma3:270m según el benchmark
  prompt_sistema: ia/prompts/sistema.md
  max_herramientas_por_turno: 1
  turnos_historial: 4
  frase_espera: true          # "Mmm, déjame pensar…" al entrar en PENSANDO
tts:
  voz: es_ES-...              # nombre del modelo de Piper
  velocidad: 1.0
ui:
  pantalla_completa: true
  fps: 30
herramientas:
  buscar_web: false           # true solo si hay internet
```

## 5. Hardware → Diseño 3D

Responsable: Hardware. Consume: 3D.

- [`hardware/medidas.md`](hardware/medidas.md) con versión. Un componente sin medida real no se modela como definitivo.
- STEP de la PCB en `pcb/fabricacion/vX.Y/`.
- Cualquier cambio de componente se avisa en la reunión semanal y sube la versión del plano.

## 6. Diseño 3D → Hardware

Responsable: 3D. Consume: Hardware.

- DXF del contorno del frontal con los agujeros de los botones en `cad/referencias/frontal_vX.Y.dxf`, a escala 1:1 en mm, con el origen en la esquina inferior izquierda de la PCB.
- Posición y diámetro de los postes de montaje de la PCB (M2.5).
