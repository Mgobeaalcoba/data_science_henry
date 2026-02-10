✏️Consigna

En esta actividad pondrás en práctica los conceptos vistos sobre clustering y reducción de la dimensionalidad, utilizando un dataset real de clientes minoristas.

El objetivo es reproducir un flujo analítico completo que permita segmentar a los clientes según sus características de compra, visualizar los grupos en un espacio reducido y reflexionar cómo esta segmentación puede servir como proxy o paso previo a un sistema de recomendación.

Utilizarás el dataset de Kaggle(opens in a new tab)

DATASET

Tu tarea consiste en realizar un análisis no supervisado que incluya:

Exploración del dataset y tratamiento de variables numéricas relevantes.

Aplicación de K-Means para generar clusters representativos de clientes.

Evaluación del modelo mediante el método del codo y la silueta.

Representación visual de los clusters usando PCA y/o t-SNE.

Breve reflexión sobre cómo los clusters obtenidos podrían alimentar un sistema de recomendación (por similitud entre clientes o perfiles de compra).

⚠️ Requisitos mínimos (obligatorios)

•
Cargar el dataset y realizar limpieza básica (eliminar nulos, normalizar si es necesario).

•
Implementar K-Means con al menos tres valores distintos de k.

•
Evaluar con método del codo (inercia/SSE) y silueta (−1 a 1) para seleccionar el k óptimo.

•
Generar una visualización 2D con PCA mostrando los clusters.

•
Incluir un breve párrafo de interpretación (1–2 líneas por cluster) describiendo patrones observados.


