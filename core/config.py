import os

# Nombre de la app
APP_NAME = "HackFlow by Megalo04"

# Version actual
VERSION = "0.1.0"

# Paths importantes 
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# Comandos comunes para instalar paquetes 
PACKAGE_MANAGERS = {
    "termux": "pkg",
    "ubuntu": "apt-get",
    "kali": "apt-get",
}

# Lista base de dependencias comunes a instalar en cada entorno
BASE_DEPENDENCIES = [
    "nmap",
    "masscan",
    "python3",
    "python3-pip",
]

# Mensajes de ética y avisos 
ETHICS_MESSAGE = """
[!] Recuerda siempre usar HackFlow con fines éticos y legales.
El hacking ético protege sistemas, nunca los vulnera sin permiso.
"""

# Timeout para conexiones o comandos (segundos)
COMMAND_TIMEOUT = 30

# Colores o estilos globales 
COLORS = {
    "info": "cyan",
    "warning": "yellow",
    "error": "red",
    "success": "green",
}

# Otros parámetros globales ...

