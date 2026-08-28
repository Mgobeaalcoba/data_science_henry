# Clase 03 — Regresión Logística

**Caso**: FinanceGuard, un banco digital, pierde 20% de sus clientes por año (churn). Como Data Scientist Jr., este es el **avance 1 de 4** del Proyecto Integrador: un modelo baseline de regresión logística que sirve de referencia para los avances posteriores (clases 06, 08 y 09).

**Dataset**: `data/Churn_Modelling.csv` (10.000 clientes; diccionario de variables en `docs/diccionario_variables.md`)

**Notebook**: `notebooks/1_EDA_RegresionLogistica.ipynb` — nombre exigido por la consigna del PI, no renombrar. Resuelve lo obligatorio de `docs/consigna_actividad_clase_3.md` y `docs/consigna_avance_1_PI.md`:
1. Exploración del churn bancario y del desbalanceo de clases
2. Preparación: encoding, escalado, split 80/20, mención de multicolinealidad
3. Regresión logística con scikit-learn: sigmoide, coeficientes, odds ratios
4. Evaluación: matriz de confusión, curva ROC/AUC, precision/recall/F1

**Resultado de referencia**: AUC ≈ 0.78, Accuracy ≈ 0.81 (baseline — se espera que los avances 2 y 3 lo mejoren).

**Siguiente avance del PI**: clase 06 (`2_GradientBoosting_Optimizacion.ipynb`).
