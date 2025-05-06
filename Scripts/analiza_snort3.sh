#!/bin/bash

# Verificación de argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <ruta_al_pcapng> <ruta_salida_alertas>"
    exit 1
fi

PCAP_FILE="$1"
OUTPUT_DIR="$2"

# Verifica que el archivo pcapng existe
if [ ! -f "$PCAP_FILE" ]; then
    echo "Error: el archivo '$PCAP_FILE' no existe."
    exit 2
fi

# Crea el directorio de salida si no existe
mkdir -p "$OUTPUT_DIR"

# Ejecuta Snort con el archivo pcapng y guarda alertas en el directorio especificado
sudo snort -c /usr/local/etc/snort/snort.lua -r "$PCAP_FILE" -A alert_fast -l "$OUTPUT_DIR"

# Confirmación final
if [ -f "$OUTPUT_DIR/alert.fast" ]; then
    echo "✅ Análisis completado. Archivo generado en: $OUTPUT_DIR/alert.fast"
else
    echo "⚠️ No se generó el archivo de alertas. Verifica la configuración de Snort o el archivo pcap."
    exit 3
fi

