# Análisis de Falsos Positivos - TFG

Este directorio contiene los resultados del análisis de alertas generadas por Snort, centrándose en la identificación de **falsos positivos** y la modificación de reglas para mejorar la eficacia del sistema IDS.

---

## Estructura del Directorio

### Carpetas de Capturas
- `01 - DIT (...)` hasta `07 - DIT (...)`
- `http`
- `youtube`

Cada una de estas carpetas contiene los archivos de alertas generadas por Snort al aplicar diferentes conjuntos de reglas (`RS1_alert`, `RS2_alert`, `RS3_alert`, `RS4_alert`). Estas alertas provienen de diferentes escenarios de tráfico.

### Archivos `*-FP`
- `01-DIT-FP`, `02-DIT-FP`, ..., `07-DIT-FP`
- `http-FP`, `youtube-FP`

Estos archivos contienen las alertas específicas que han sido **identificadas como falsos positivos** dentro de cada escenario y conjunto de reglas. Se utilizan como referencia para limpiar los paquetes de reglas en pasos posteriores.

### Informe Rulesets
Contiene un informe por cada ruleset, detallando qué SIDs han sido responsables de generar falsos positivos, agrupadas por escenario de captura.


---

## Propósito

El análisis de falsos positivos tiene como objetivo:
- Identificar reglas que se activan incorrectamente.
- Reducir el ruido en los análisis de Snort.
- Mejorar la calidad de los rulesets personalizados.



---

## Relación con Scripts

Este directorio es generado y gestionado con ayuda de los scripts disponibles en el repositorio:
- `extraer_sids.py`: para identificar SIDs activadas.
- `limpia_reglas.py`: para eliminar reglas problemáticas.
- `analisisFP.py`: para generar resúmenes de alertas.

---
