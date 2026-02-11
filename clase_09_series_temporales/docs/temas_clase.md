¡Bienvenidos a la Lecture: Análisis de series temporales!

En el mundo real, muchos fenómenos no se comportan de forma aislada, sino que evolucionan en el tiempo: las temperaturas diarias, las ventas mensuales o el valor de una acción. Su característica principal es que el tiempo influye en los valores observados: lo que ocurre hoy depende, en parte, de lo que pasó antes. Los datos temporales revelan patrones que nos permiten comprender el pasado y anticipar el futuro. Este tipo de información, conocida como serie temporal, constituye una de las fuentes más valiosas para la analítica de negocio y el aprendizaje automático.

En esta clase aprenderemos a descomponer una serie temporal en sus componentes fundamentales —tendencia, estacionalidad y ruido—, a evaluar su estacionariedad mediante pruebas estadísticas y a analizar la autocorrelación de los datos con funciones ACF y PACF. A partir de allí, exploraremos los principales modelos de predicción temporal: los clásicos ARIMA y SARIMA, el modelo aditivo Prophet y los enfoques modernos de machine learning como Random Forest y XGBoost, que permiten abordar el forecasting desde una perspectiva supervisada.

El objetivo no será únicamente dominar las técnicas, sino también entender cuándo y por qué utilizar cada una, reconociendo sus fortalezas y limitaciones según el tipo de serie, la cantidad de datos disponibles y la naturaleza del negocio.

Al finalizar esta lección, serás capaz de construir un flujo completo de análisis temporal: desde la exploración de la serie y su descomposición hasta la implementación, validación y comparación de modelos predictivos, interpretando los resultados como insumos estratégicos para la toma de decisiones.

¡Éxitos! 👩🏽‍💻

Objetivos de la lección 💥

1
Analizar los componentes esenciales de las series de tiempo, diferenciando tendencia, estacionalidad y ruido para interpretar patrones temporales en los datos.

2
Determinar la estacionariedad de una serie mediante pruebas estadísticas y evaluar la autocorrelación con funciones ACF y PACF para seleccionar modelos adecuados.

3
Implementar modelos ARIMA, SARIMA y Prophet, además de enfoques basados en machine learning como Random Forest y XGBoost, optimizando la predicción de series temporales.

Caso integrador de la clase 📄

CityScoot Forecasting

CityScoot, la plataforma de alquiler de scooters eléctricos, ha consolidado una importante base de usuarios en diferentes ciudades. Hasta ahora, el equipo de analítica ha trabajado modelos de regresión para entender los factores que explican la demanda diaria, como el clima, el marketing y los precios dinámicos.

Sin embargo, la dirección ahora solicita dar un paso más: predecir la cantidad de viajes diarios para las próximas semanas. El objetivo es anticipar la demanda futura y optimizar la distribución de flota, el mantenimiento preventivo y las campañas publicitarias.

Desafío analítico:

A partir del historial de viajes diarios del último año, el equipo de datos deberá:

1
Explorar la serie temporal y descomponerla en sus componentes de tendencia, estacionalidad y ruido.

2
Evaluar la estacionariedad mediante pruebas estadísticas y gráficos de autocorrelación (ACF, PACF).

3
Entrenar y comparar modelos de predicción:

Modelos estadísticos: ARIMA y SARIMA.

Modelo aditivo: Prophet.

Modelos de machine learning: Random Forest Regressor y XGBoost Regressor (enfoque supervisado con lags y features externas).

4
Seleccionar el modelo más adecuado según métricas como RMSE, MAE y MAPE.

Dataset

Cityscoot Daily rides