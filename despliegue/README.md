# despliegue/ — Instalación de BMO en la Raspberry Pi 5

> Responsables: **Hardware** (sistema operativo, NVMe, energía) y **Líder** (software y servicio). Objetivo: que una Pi nueva quede funcionando como BMO siguiendo **solo** esta guía.

## Estructura a llenar

```
despliegue/
├── README.md               ← esta guía (completar con los comandos reales probados)
├── instalar.sh             ← script que automatiza los pasos 3–6 (Líder, S7)
├── bmo.service             ← servicio systemd: arranca BMO al encender y lo reinicia si se cae
├── modelos.txt             ← modelos de Ollama, Whisper y Piper con su versión exacta
└── config.txt.extra        ← líneas agregadas a /boot/firmware/config.txt (PCIe, pantalla, cámara)
```

## Guía (borrador: verificar y completar cada comando en la Pi real)

### 1. Sistema operativo
- Raspberry Pi OS **64 bits** (Bookworm o posterior), instalado con Raspberry Pi Imager.
- En el Imager: usuario, Wi-Fi, SSH activado y nombre de equipo `bmo`.

### 2. Arranque desde NVMe
- Actualizar el bootloader (`sudo rpi-eeprom-update`).
- Activar PCIe en `config.txt` si el HAT lo requiere.
- Clonar el sistema a la NVMe y cambiar el orden de arranque (`raspi-config` → *Advanced* → *Boot Order*).
- Anotar aquí los comandos exactos usados.

### 3. Pantalla, cámara y audio
- Configurar la pantalla según el fabricante (ver [conexiones.md](../docs/hardware/conexiones.md)).
- Cámara: `rpicam-hello` debe mostrar imagen.
- Audio: `arecord -l` y `aplay -l` deben listar el micrófono y el parlante. Anotar los nombres en `config.yaml`.

### 4. Ollama y modelos
- Instalar Ollama con el instalador oficial para Linux ARM64.
- Descargar los modelos de `modelos.txt` (`ollama pull ...`).
- Verificar que `ollama run <modelo>` responde.

### 5. BMO
```bash
git clone https://github.com/cospino08/BMO.git
cd BMO/software
python -m venv .venv && source .venv/bin/activate
pip install -e .
cp config.example.yaml config.yaml   # y ajustar
```

### 6. Servicio
- Copiar `bmo.service` a `/etc/systemd/system/` y ejecutar `sudo systemctl enable --now bmo`.
- Logs: `journalctl -u bmo -f`.
- El servicio debe:
  - Iniciar después de `ollama.service` y de la sesión gráfica.
  - Reiniciarse si se cae (`Restart=on-failure`).

### 7. Verificación final
- [ ] `vcgencmd get_throttled` → `0x0` con todo conectado
- [ ] `sudo evtest` muestra el teclado de la Pico
- [ ] BMO arranca solo tras `sudo reboot`
- [ ] BMO funciona con el Wi-Fi apagado

## Checklist

- [ ] S2: Pasos 1–2 hechos y documentados (Hardware)
- [ ] S2: Paso 4 + `modelos.txt` (IA)
- [ ] S5: Pasos 3 y 5 documentados
- [ ] S7: `bmo.service` + `instalar.sh` probados en una instalación limpia
