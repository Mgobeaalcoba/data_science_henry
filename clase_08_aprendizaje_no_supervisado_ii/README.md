# Clase 08 — Aprendizaje No Supervisado II

**Caso**: FinanceGuard, **avance 3 de 4** del Proyecto Integrador (viene de clases 03 y 06). Ahora se busca segmentar clientes para entender el churn desde un ángulo no supervisado.

**Dataset**: `data/Churn_Modelling.csv` (mismo caso que clases 03 y 06)

**Notebook**: `notebooks/3_AprendizajeNoSupervisado.ipynb` — nombre exigido por la consigna del PI, no renombrar. Resuelve lo obligatorio de `docs/3_avance_pi.md`:
1. K-Means (codo + silueta, interpretación de centroides, visualización 2D)
2. DBSCAN como comparación (detecta outliers, no requiere definir K)
3. PCA (varianza explicada y cargas) y t-SNE para visualización
4. Tasa de churn por segmento identificado

**Resultado de referencia**: K=3 (óptimo según coeficiente de silueta); el segmento de clientes en Alemania con mayor balance concentra la tasa de churn más alta (~32.4% vs. ~20.4% global) — el foco prioritario para retención.

**Siguiente avance del PI**: clase 09, cierre con reporte (`docs/Reporte_Modelos.md`, no un notebook).
