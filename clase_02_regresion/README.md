# Clase 02: Aprendizaje Supervisado I - Regresión

## Objetivos
- Comprender los fundamentos de la regresión lineal
- Implementar modelos de regresión con scikit-learn
- Evaluar modelos usando métricas apropiadas
- Aplicar técnicas de regularización

## Contenidos

### 1. Regresión Lineal Simple
- Concepto de regresión
- Función de costo (MSE)
- Método de mínimos cuadrados
- Interpretación de coeficientes

### 2. Regresión Lineal Múltiple
- Extensión a múltiples variables
- Multicolinealidad
- Feature selection básico

### 3. Métricas de Evaluación
- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R²** (Coeficiente de determinación)
- **MAPE** (Mean Absolute Percentage Error)

### 4. Regularización
- **Ridge Regression (L2)**
- **Lasso Regression (L1)**
- **ElasticNet**
- Selección de hiperparámetros

### 5. Validación de Modelos
- Train/Test split
- Validación cruzada (K-Fold)
- Análisis de residuos

## Notebooks

1. **01_regresion_simple.ipynb**: Implementación desde cero
2. **02_regresion_multiple.ipynb**: Regresión con múltiples features
3. **03_metricas_evaluacion.ipynb**: Comparación de métricas
4. **04_regularizacion.ipynb**: Ridge, Lasso y ElasticNet
5. **05_validacion_cruzada.ipynb**: Técnicas de validación

## Scripts

- `linear_regression.py`: Implementación personalizada
- `model_training.py`: Pipeline de entrenamiento
- `metrics.py`: Cálculo de métricas

## Datasets

- `boston_housing.csv`: Predicción de precios de casas
- `salary_data.csv`: Predicción de salarios
- `california_housing.csv`: Housing prices en California

## Ejercicios

1. Implementar regresión lineal desde cero
2. Comparar rendimiento de diferentes modelos
3. Analizar el efecto de la regularización
4. Realizar feature engineering para mejorar predicciones
5. Validar modelos con K-Fold CV

## Recursos

- [Linear Regression - StatQuest](https://www.youtube.com/watch?v=nk2CQITm_eo)
- [Ridge and Lasso Regression](https://scikit-learn.org/stable/modules/linear_model.html)
