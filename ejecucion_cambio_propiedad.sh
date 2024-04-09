#!/bin/bash

# Verifica si se proporciona un archivo como argumento
if [ $# -ne 1 ]; then
  echo "Uso: $0 <archivo>"
  exit 1
fi

# Verifica si el archivo existe
if [ ! -f "$1" ]; then
  echo "El archivo $1 no existe."
  exit 1
fi

# Permite la ejecución del archivo
chmod +x "$1"

# Cambia la propiedad del archivo a root
sudo chown root "$1"

echo "Se ha permitido la ejecución del archivo $1 y se ha cambiado su propiedad a root."
