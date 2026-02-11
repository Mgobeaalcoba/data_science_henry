Introducción

¡Comenzamos!

En la clase anterior, el equipo de analítica de ShopSense Retail logró segmentar su base de clientes utilizando técnicas de clustering, descubriendo patrones de comportamiento que permitieron identificar grupos como compradores omnicanales, digitales leales o clientes tradicionales esporádicos.

Esa segmentación representó un gran paso: permitió entender qué tipo de clientes existen dentro de la base de datos. Sin embargo, el siguiente desafío natural es responder a una nueva pregunta: ¿qué producto o servicio podría interesarle a cada cliente en particular?

A partir de esta pregunta surge el concepto de sistemas de recomendación, uno de los pilares del aprendizaje automático aplicado en la vida real.

Los recomendadores son los algoritmos detrás de las sugerencias personalizadas que vemos a diario en plataformas como Netflix, Spotify o Amazon: predicen la afinidad entre usuarios y productos basándose en patrones de interacción previos.

Mientras el clustering agrupa usuarios según similitudes generales, los sistemas de recomendación buscan generar predicciones individuales, es decir, anticipar qué elementos podrían gustar a un usuario determinado.

En esta clase profundizaremos en los principales tipos de sistemas de recomendación:

Los basados en filtrado colaborativo, que utilizan el comportamiento de usuarios similares,

Los basados en contenido, que se apoyan en las características de los productos o servicios.

Los modelos híbridos, que combinan ambos enfoques para lograr mayor precisión y diversidad.

A lo largo de la sesión, analizaremos sus principios de funcionamiento, ventajas y limitaciones, y exploraremos cómo evaluar su desempeño con métricas como Precision@K, Recall@K, NDCG@K y diversidad, utilizando un notebook interactivo en Python con la librería Surprise.

Esta clase marca el puente entre la segmentación y la personalización inteligente, mostrando cómo las técnicas de aprendizaje no supervisado evolucionan para construir experiencias predictivas y adaptadas a cada usuario.

¡Éxitos! 🚀

Objetivos de la lección 💥

1
Distinguir los tipos de sistemas de recomendación, analizando sus enfoques principales y aplicaciones en distintos contextos.

2
Implementar métodos de filtrado colaborativo y basado en contenido, evaluando su eficacia en la personalización de recomendaciones.

3
Examinar técnicas de evaluación de recomendadores, comparando métricas como precisión, cobertura y diversidad para optimizar resultados.

Caso integrador de la clase 📄

ShopSense Retail: del clustering a la recomendación personalizada

Tras el análisis de segmentación realizado en la clase anterior, el equipo de analítica de ShopSense Retail logró identificar distintos tipos de clientes según su comportamiento de compra y uso de canales.

Ahora, la dirección comercial busca dar el siguiente paso: personalizar las ofertas y productos recomendados para cada uno de esos clientes, con el objetivo de aumentar la conversión y la fidelización.

Durante los últimos meses, ShopSense ha acumulado un historial de interacciones entre clientes y productos: compras realizadas, valoraciones de artículos, y tiempo de permanencia en ciertas categorías del sitio web y la aplicación móvil

Esta nueva información plantea una oportunidad clara: utilizar técnicas de sistemas de recomendación para anticipar los intereses de cada cliente y ofrecerle sugerencias relevantes en el momento adecuado.

El equipo decide iniciar una fase piloto en la que se construirán tres tipos de recomendadores:

1
Un recomendador colaborativo, basado en la similitud entre usuarios y sus patrones de compra. Por ejemplo, si un cliente A y un cliente B suelen adquirir los mismos productos de tecnología o moda, y A compra un nuevo artículo, el sistema puede recomendar ese mismo producto a B. Este enfoque aprovecha la “sabiduría colectiva” del comportamiento histórico.

2
Un recomendador basado en contenido, que analiza las características de los productos y el perfil de preferencias individuales. Si un cliente ha mostrado interés en zapatillas de running con suela amortiguada, el modelo buscará artículos con descripciones y atributos similares, personalizando las recomendaciones según el estilo de compra de cada usuario.

3
Finalmente, un modelo híbrido, que combinará ambas estrategias: la similitud entre usuarios y la similitud entre productos. Este tipo de modelo busca equilibrar precisión y diversidad, ofreciendo resultados más completos y reduciendo las limitaciones de cada método por separado



Para evaluar la calidad del sistema:

El equipo establecerá un conjunto de métricas estándar en la industria:

Precision@K (porcentaje de recomendaciones relevantes dentro del top K)

Recall@K (cobertura de elementos relevantes recuperados)

NDCG@K (orden correcto de las recomendaciones)

Además, se considerarán indicadores de novedad, diversidad y serendipity, que ayudan a medir la capacidad del modelo de sorprender al usuario con sugerencias útiles y no repetitivas.

El objetivo general del caso es comprender cómo las técnicas vistas en el módulo anterior —como el clustering y la reducción de dimensionalidad— sirven como punto de partida para la personalización, y cómo los sistemas de recomendación llevan esa lógica al siguiente nivel, generando acciones concretas sobre la experiencia del cliente.

En este módulo, vas a explorar la construcción de estos modelos mediante la librería Surprise, evaluar sus resultados con distintas métricas y reflexionar sobre los trade-offs entre precisión, cobertura y diversidad.

De esta manera, ShopSense Retail avanza desde el análisis descriptivo hacia una estrategia de personalización basada en datos, consolidando el aprendizaje no supervisado como una herramienta clave para el negocio.

Dataset

Users

Items

Interaction

¡Vamos a recapitular lo aprendido!

A lo largo de esta clase, los estudiantes conocieron cómo las diferentes familias de algoritmos de recomendación —colaborativos, basados en contenido e híbridos— permiten transformar los datos de interacción y los metadatos del catálogo en conocimiento predictivo. A través del caso ShopSense Retail, se evidenció que la personalización no es un proceso aislado, sino un ecosistema donde múltiples enfoques se complementan para ofrecer experiencias más relevantes y equilibradas.

Puntos clave de la clase:

El filtrado colaborativo convierte los comportamientos colectivos en patrones de afinidad, aprovechando las coincidencias entre usuarios y productos para generar predicciones basadas en evidencias reales.

El modelo basado en contenido construye un perfil individual a partir de los atributos de los productos, siendo esencial para cubrir el lanzamiento de nuevos ítems y mantener coherencia semántica en las recomendaciones.

Los modelos híbridos integran ambos mundos, equilibrando precisión y cobertura, y permiten ajustar dinámicamente los pesos según el tipo de usuario, la madurez del catálogo o los objetivos del negocio.

Las métricas de evaluación (Precision@K, Recall@K, NDCG@K, diversidad y novedad) son indispensables para medir el impacto del sistema no solo en exactitud técnica, sino también en la experiencia y satisfacción del usuario final.

En conjunto, esta lecture muestra el tránsito desde la agrupación de clientes hasta la personalización de sus decisiones de compra, evidenciando cómo la combinación inteligente de métodos eleva la capacidad predictiva de un sistema. En la próxima clase, se abordará la evolución natural de este proceso: los motores de recomendación avanzados, donde se incorporan arquitecturas neuronales y modelos secuenciales capaces de capturar contexto, intención y temporalidad en cada interacción.