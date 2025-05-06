import re
import pandas as pd
import os

def contar_sids(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        contenido = f.read()

    # Buscar coincidencias del patrón [1:1390:17] => extrae 1390
    sids = re.findall(r'\[\d+:(\d+):\d+\]', contenido)

    # Contar ocurrencias
    contador = {}
    for sid in sids:
        sid_int = int(sid)
        contador[sid_int] = contador.get(sid_int, 0) + 1

    # Ordenar por SID
    sids_ordenados = sorted(contador.items())

    # Imprimir por pantalla
    print(f"\nRecuento de SIDs en: {ruta_archivo} ({len(sids_ordenados)} únicos):")
    for sid, cantidad in sids_ordenados:
        print(f"SID: {sid} -> {cantidad} veces")

    # Obtener ruta del directorio del archivo de entrada
    directorio_salida = os.path.dirname(os.path.abspath(ruta_archivo))
    nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]
    ruta_salida = os.path.join(directorio_salida, f"recuento_{nombre_base}.xlsx")

    # Guardar en Excel
    df = pd.DataFrame(sids_ordenados, columns=["SID", "Cantidad"])
    df.to_excel(ruta_salida, index=False)
    print(f"Resultado guardado en: {ruta_salida}")

# --- Procesar varios archivos ---

archivos = [
    "logs/smtp/RS1/smtp-RS1-logs.txt",
    "logs/smtp/RS2/smtp-RS2-logs.txt",
    "logs/smtp/RS3/smtp-RS3-logs.txt",
    "logs/smtp/RS4/smtp-RS4-logs.txt"
]

for archivo in archivos:
    contar_sids(archivo)
