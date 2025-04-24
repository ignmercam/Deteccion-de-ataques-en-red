import os
import re

# Ruta a la carpeta con archivos .rules
RULES_DIR = "rules"
# Ruta al archivo con SIDs a eliminar
FALSOS_POSITIVOS = "falsos_positivos.txt"

def cargar_sids(fichero):
    with open(fichero, "r") as f:
        return {line.strip() for line in f if line.strip().isdigit()}

def limpiar_reglas(carpeta, sids_fp):
    sid_pattern = re.compile(r"sid\s*:\s*(\d+)\s*;")
    archivos_modificados = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".rules"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, "r") as f:
                lineas = f.readlines()

            nuevas_lineas = []
            modificado = False
            for linea in lineas:
                match = sid_pattern.search(linea)
                if match and match.group(1) in sids_fp:
                    modificado = True
                    continue  # Eliminar línea con SID de falso positivo
                nuevas_lineas.append(linea)

            if modificado:
                with open(ruta_archivo, "w") as f:
                    f.writelines(nuevas_lineas)
                archivos_modificados.append(archivo)
                print(f"[MODIFICADO] {archivo}")
            else:
                print(f"[SIN CAMBIOS] {archivo}")

    # Resumen final
    print("\nResumen final:")
    if archivos_modificados:
        print("Archivos modificados:")
        for archivo in archivos_modificados:
            print(f" - {archivo}")
    else:
        print("No se modificó ningún archivo.")

if __name__ == "__main__":
    sids_a_eliminar = cargar_sids(FALSOS_POSITIVOS)
    limpiar_reglas(RULES_DIR, sids_a_eliminar)
