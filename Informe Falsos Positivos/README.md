# Análisis de Trafico de Red - Dataset de Capturas y Alertas Snort

Este repositorio contiene un conjunto de trazas de tráfico de red analizadas mediante el sistema de detección de intrusiones **Snort**. Las capturas han sido procesadas utilizando diferentes paquetes de reglas (rulesets) con el fin de observar el comportamiento y las alertas generadas bajo distintos contextos de detección.

---

## Estructura del Repositorio

Cada carpeta principal corresponde a una **captura de tráfico específica**


### Dentro de cada carpeta de captura:

- `RS1/`
- `RS2/`
- `RS3/`
- `RS4/`

Cada una de estas carpetas representa un conjunto de reglas Snort (ruleset) diferente, aplicadas sobre la misma traza de tráfico. Dentro de cada carpeta de ruleset se encuentran:

- **Archivos de log de Snort** correspondientes a las alertas generadas.
- Un archivo `.xlsx` con un resumen estadístico de las alertas:
  - **SID** (Snort ID) únicos detectados.
  - **Frecuencia** de aparición de cada SID.

- `Raw Log Files/`

Contiene los logs crudos de Snort generados al analizar la traza con los cuatro rulesets. Sirve como repositorio completo y sin filtrar del análisis.

---

