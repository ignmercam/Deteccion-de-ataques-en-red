#!/bin/bash

# Creamos carpeta para salidas combinadas
mkdir -p fusionados

# Listamos todos los archivos y agrupamos manualmente por prefijo
ls -1 | while read -r archivo; do
    # Extraemos el prefijo (por ejemplo: "01", "02", etc.)
    prefijo=$(echo "$archivo" | cut -c1-2)

    # Solo procesamos si el prefijo es numérico entre 01 y 07 y termina en .pcapng
    if [[ "$prefijo" =~ ^0[1-7]$ && "$archivo" == *.pcapng ]]; then
        echo "$archivo" >> "grupo_$prefijo.txt"
    fi
done

# Fusionamos por grupo
tr -d '\r' < grupo_01.txt | xargs -d '\n' mergecap -w 01_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_02.txt | xargs -d '\n' mergecap -w 02_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_03.txt | xargs -d '\n' mergecap -w 03_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_04.txt | xargs -d '\n' mergecap -w 04_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_05.txt | xargs -d '\n' mergecap -w 05_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_06.txt | xargs -d '\n' mergecap -w 06_DIT_COMBINADO.pcapng
tr -d '\r' < grupo_07.txt | xargs -d '\n' mergecap -w 07_DIT_COMBINADO.pcapng

done
