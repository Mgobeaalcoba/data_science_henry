3° avance

Contexto:

FinanceGuard es un banco digital que enfrenta un desafío crítico: una tasa anual de abandono de clientes del 20%, lo que implica pérdidas significativas. Para revertir esta situación, la compañía busca aprovechar el potencial del análisis de datos y el aprendizaje automático. En este contexto, el estudiante, en su rol de Científico de Datos Junior, forma parte del equipo encargado de desarrollar un sistema predictivo que identifique a los clientes con mayor probabilidad de abandonar la entidad, facilitando estrategias de retención más efectivas.

Tu rol:

En este tercer avance, asumes el rol de analista de segmentación y exploración no supervisada. Tu responsabilidad es aplicar técnicas de clustering y reducción de dimensionalidad para descubrir patrones ocultos en los datos de los clientes. A través de estas técnicas, deberás identificar segmentos con comportamientos diferenciados y analizar su relación con la tasa de churn, aportando una visión complementaria a los modelos supervisados desarrollados previamente.

Deberás entregar el notebook 3_AprendizajeNoSupervisado.ipynb donde implemente técnicas de clustering (K-Means y DBSCAN) para segmentar la base de clientes, y aplique reducción de dimensionalidad (PCA y t-SNE) para visualizar patrones en los datos.

Detalle del avance:

Clustering básico para segmentación:

K-Means clustering:

Conceptos fundamentales: centroides, iteraciones

Selección del número de clusters K:

Método del codo (Elbow method)

Coeficiente de silueta (Silhouette score)

Implementación paso a paso

Interpretación de centroides

Visualización de clusters en 2D

DBSCAN (Density-Based clustering):

Conceptos: core points, border points, noise

Parámetros básicos: eps (epsilon) y min_samples

Ventajas: detecta outliers, no requiere definir K

Comparación con K-means

Reducción de dimensionalidad:

PCA (Principal Component Analysis):

Conceptos básicos: componentes principales

Varianza explicada por cada componente

Selección del número de componentes

Visualización de datos en 2D y 3D

Interpretación de los componentes principales

t-SNE básico:

Visualización no lineal de datos

Parámetro perplexity (concepto básico)

Diferencias con PCA

Limitaciones y cuidados en interpretación

Aplicación al problema de churn:

Segmentación de clientes:

Aplicar K-means al dataset de clientes

Identificar 3-5 segmentos principales

Analizar características de cada segmento

Tasa de churn por segmento identificado

Perfiles de clientes por cluster:

Características demográficas y comportamiento por cluster

Crear features derivadas del clustering

Conocimientos necesarios
Conceptos básicos de clustering (K-means, DBSCAN)

Reducción de dimensionalidad (PCA, t-SNE básico)

Métricas de evaluación no supervisada

🟡 Tech Stack necesario
Scikit-learn (KMeans, DBSCAN, PCA)

Matplotlib, Seaborn para visualizaciones

Pandas, NumPy para manipulación de datos

🟡 Notas extra
La segmentación no supervisada puede revelar patrones “ocultos” en el comportamiento de los clientes. Usa estos insights para mejorar el feature engineering, y crear modelos más específicos.

Descripción de variables:
* RowNumber: Índice de la fila.
* CustomerId: Identificador único para cada cliente.
* Surname: Apellido del cliente (puede no ser útil para el análisis).
* CreditScore: Puntuación crediticia del cliente [300 : 850].
* Geography: País del cliente (ej. Francia, España).
* Gender: Género del cliente (ej. Masculino, Femenino).
* Age: Edad del cliente.
* Tenure: Número de años que el cliente ha estado con el banco.
* Balance: Saldo de cuenta del cliente.
* NumOfProducts: Número de productos que ha comprado el cliente.
* HasCrCard: Si el cliente tiene tarjeta de crédito (1 = Sí, 0 = No).
* IsActiveMember: Si el cliente es un miembro activo (1 = Sí, 0 = No).
* EstimatedSalary: Salario anual estimado del cliente.
* Exited: Si el cliente dejó el banco (1 = Sí, 0 = No) – esta es la variable objetivo.
* 