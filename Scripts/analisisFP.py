import os
import re

# Definimos solo los archivos que realmente contienen alertas
rulesets = {
    "RS2": "RS2_alert",
    "RS3": "RS3_alert",
    "RS4": "RS4_alert"
}

output_lines = [
    "#RS1#",
    "0 alertas",
    "-\n"
]

for rs, filename in rulesets.items():
    alert_count = 0
    sid_set = set()

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                # Extraer el SID con formato típico: [1:2092:1]
                match = re.search(r'\[\d+:(\d+):\d+\]', line)
                if match:
                    alert_count += 1
                    sid_set.add(match.group(1))
    else:
        print(f"Archivo {filename} no encontrado.")

    output_lines.append(f"#{rs}#")
    output_lines.append(f"{alert_count} alertas")
    output_lines.append(f"SIDs: {', '.join(sorted(sid_set)) if sid_set else '-'}\n")

# Escribimos el resultado en un archivo
with open("resumen_alertas.txt", "w") as out_file:
    out_file.write('\n'.join(output_lines))

print("Resumen generado en 'resumen_alertas.txt'")
