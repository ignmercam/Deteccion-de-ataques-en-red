import os


def fusionar_ficheros_en_directorio(directorio, nombre_salida="alertas_fusionadas.txt"):
    """
    Fusiona todos los archivos de un directorio en un solo archivo de salida.

    :param directorio: Ruta del directorio que contiene los archivos a fusionar.
    :param nombre_salida: Nombre del archivo de salida.
    """
    ruta_salida = os.path.join(directorio, nombre_salida)

    with open(ruta_salida, 'w') as fichero_salida:
        for nombre_fichero in sorted(os.listdir(directorio)):
            ruta_fichero = os.path.join(directorio, nombre_fichero)
            if os.path.isfile(ruta_fichero) and nombre_fichero != nombre_salida:
                with open(ruta_fichero, 'r') as f:
                    contenido = f.read()
                    fichero_salida.write(f"----- {nombre_fichero} -----\n")
                    fichero_salida.write(contenido)
                    fichero_salida.write("\n")

    print(f"Ficheros fusionados en: {ruta_salida}")


def main():
    # Cambia esta ruta por la que necesites
    directorio = "logs/smtp/RS4"
    nombre_salida = "smtp-RS4-logs.txt"

    fusionar_ficheros_en_directorio(directorio, nombre_salida)


if __name__ == "__main__":
    main()
