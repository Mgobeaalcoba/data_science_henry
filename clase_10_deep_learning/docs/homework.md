Homework
✏️Contexto

Durante esta actividad trabajarás con datos del mercado financiero simulados a partir del índice VIX, conocido como el “índice del miedo” por reflejar la volatilidad esperada del mercado bursátil. El objetivo será construir un modelo de red neuronal recurrente (LSTM) utilizando PyTorch, capaz de predecir el valor del índice a corto plazo a partir de su comportamiento histórico.

Tu tarea consiste en:
Explorar los datos y realizar un análisis exploratorio (EDA) básico para detectar tendencias y estacionalidades.

Implementar una validación cruzada de series temporales, respetando la naturaleza secuencial de los datos.

Construir y entrenar una red LSTM en PyTorch para predecir el valor del VIX en los próximos días.

Evaluar el rendimiento del modelo con métricas adecuadas (RMSE, MAE, R²) y comparar con un modelo base (por ejemplo, persistencia o regresión lineal).

Archivos generados
econotrend_vix_sim.csv(opens in a new tab) → Dataset sintético de 5 años de valores diarios del índice VIX (simulados con tendencia y ruido estacional).

econotrend_lstm_forecast.ipynb(opens in a new tab) → Notebook base con estructura para importar datos, definir el modelo LSTM, entrenar y evaluar.

Requisitos mínimos (obligatorios)
Cargar el dataset econotrend_vix_sim.csv y realizar una limpieza y normalización de los datos.

Implementar una ventana deslizante para construir secuencias de entrenamiento (lookback = 10 días).

Dividir los datos respetando el orden temporal (sin barajado).

Construir una red LSTM en PyTorch con al menos una capa recurrente y una capa densa de salida.

Entrenar el modelo y graficar la comparación entre valores reales y predichos.

Evaluar el rendimiento con al menos dos métricas cuantitativas (MAE y RMSE).

Explicar brevemente si la serie analizada muestra evidencia de ser predecible o si se comporta como un random walk.

Extra Credits
Implementar una segunda arquitectura (por ejemplo, LSTM bidireccional o GRU) y comparar resultados.

Añadir regresores externos, como el rendimiento del S&P 500 o tasas de interés simuladas.

Guardar y recargar los pesos del modelo con torch.save() y torch.load().

Realizar una predicción multi-step (por ejemplo, horizonte de 5 días).

Incluir un gráfico de curvas de entrenamiento (loss vs epoch) para discutir overfitting o estabilidad del modelo.
