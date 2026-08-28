# Clase 08 — Aprendizaje No Supervisado II

**Caso**: FinanceGuard, **avance 3 de 4** del Proyecto Integrador (viene de clases 03 y 06). Ahora se busca segmentar clientes para entender el churn desde un ángulo no supervisado.

**Dataset**: `data/Churn_Modelling (1).csv` (mismo caso que clases 03 y 06)

**Notebook**: `notebooks/3_AprendizajeNoSupervisado.ipynb` — nombre exigido por la consigna del PI, no renombrar. Resuelve lo obligatorio de `docs/3_avance_pi.md`:
1. K-Means (codo + silueta, interpretación de centroides, visualización 2D)
2. DBSCAN como comparación (detecta outliers, no requiere definir K)
3. PCA (varianza explicada) y t-SNE para visualización
4. Tasa de churn por segmento identificado

**Resultado de referencia**: K=4; el segmento de clientes con mayor balance pero menos productos concentra la tasa de churn más alta (~32% vs. ~20% global) — el foco prioritario para retención.

**Siguiente avance del PI**: clase 09, cierre con reporte (`docs/Reporte_Modelos.md`, no un notebook).
