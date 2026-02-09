### Introducción: 

Cuando entrenamos un modelo de machine learning, nuestro objetivo no es simplemente que “aprenda” los datos, sino que entienda sus patrones de forma que pueda generalizar: funcionar bien con ejemplos nuevos, en contextos reales.

En esta lecture vamos a recorrer justamente ese camino: entender qué significa que un modelo esté “aprendiendo de más” (overfitting) o “de menos” (underfitting), entender por qué un simple train-test split no siempre es suficiente para evaluar el rendimiento, y cómo la validación cruzada nos da una visión más robusta del desempeño del modelo. También vamos a hablar de métricas de evaluación, para aprender a elegir la más adecuada según el problema, y de ajuste de hiperparámetros, que nos permite optimizar los modelos de manera sistemática. Todo esto es parte del mismo objetivo: construir modelos confiables, que no solo brillen en entrenamiento, sino que agreguen valor en producción.

### Objetivos: 

1. Evaluar la importancia de la validación cruzada, explorando métodos como K-Fold para mejorar la robustez y generalización de los modelos.
2. Distinguir el concepto de sobreajuste y subajuste, analizando su impacto en el rendimiento de modelos de aprendizaje automático.
3. Aplicar técnicas de optimización de hiperparámetros como Grid Search, Random Search y Optuna, integrando estrategias de regularización L1 y L2 para mejorar la precisión.

### Resumen: 

A lo largo de esta clase vimos que entrenar un modelo no se trata únicamente de apretar un botón y aceptar el resultado. Hay que mirar con cuidado qué está pasando: si está cayendo en overfitting o underfitting, si nuestras métricas realmente reflejan el problema, y si estamos validando de manera robusta.

La validación cruzada nos dio una forma de evaluar con mayor confianza; las métricas, un lenguaje para comparar; y las técnicas de ajuste de hiperparámetros, un método para explorar configuraciones de manera ordenada. En conjunto, estas herramientas nos permiten pasar de tener un modelo “que funciona en mi máquina” a un modelo que aprende bien y generaliza mejor.

El desafío ahora es poner en práctica todo esto en tus propios experimentos: pensar qué métrica elegir, cómo validar los resultados y cómo ajustar los hiperparámetros con criterio. Ese es el camino para que tus modelos no solo sean técnicamente correctos, sino también útiles en el mundo real. 🚀