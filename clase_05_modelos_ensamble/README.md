# Clase 05 — Modelos de Ensamble

**Caso**: predecir el consumo energético de un edificio (calefacción y refrigeración) a partir de sus características estructurales (dataset UCI "Energy Efficiency").

**Dataset**: `data/ENB2012_data.xlsx`

**Notebook**: `notebooks/homework_modelos_ensamble.ipynb` — resuelve lo obligatorio de `docs/homework.md`:
1. Carga, exploración y split 80/20
2. Modelo base: Árbol de decisión (RMSE/MAE/R² para Heating y Cooling Load)
3. Random Forest — comparación + `feature_importances_`
4. XGBoost — comparación con Random Forest
5. Tabla comparativa + gráfico de barras (RMSE y R²)
6. Reflexión sobre trade-off sesgo/varianza y recomendación de modelo

**Resultado de referencia**: XGBoost gana claramente sobre Random Forest y el árbol simple (R² > 0.99 en ambos targets).
