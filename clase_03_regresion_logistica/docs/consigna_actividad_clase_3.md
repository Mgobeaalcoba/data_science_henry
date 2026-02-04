## Consigna

FinanceGuard es un banco digital que enfrenta un incremento del 20% anual en la tasa de
abandono de clientes (churn). Como Científico de Datos Junior, tu objetivo en este primer
avance es construir un modelo baseline de predicción de churn mediante Regresión Logística,
comprendiendo cómo las variables demográficas y financieras influyen en la probabilidad de
que un cliente abandone el banco. El análisis comienza con la carga y exploración del dataset
de 50.000 clientes, la detección de valores faltantes, el tratamiento de variables categóricas y
numéricas, y la división del conjunto de datos para entrenamiento y prueba.
El modelo se implementará con scikit-learn, interpretando la función sigmoide, los
coeficientes y los odds ratios, para luego evaluar su desempeño mediante matriz de
confusión, precision, recall, F1-score y curva ROCAUC. Este trabajo se entregará en el
notebook 1_EDA_RegresionLogistica.ipynb, que servirá como base de referencia para
comparar y mejorar modelos más complejos en los próximos avances.

### Tareas a realizar

1. Comprensión del problema y análisis exploratorio básico:
○ Investigar qué es el churn bancario
○ Carga y exploración inicial del dataset 50,000 clientes)
○ Variables demográficas: edad, género, ubicación, antigüedad
○ Variables financieras: saldo promedio, productos contratados, transacciones
○ Variable objetivo: churn 1 = abandonó, 0 = activo)
○ Análisis de desbalanceo de clases (típicamente 8020
2. Preparación de datos para regresión logística:
○ Tratamiento de valores faltantes básico
○ Encoding de variables categóricas One-Hot, Label Encoding)
○ Escalamiento de variables numéricas StandardScaler)
○ Split básico: train 80%, test 20%
○ Identificación de multicolinealidad
3. Implementación de Regresión Logística:
○ Regresión Logística Simple:
■ Implementación desde cero (opcional)
■ Uso de scikit-learn
■ Interpretación de la función sigmoide
○ Análisis de coeficientes:
■ Interpretación de pesos/coeficientes
■ Odds ratios y su significado
■ Intervalos de confianza
○ Evaluación específica:
■ Matriz de confusión
■ Curva ROC y AUC
■ Precision, Recall, F1Score

Notas extra
La regresión logística será tu modelo baseline. Enfócate en entender cómo
funciona el algoritmo, el procesamiento de las variables, y la interpretación de
los resultados. Este modelo debe ser tu referencia para comparar modelos
más complejos.

