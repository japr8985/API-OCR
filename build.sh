#!/usr/bin/env bash

# Salir inmediatamente si un comando termina con un estado distinto de cero.
set -eo pipefail

# Instala Tesseract OCR y sus datos de idioma (si es necesario)
apt-get update -y
apt-get install -y tesseract-ocr
# Si necesitas los datos de idioma español, descomenta la línea de abajo:
# apt-get install -y tesseract-ocr-spa

# Instala las dependencias de Python
pip install -r requirements.txt