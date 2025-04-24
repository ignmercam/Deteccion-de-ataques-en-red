import re

def extraer_sids(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        contenido = f.read()

    # Buscar coincidencias del patrón SID [1:1390:17] => extrae 1390
    sids = re.findall(r'\[\d+:(\d+):\d+\]', contenido)

    # Eliminar duplicados y ordenar
    sids_unicos = sorted(set(map(int, sids)))

    # Convertir a string separados por coma
    resultado = ", ".join(map(str, sids_unicos))

    # Imprimir resultados
    print(f"SIDs encontrados ({len(sids_unicos)}):")
    print(resultado)

# Ejemplo de uso
archivo = "alert_fast.txt"
extraer_sids(archivo)
