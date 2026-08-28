# Clase 06 — Optimización de Modelos

**Caso**: FinanceGuard, **avance 2 de 4** del Proyecto Integrador (viene de clase 03). Ahora se comparan algoritmos de boosting y se optimiza XGBoost.

**Dataset**: `data/Churn_Modelling.csv` (mismo dataset que clase 03)

**Notebook**: `notebooks/2_GradientBoosting_Optimizacion.ipynb` — nombre exigido por la consigna del PI, no renombrar. Resuelve lo obligatorio de `docs/2_avance_pi_consigna.md`:
1. Comparación de Random Forest, XGBoost, LightGBM, CatBoost y un Stacking (meta-learner: regresión logística)
2. `GridSearchCV` aplicado solamente a XGBoost (la consigna lo pide así; Optuna queda como opcional, no implementado, para mantener el notebook corto)
3. Validación con `StratifiedKFold` (el dataset está desbalanceado) y métricas Accuracy/Precision/Recall/ROC-AUC
4. Tabla comparativa final

**Resultado de referencia**: el Stacking gana por muy poco margen sobre CatBoost (ROC-AUC ≈ 0.870 vs. 0.870); el tuning de XGBoost aporta una mejora modesta pero real sobre su versión default.

**Siguiente avance del PI**: clase 08 (`3_AprendizajeNoSupervisado.ipynb`).
