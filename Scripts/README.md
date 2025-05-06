# Scripts de Análisis de Alertas - TFG

Este directorio contiene varios scripts utilizados en el proyecto de detección de ataques en red para automatizar el análisis de alertas, extracción de SIDs y limpieza de reglas relacionadas con falsos positivos.

---

## Descripción de Scripts

### 1. `analiza.sh`
Script en Bash para automatizar el análisis de tráfico de red con Snort.

**Funcionalidad:**
- Convierte un archivo `.pcapng` a `.pcap` usando `editcap`.
- Ejecuta Snort con el archivo `.pcap` resultante.
- Guarda los resultados en una carpeta especificada.

**Uso:**
```bash
./analiza.sh archivo.pcapng carpeta_salida/
```

---

### 2. `analisisFP.py`
Script en Python que analiza archivos de alertas (`RS2_alert`, `RS3_alert`, `RS4_alert`) y extrae información clave.

**Funcionalidad:**
- Cuenta la cantidad de alertas en cada archivo.
- Extrae los SIDs únicos y los presenta ordenadamente.
- Genera un resumen en `resumen_alertas.txt`.

---

### 3. `extraer_sids.py`
Script para obtener los SIDs únicos desde un archivo de alertas (como `alert_fast.txt`).

**Funcionalidad:**
- Busca patrones de SID `[1:xxxx:1]`.
- Muestra los SIDs únicos y ordenados.

**Uso común:**
Se utiliza para identificar qué reglas se están activando con más frecuencia o para ayudar en la detección de falsos positivos.

---

### 4. `limpia_reglas.py`
Script de limpieza que elimina reglas de archivos `.rules` basadas en una lista de SIDs considerados falsos positivos.

**Requiere:**
- Carpeta `rules/` con archivos `.rules`.
- Archivo `falsos_positivos.txt` con SIDs (uno por línea).

**Funcionalidad:**
- Identifica y elimina las reglas que coinciden con los SIDs listados.
- Imprime un resumen indicando qué archivos fueron modificados.

---

### 5. `fusion_logs.py`
Script en Python para fusionar múltiples archivos de alertas (`alert_fast.txt`) en un solo archivo consolidado.

**Funcionalidad:**
- Lee archivos de alertas en una carpeta dada.
- Filtra líneas que contienen información válida de alertas.
- Crea un archivo `alert_fusionado.txt` con todas las alertas combinadas.

---

### 6. `contador_sids.py`
Script en Python que cuenta la aparición de cada SID en un archivo de alertas.

**Funcionalidad:**
- Extrae los SIDs del archivo.
- Cuenta la frecuencia de cada SID.
- Genera un listado ordenado por cantidad de ocurrencias.

---

### 7. `analiza_snort3.sh`
Script en Bash para analizar tráfico con Snort 3 a partir de archivos `.pcapng`.

**Funcionalidad:**
- Convierte `.pcapng` a `.pcap` usando `editcap`.
- Ejecuta Snort 3 y guarda los resultados.
- Organiza la salida en un directorio específico.

---

### 8. `fusiona_pcap.sh`
Script en Bash para fusionar múltiples archivos `.pcap` en uno solo.

**Funcionalidad:**
- Utiliza `mergecap` para combinar todos los `.pcap` de una carpeta en un único archivo.

---

## Utilidad General

Estos scripts son parte integral del flujo de trabajo de análisis de seguridad en red, ayudando a:
- Automatizar la revisión de alertas.
- Filtrar falsos positivos.
- Mantener las reglas de Snort limpias y eficientes.
- Consolidar información para análisis más eficaces.
