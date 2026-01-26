# Clase 03: Regresión Logística

## Objetivos
- Comprender los fundamentos de la regresión logística
- Implementar clasificación binaria y multiclase
- Interpretar coeficientes y probabilidades
- Evaluar modelos de clasificación

## Contenidos

### 1. Fundamentos
- Diferencia entre regresión lineal y logística
- Función sigmoide
- Función de costo (Log Loss)
- Descenso del gradiente

### 2. Clasificación Binaria
- Implementación con scikit-learn
- Interpretación de coeficientes
- Umbral de decisión
- Curva de decisión

### 3. Clasificación Multiclase
- One-vs-Rest (OvR)
- One-vs-One (OvO)
- Softmax regression

### 4. Métricas de Clasificación
- Matriz de confusión
- Accuracy, Precision, Recall
- F1-Score
- Curva ROC y AUC

### 5. Regularización
- L1 (Lasso) y L2 (Ridge)
- Parámetro C en logistic regression

## Notebooks

1. **01_fundamentos_logistica.ipynb**: Teoría y matemática
2. **02_clasificacion_binaria.ipynb**: Ejemplos prácticos
3. **03_clasificacion_multiclase.ipynb**: Problemas multiclase
4. **04_metricas_clasificacion.ipynb**: Evaluación de modelos
5. **05_interpretacion_modelos.ipynb**: Análisis de coeficientes

## Scripts

- `logistic_regression.py`: Implementación personalizada
- `classification_utils.py`: Utilidades para clasificación
- `metrics_plotting.py`: Visualización de métricas

## Datasets

- `titanic.csv`: Supervivencia del Titanic
- `credit_risk.csv`: Riesgo crediticio
- `customer_churn.csv`: Predicción de churn

## Ejercicios

1. Predecir supervivencia en el Titanic
2. Comparar diferentes umbrales de decisión
3. Implementar regresión logística desde cero
4. Optimizar el parámetro C
5. Analizar feature importance

## Recursos

- [Logistic Regression - StatQuest](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- [Scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
