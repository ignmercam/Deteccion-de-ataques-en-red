#!/bin/bash

# Verificar argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 archivo.pcapng carpeta_salida/"
    exit 1
fi

PCAPNG=$1
SALIDA=$2

# Obtener nombre base sin extensión
BASENAME=$(basename "$PCAPNG" .pcapng)
PCAP="/tmp/${BASENAME}.pcap"

# Convertir pcapng a pcap
echo "[+] Convirtiendo $PCAPNG a formato pcap..."
editcap -F pcap "$PCAPNG" "$PCAP"

# Ejecutar snort con el archivo convertido
echo "[+] Ejecutando Snort sobre $PCAP..."
sudo snort -c /etc/snort/snort.conf -r "$PCAP" -l "$SALIDA" -A fast

# Mensaje final
echo "[+] Análisis completado. Resultados guardados en $SALIDA"
