# Clase 09 — Análisis de Series Temporales

**Caso**: CityScoot (scooters compartidos) quiere entender la tendencia y estacionalidad de sus viajes diarios.

**Dataset**: `data/cityscoot_daily_rides.csv` — ⚠️ **simulado**: el dataset original de la consigna no estaba en el repo (se perdió y no hay rastro en el historial de git). Se generó sintéticamente (2 años de viajes diarios, tendencia creciente + estacionalidad semanal + ruido, semilla fija) para que el notebook sea ejecutable. Ver `ARCHITECTURE.md` para más detalle.

**Notebook**: `notebooks/series_temporales_cityscoot.ipynb` — resuelve lo obligatorio de `docs/actividad.md`:
1. Carga de la serie en pandas
2. Gráfico de la serie completa (tendencia y estacionalidad a simple vista)
3. Descomposición aditiva con `statsmodels.tsa.seasonal.seasonal_decompose` (period=7, estacionalidad semanal)
4. Interpretación de los 3 componentes: tendencia, estacionalidad, residuo

## Nota: esta clase también es el cierre del Proyecto Integrador

`docs/4_avance_pi.md` y `docs/Reporte_Modelos.md` (+ su versión en PDF) son el **avance 4 / cierre** del PI FinanceGuard (viene de clases 03, 06 y 08) — un reporte que consolida los 3 avances anteriores, no un notebook. Se dejaron intactos: no forman parte de la consigna de esta clase (series temporales) y no cuentan para la regla de "un notebook por clase".
