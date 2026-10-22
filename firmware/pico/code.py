import board
import digitalio
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Mismo orden que docs/contratos.md §1
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
