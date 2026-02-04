💡 Conocimientos necesarios:

•
Fundamentos de regresión logística

•
Conceptos de odds y log-odds

•
Métricas de clasificación binaria

•
Interpretabilidad de modelos lineales

⚠️ Tech Stack necesario:

•
Python 3.8+

•
Pandas, NumPy

•
Scikit-learn (LogisticRegression)

•
Matplotlib, Seaborn

•
Jupyter Notebooks

Dataset

aquí
La regresión logística será tu modelo baseline. Enfócate en entender cómo funciona el algoritmo, el procesamiento de las variables, y la interpretación de los resultados. Este modelo debe ser tu referencia para comparar modelos más complejos.

Comprensión del problema y análisis exploratorio básico
Investigar qué es el churn bancario

Carga y exploración inicial del dataset (50,000 clientes)

Variables demográficas: edad, género, ubicación, antigüedad

Variables financieras: saldo promedio, productos contratados, transacciones

Variable objetivo: churn (1 = abandonó, 0 = activo)

Análisis de desbalanceo de clases (típicamente 80-20)

Preparación de datos para regresión logística
Tratamiento de valores faltantes básico

Encoding de variables categóricas (One-Hot, Label Encoding)

Escalamiento de variables numéricas (StandardScaler)

Split básico: train (80%), test (20%)

Identificación de multicolinealidad

Implementación de Regresión Logística
Regresión Logística Simple:

Implementación desde cero (opcional)

Uso de scikit-learn

Interpretación de la función sigmoide

Análisis de coeficientes:

Interpretación de pesos/coeficientes

Odds ratios y su significado

Intervalos de confianza

Evaluación específica:

Matriz de confusión

Curva ROC y AUC

Precision, Recall, F1-Score

Entrega
Debes entregar el notebook 1_EDA_RegresionLogistica.ipynb donde realices un análisis exploratorio (EDA) básico, un procesamiento de los datos básico, y los resultados de la implementación de la regresión logística.
