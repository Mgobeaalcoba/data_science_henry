¡Comenzamos!

¡Bienvenidos/as! En el mundo real, los datos rara vez vienen acompañados de etiquetas que indiquen a qué grupo pertenece cada observación. En estos escenarios, donde el objetivo no es predecir una variable sino descubrir estructuras ocultas y patrones naturales, entran en juego las técnicas de aprendizaje no supervisado.

Dentro de este enfoque, una de las tareas más utilizadas es el clustering o agrupamiento, cuyo propósito es identificar subconjuntos de observaciones similares entre sí según sus características. Estas agrupaciones permiten obtener una visión más profunda de los datos, generando información valiosa para la toma de decisiones: segmentar clientes, identificar perfiles de consumo, clasificar productos según comportamiento, o incluso detectar anomalías.

En esta lección exploraremos las principales técnicas de clustering, comenzando por los algoritmos particionales, como K-Means, y los basados en densidad, como DBSCAN. Analizaremos cómo funcionan, cuándo conviene aplicar cada uno y cómo evaluar la calidad de los grupos formados mediante métricas como el método del codo y el índice de silueta.

Además, conoceremos cómo los métodos de reducción de dimensionalidad, como PCA y t-SNE, ayudan a simplificar los conjuntos de datos y visualizar relaciones complejas en espacios más reducidos minimizando la pérdida de información relevante.

A lo largo de la clase, trabajaremos con un caso aplicado al sector retail —ShopSense Retail—, donde el equipo de analítica busca segmentar a sus clientes a partir de variables de comportamiento (frecuencia, gasto, recencia y uso de canales). A través de este caso, aprenderemos a combinar técnicas de clustering y reducción de dimensionalidad para obtener insights útiles que podrán servir como paso previo para un sistema de recomendación en la siguiente unidad. 🚀 ¡Éxitos!

Objetivos de la lección 💥

1
Aplicar técnicas de clustering como K-Means y DBSCAN para segmentar datos y descubrir patrones dentro de conjuntos de datos no etiquetados.

2
Evaluar la calidad de los clusters mediante el método del codo y el índice de silueta, determinando la estructura óptima de agrupación.

3
Explorar métodos de reducción de dimensionalidad como PCA y t-SNE, analizando la varianza explicada y su impacto en la simplificación de datos.

Caso integrador de la clase 📄

ShopSense Retail – Explorando patrones de comportamiento sin etiquetas

En esta clase trabajaremos con un caso aplicado al sector retail: ShopSense Retail, una cadena de tiendas que busca comprender mejor el comportamiento de sus clientes a partir de sus registros de compras en distintos canales (web, app y tienda física).

Durante los últimos meses, el área de analítica de ShopSense ha recolectado información detallada sobre las interacciones de cuatro mil clientes, incluyendo su frecuencia de compra, gasto promedio, tiempo desde la última compra, uso de cupones, devoluciones y antigüedad en la marca. Sin embargo, no cuentan con etiquetas que indiquen a qué tipo de cliente pertenece cada uno, ni con una clasificación previa de segmentos.

El objetivo del equipo es descubrir grupos naturales de clientes que compartan características similares, con el fin de generar estrategias de marketing más efectivas y personalizar futuras recomendaciones de productos.

Para lograrlo, se propone aplicar diferentes técnicas de aprendizaje no supervisado, comenzando por el clustering particional (K-Means) y el clustering por densidad (DBSCAN).

En la primera etapa, el equipo explorará las variables RFM —Recency (tiempo desde la última compra), Frequency (número de compras recientes) y Monetary (gasto total)— junto con la proporción de uso de los distintos canales de compra (web_pct, app_pct, store_pct). Mediante visualizaciones y análisis de dispersión, intentarán identificar si existe alguna separación evidente entre los clientes, o si es necesario recurrir a algoritmos que descubran esa estructura oculta.



Luego, se aplicará el algoritmo K-Means probando distintos valores de k y evaluando los resultados mediante los métodos del codo y de la silueta para determinar el número óptimo de clusters. Posteriormente, se experimentará con DBSCAN, un algoritmo basado en densidad que permite detectar grupos de forma arbitraria y manejar datos con ruido o valores atípicos.

Una vez identificados los grupos más representativos, se explorarán técnicas de reducción de dimensionalidad como PCA y t-SNE. En el caso de PCA, permitirá reducir la dimensionalidad del dataset preservando la mayor varianza posible. Se analizará la varianza explicada acumulada para determinar cuántas componentes principales retener. Por otra parte, t-SNE se utilizará específicamente para visualización exploratoria, permitiendo observar en dos dimensiones las relaciones no lineales entre los datos. Ambas técnicas facilitarán entender la distribución de los clientes y comprobar la coherencia de los clusters obtenidos.

Finalmente, se realizará una mini demostración del enfoque “cluster-then-predict”, donde se usará la etiqueta sintética next_purchase_30d (probabilidad de que el cliente vuelva a comprar en los próximos 30 días) para mostrar cómo los clusters pueden incorporarse como una nueva característica predictiva en un modelo de clasificación supervisado.

💪🏽 Este caso permitirá comprender paso a paso cómo pasar de un conjunto de datos sin etiquetas a un modelo que descubre patrones, los valida y los utiliza para mejorar la toma de decisiones.

Los resultados servirán como base conceptual para la siguiente clase, centrada en la construcción de sistemas de recomendación.

¡Vamos a recapitular lo aprendido!

La sesión permitió recorrer de manera integral el proceso de aprendizaje no supervisado, aplicando distintas familias de algoritmos sobre el caso ShopSense Retail para descubrir y validar la estructura de comportamiento en la base de clientes. Desde la exploración inicial hasta la reducción de dimensionalidad, el equipo experimentó cómo cada técnica aporta una perspectiva distinta del mismo fenómeno y cómo, combinadas, construyen una visión completa y honesta del negocio.

•
K-Means permitió obtener una segmentación operativa útil para ejecutar campañas diferenciadas, creando cuatro perfiles interpretables de clientes según sus hábitos de compra y uso de canales. Aunque las métricas revelaron estructura débil (silhouette 0.240, sin codo marcado), estos segmentos resultan valiosos para ejecución táctica cuando se comprende que representan divisiones graduales dentro de un continuo más que grupos naturalmente separados.

•
DBSCAN reveló la estructura real de densidad de los datos: un único grupo denso homogéneo que agrupa el 98.8% de los clientes, más 47 outliers (1.2%) con comportamientos genuinamente excepcionales (170% más devoluciones, 71% más uso de cupones, 49% más gasto). Este hallazgo validó la interpretación de K-Means y estableció expectativas realistas: las diferencias entre clientes son graduales, no categóricas, lo cual orienta hacia personalización continua más que segmentaciones rígidas.

•
Las métricas de evaluación (inercia y silueta) ayudaron a validar la coherencia de los clusters y a comprender la estructura real de los datos, equilibrando rigor estadístico con interpretación de negocio. La combinación de silhouette bajo en K-Means y estructura de grupo único en DBSCAN contó una historia coherente sobre la homogeneidad de la base, permitiendo al equipo tomar decisiones informadas con expectativas realistas.

•
PCA y t-SNE sirvieron como herramientas de reducción y visualización, resumiendo múltiples variables en componentes interpretables y confirmando visualmente la estructura identificada por las métricas. PCA mostró la superposición considerable entre clusters de K-Means, mientras que t-SNE (con la advertencia de que amplifica diferencias sutiles) permitió explorar variaciones locales dentro del grupo homogéneo. Estas representaciones reducidas preparan los datos para el modelado predictivo posterior.

El valor pedagógico de esta sesión radica en la honestidad metodológica: el equipo aprendió que "no encontrar múltiples grupos densamente diferenciados" es un resultado igualmente valioso que "encontrar varios clusters", y que interpretar correctamente las métricas es más importante que obtener valores "altos". Esta comprensión permite tomar decisiones estratégicas realistas: K-Means responde "¿cómo puedo dividir mi base en segmentos operativos útiles?" mientras que DBSCAN responde "¿cuál es la estructura real de densidad?". Ambas perspectivas son complementarias y necesarias.

En conjunto, estas técnicas sentaron las bases para pasar del análisis descriptivo al modelado predictivo y sistemas de recomendación, donde los clusters identificados y las componentes reducidas se transformarán en insumos para anticipar preferencias y personalizar la experiencia de cada cliente en ShopSense Retail. Con la comprensión de que las similitudes entre clientes son graduales más que categóricas, el sistema podrá aprovechar matices de comportamiento que van más allá de la pertenencia a un cluster específico, generando recomendaciones más precisas y personalizadas.
