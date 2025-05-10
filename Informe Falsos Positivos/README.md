# Análisis de Trafico de Red - Dataset de Capturas y Alertas Snort

Este repositorio contiene un conjunto de trazas de tráfico de red analizadas mediante el sistema de detección de intrusiones **Snort**. Las capturas han sido procesadas utilizando diferentes paquetes de reglas (rulesets) con el fin de observar el comportamiento y las alertas generadas bajo distintos contextos de detección.

---

## Estructura del Repositorio

Cada carpeta principal corresponde a una **captura de tráfico específica** y sigue el siguiente formato:

```
XX - DIT (XX - DIT (captura_0000X_YYYYMMDD_HHMMSS))
```

Además, hay carpetas con nombres de protocolos o servicios específicos (`http`, `smtp`, `youtube`), que también siguen la misma estructura interna.

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

## Uso Sugerido

Este conjunto de datos está diseñado para facilitar el estudio comparativo de la efectividad y precisión de distintos paquetes de reglas Snort en la detección de amenazas sobre distintos tipos de tráfico.

Puedes utilizar los archivos `.xlsx` para:
- Analizar qué reglas se activan con más frecuencia.
- Comparar la cobertura de detección entre rulesets.
- Realizar análisis de falsos positivos o redundancia.

---

## Créditos

Proyecto desarrollado como parte del trabajo de fin de grado (TFG) en detección de ataques en red.
