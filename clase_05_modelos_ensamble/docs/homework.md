## Homework

### 🎯Objetivos

Entrenar y comparar dos métodos de ensamble —Random Forest Regressor y XGBoost Regressor— en un problema de regresión multivariable: predecir el consumo energético de edificios (Heating Load y Cooling Load) a partir de sus características estructurales.

#### Variables predictoras (features):
- Relative Compactness
- Surface Area
- Wall Area
- Roof Area
- Overall Height
- Orientation
- Glazing Area
- Glazing Area Distribution

#### Variables objetivo (targets):
- Heating Load (Y1)
- Cooling Load (Y2)

### Consiga

#### Carga y exploración de datos
- Importar el dataset, visualizar sus dimensiones y explorar las variables.
- Verificar si existen valores nulos o atípicos.

#### Preparación del dataset
- Separar las variables predictoras (X) de las variables objetivo (Y1 y Y2).
- Dividir en entrenamiento y prueba (ej: 80% / 20%).

#### Modelo base: Árbol de decisión
- Entrenar un DecisionTreeRegressor como punto de comparación.
- Evaluar con métricas de regresión (RMSE, MAE, R²) sobre Heating y Cooling Load.

#### Random Forest Regressor
- Entrenar un Random Forest con diferentes valores de n_estimators y min_samples_leaf.
- Comparar resultados con el árbol individual.
- Analizar la importancia de variables (feature_importances_).

#### XGBoost Regressor
- Entrenar un XGBoost ajustando n_estimators, max_depth y learning_rate.
- Comparar con Random Forest en términos de métricas.

#### Comparación de resultados
- Crear una tabla comparativa con todas las métricas para Árbol, Random Forest y XGBoost.
- Representar visualmente los resultados con un barplot de RMSE y R².

### Reflexión final
¿Qué modelo recomendarías para un caso real de predicción energética?
¿Cómo influye el trade-off sesgo/varianza en Random Forest y en XGBoost?
¿Qué ventajas y desventajas encontraste en cada técnica?

### Formato de trabajo
Un notebook en Python (.ipynb) con: Código limpio y comentado. Resultados con métricas y gráficos. Una breve conclusión al final con la recomendación de modelo.
