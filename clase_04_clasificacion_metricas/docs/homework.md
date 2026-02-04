## Homework

### Contexto

Estás trabajando en el equipo de analítica de una fintech que busca optimizar su presupuesto de marketing. El objetivo es construir un modelo que clasifique prospectos (leads) en función de su probabilidad de conversión, para decidir en qué contactos vale la pena invertir más recursos.

Contás con un dataset histórico de usuarios que fueron impactados por campañas online. Algunas personas compraron un producto financiero, otras no. A partir de ese historial, deberás entrenar modelos que permitan predecir si un nuevo usuario tiene alta o baja probabilidad de conversión.

Este tipo de problema es típico de la industria Martech y es un caso real de aplicación de modelos de clasificación para scoring de leads.

### Dataset ( /Users/mgobea/Documents/Personal_Develop/data_science_henry/clase_04_clasificacion_metricas/docs/resumen_contenidos.md )

Cada fila representa un lead. Las variables incluidas son:

age: edad del usuario

income: ingreso estimado

web_visits: cantidad de visitas previas al sitio

clicked_ad: si hizo clic en una campaña reciente (1 = sí, 0 = no)

device_type: tipo de dispositivo utilizado (mobile, desktop, tablet)

time_on_site: minutos promedio por visita

past_purchases: cantidad de compras anteriores en la plataforma

converted: variable objetivo (1 = compró, 0 = no compró)

### Tu objetivo

Construir un clasificador que permita predecir la probabilidad de conversión de un nuevo lead, utilizando los datos históricos para entrenar y comparar modelos.

### Pasos necesarios: 

01. Explorá el dataset:
Revisá la distribución de las variables, su relación con la variable objetivo y posibles transformaciones necesarias (por ejemplo, codificación de variables categóricas o escalado).

02. Entrená y compará al menos 3 modelos:
K-Vecinos más cercanos (KNN)

Árbol de decisión

SVM (con kernel lineal o no lineal)

(Opcional) Agregá regresión logística.

03. Evaluá el rendimiento con las métricas adecuadas:
Accuracy

Precisión

Recall

F1-score

AUC y curva ROC

04. Seleccioná el mejor modelo según su rendimiento general y según el criterio de negocio:
En este caso, es preferible detectar bien los usuarios que sí convertirán, incluso si eso implica asumir algunos falsos positivos.

05. Presentá tus conclusiones:
¿Qué modelo tuvo mejor desempeño?

¿Qué variable parece tener mayor peso en la clasificación?

¿Qué estrategia sugerirías al equipo de marketing con base en los resultados?

💡 Tip final
No se espera que construyas el modelo perfecto, sino que puedas comparar alternativas y justificar tu elección. Este es el tipo de análisis que se espera de un/a Data Scientist en contextos reales de negocio.
