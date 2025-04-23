# Deteccion-de-ataques-en-red

Análisis de las Capacidades de Detección de sistemas OpenSource y Comerciales antes ataques en red y de entorno móvil

Continuación TFGs Análisis Capacidades de Detección de Ataques en Red

(1) Inicial "Familiarización": Matriz MITRE Enterprise
	- Mejorar los resultados haciendo ajuste de reglas:
		* Rendimiento tras eliminar las reglas que producen FP automáticos del tráfico legítimo.
		* Chequear calculos (detectado error en RS4: Se está sumando las alertas de Talos Community 2 veces!!)
	- Regenerar las Gráficas de Resultados (Snort/PA/FG, FP, ...) incluyendo lo anterior y el dataset legítimo "CIC2018 (FP)"
	- [Pendiente] Efecto de los Preprocesadores: idem otro TFG con estos datasets

https://attack.mitre.org/matrices/enterprise/

(2) Estudio similar para: Matriz MITRE "Mobile"
	- Identificar tácticas/Técnicas "Traffic Network"
	- Banco de ataques:
		* Datasets: oficiales (artículos científicos) y marcados
			- Buscar artículos en: https://scholar.google.es/
			- Ejemplo:	https://fkie-cad.github.io/COMIDDS/content/all_datasets/
		* Generar
		Intentar cubrir el % mayor de técnicas/tácticas
	- Detectar: Snort/FG/PA
		* Instrucciones FG/PA cuando se empiece esta etapa (Avisar!)
	- Analizar Resultados (y comparar con los de la parte Enterprise)

https://attack.mitre.org/matrices/mobile/
