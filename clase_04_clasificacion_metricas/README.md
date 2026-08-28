# Clase 04 — Modelos de Clasificación y Métricas

**Caso**: una fintech quiere priorizar en qué leads (prospectos) invertir presupuesto de marketing, clasificándolos según probabilidad de conversión.

**Dataset**: `data/martech_homework_dataset_fixed.csv`

**Notebook**: `notebooks/homework_clasificacion_leads_fintech.ipynb` — resuelve lo obligatorio de `docs/homework.md`:
1. Exploración del dataset y transformaciones necesarias (encoding, escalado)
2. Comparación de al menos 3 modelos: KNN, Árbol de decisión, SVM
3. Evaluación con Accuracy, Precision, Recall, F1-score, AUC y curva ROC
4. Selección del mejor modelo según el criterio de negocio (priorizar recall: mejor algún falso positivo que perderse un lead que sí convierte)
5. Conclusiones para el equipo de marketing

**Resultado de referencia**: SVM gana en las 5 métricas (Recall ≈ 0.63, AUC ≈ 0.88); la variable con más peso es el tiempo en el sitio (`time_on_site`).
