## 2° avance --> Detalle

Gradient Boosting y Stacking

1
Random Forest y Gradient Boosting:

Random Forest y XGBoost:

Parámetros clave: learning_rate, max_depth, n_estimators

Early stopping y otros parámetros para evitar overfitting

Feature importance y gain

Regularización alpha y lambda

LightGBM:

Optimización para velocidad

Parámetros específicos: num_leaves, min_data_in_leaf

Categorical feature handling

CatBoost:

Manejo automático de categóricas

2
Validación cruzada y métricas especializadas:

Estrategias de CV:

StratifiedKFold para datos desbalanceados

GroupKFold para datos agrupados

StratifiedGroupKFold para datos desbalanceados y agrupados

TimeSeriesSplit para datos temporales

Métricas de evaluación:

Accuracy, Recall, y Precision

PR-AUC para datos desbalanceados

ROC-AUC para datos desbalanceados

Business metrics personalizadas

3
Stacking y Blending:

Stacking:

Nivel 1: XGBoost, LightGBM, CatBoost

Meta-learner: Regresión Logística regularizada

Cross-validation para evitar overfitting

Blending:

Holdout set para meta-learner

Ponderación óptima de modelos

4
Optimización de hiperparámetros avanzada:

Bayesian Optimization con Optuna:

Objective function personalizada

Visualización de importancia de hiperparámetros

Grid Search y Random Search:

Comparación de eficiencia

Nested cross-validation

## Consigna

Deberás entregar el notebook 2_GradientBoosting_Optimizacion.ipynb donde compares los resultados de la ejecución de los algoritmos de Random Forest, Gradient Boosting (xGBoost, LightGBM, y CatBoost), y un ensamble de modelos (solo Stacking).
Es clave que apliques optimización de hiperparámetros solamente al modelo XGBoost,  utilizando Grid Search.

La optimización utilizando Optuna es opcional, siendo bueno mencionar que hoy en día es ampliamente utilizada.  Es caso de decidir hacerla utilizar 50 trials.

🟡 Conocimientos necesarios
Algoritmos de Gradient Boosting

Técnicas de ensemble (Stacking, Blending)

Optimización bayesiana

Validación cruzada

Métricas de evaluación para modelos de clasificación

🟡 Tech Stack necesario
XGBoost, LightGBM, CatBoost

Optuna, Random/Grid Search

Scikit-learn (ensemble methods)