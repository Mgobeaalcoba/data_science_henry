# Clase 10 — Introducción al Deep Learning

**Caso de la clase (en la teórica)**: FinShield, detección de fraude transaccional con redes densas en PyTorch — se recorre en la presentación, no es el homework a entregar.

**Caso del homework**: EconoTrend quiere predecir el índice VIX ("índice del miedo" de volatilidad del mercado) a partir de su comportamiento histórico, usando una LSTM en PyTorch.

**Dataset**: `data/econotrend_vix_sim.csv` (serie simulada de 5 años)

**Notebook**: `notebooks/vix_lstm_didactico.ipynb` — resuelve lo obligatorio de `docs/homework.md`:
1. Carga, limpieza y normalización (`MinMaxScaler` ajustado solo sobre train)
2. Ventana deslizante (lookback = 10 días) para armar secuencias de entrenamiento
3. Split respetando el orden temporal (sin barajar)
4. LSTM en PyTorch con capa recurrente + capa densa de salida
5. Entrenamiento y gráfico real vs. predicho
6. Evaluación con MAE y RMSE, comparando contra modelos base (persistencia y regresión lineal)
7. Conclusión sobre si el VIX simulado es predecible o se comporta como random walk

**Resultado de referencia**: LSTM y Regresión Lineal quedan prácticamente empatadas (R² ≈ 0.67 ambas) — la señal predecible de esta serie simulada es mayormente lineal, así que la complejidad extra de la LSTM no se traduce en mejor desempeño. Ese hallazgo (comparar siempre contra un baseline simple) es el punto pedagógico central del notebook.
