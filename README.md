# Curso de Data Science y Machine Learning

Curso completo de Data Science y Machine Learning con 10 clases teórico-prácticas más 1 clase de consulta final.

## Estructura del Curso

### Clase 01: Introducción al Machine Learning
- Conceptos fundamentales de ML
- Tipos de aprendizaje (supervisado, no supervisado, por refuerzo)
- Pipeline de un proyecto de ML
- Preparación de datos y feature engineering básico

### Clase 02: Aprendizaje Supervisado I - Regresión
- Regresión lineal simple y múltiple
- Métricas de evaluación (MSE, RMSE, MAE, R²)
- Regularización (Ridge, Lasso, ElasticNet)
- Validación cruzada

### Clase 03: Regresión Logística
- Fundamentos de regresión logística
- Función sigmoide y función de costo
- Interpretación de coeficientes
- Clasificación binaria y multiclase

### Clase 04: Modelos de Clasificación y Métricas
- K-Nearest Neighbors (KNN)
- Decision Trees
- Random Forest
- Support Vector Machines (SVM)
- Métricas: Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix

### Clase 05: Modelos de Ensamble
- Bagging y Boosting
- Random Forest en profundidad
- Gradient Boosting Machines
- XGBoost, LightGBM, CatBoost
- Stacking y Blending

### Clase 06: Optimización de Modelos
- Grid Search y Random Search
- Búsqueda bayesiana con Optuna
- Feature selection
- Análisis de importancia de características
- SHAP y LIME para interpretabilidad

### Clase 07: Aprendizaje No Supervisado I
- Clustering: K-Means, DBSCAN, Hierarchical
- Métricas de evaluación: Silhouette, Davies-Bouldin
- Elbow method y Silhouette analysis
- Casos de uso prácticos

### Clase 08: Aprendizaje No Supervisado II
- Reducción de dimensionalidad: PCA, t-SNE, UMAP
- Detección de anomalías: Isolation Forest, One-Class SVM
- Association Rules: Apriori, FP-Growth
- Aplicaciones prácticas

### Clase 09: Análisis de Series Temporales
- Componentes de series temporales
- Estacionariedad y transformaciones
- Modelos ARIMA, SARIMA
- Prophet de Facebook
- Forecasting y validación temporal

### Clase 10: Introducción al Deep Learning
- Fundamentos de redes neuronales
- Perceptrón y backpropagation
- Arquitecturas: CNN, RNN, LSTM
- Frameworks: TensorFlow/Keras y PyTorch
- Transfer Learning

### Clase 11: Consulta
- Repaso de conceptos
- Resolución de dudas
- Proyectos finales
- Q&A

## Estructura de Directorios

```
data_science_henry/
├── clase_01_introduccion_ml/
│   ├── notebooks/          # Jupyter notebooks con ejercicios y ejemplos
│   ├── scripts/            # Scripts de Python reutilizables
│   ├── docs/               # Documentación, PDFs, slides
│   └── data/               # Datos específicos de la clase
├── clase_02_regresion/
│   ├── notebooks/
│   ├── scripts/
│   ├── docs/
│   └── data/
├── [... más clases ...]
├── clase_11_consulta/
│   ├── notebooks/
│   ├── scripts/
│   ├── docs/
│   └── data/
├── data/                   # Datos compartidos
│   ├── raw/                # Datos originales
│   ├── processed/          # Datos procesados
│   └── external/           # Datos externos
├── utils/                  # Utilidades compartidas
│   ├── __init__.py
│   ├── data_processing.py
│   ├── visualization.py
│   └── model_evaluation.py
├── pyproject.toml          # Configuración de Poetry
├── README.md               # Este archivo
├── .gitignore
└── LICENSE
```

## Instalación

### Requisitos
- Python 3.9 o superior
- Poetry (gestor de dependencias)

### Pasos de instalación

1. Clonar o descargar este repositorio:
```bash
git clone <url-del-repo>
cd data_science_henry
```

2. Instalar Poetry (si no lo tienes):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Instalar dependencias:
```bash
poetry install
```

4. Activar el entorno virtual:
```bash
poetry shell
```

5. Lanzar JupyterLab:
```bash
jupyter lab
```

## Librerías Principales

### Data Processing
- **NumPy**: Operaciones numéricas y arrays
- **Pandas**: Manipulación y análisis de datos
- **SciPy**: Funciones científicas y estadísticas

### Visualización
- **Matplotlib**: Visualización básica
- **Seaborn**: Visualización estadística
- **Plotly**: Gráficos interactivos
- **Yellowbrick**: Visualización para ML

### Machine Learning
- **Scikit-learn**: Algoritmos clásicos de ML
- **XGBoost**: Gradient Boosting optimizado
- **LightGBM**: Gradient Boosting rápido
- **CatBoost**: Gradient Boosting para variables categóricas
- **Imbalanced-learn**: Manejo de datos desbalanceados
- **Optuna**: Optimización de hiperparámetros

### Deep Learning
- **TensorFlow/Keras**: Framework de DL
- **PyTorch**: Framework de DL alternativo
- **TorchVision**: Visión por computadora

### Series Temporales
- **Statsmodels**: Modelos estadísticos y series temporales

### Interpretabilidad
- **SHAP**: Explicación de modelos
- **LIME**: Interpretabilidad local

### Entorno
- **Jupyter**: Notebooks interactivos
- **JupyterLab**: IDE para notebooks

## Uso

Cada clase contiene:
- **notebooks/**: Notebooks con teoría, ejemplos y ejercicios
- **scripts/**: Scripts de Python con funciones reutilizables
- **docs/**: Material de lectura, slides, referencias
- **data/**: Datasets específicos de la clase

### Flujo de trabajo sugerido:
1. Leer la documentación en `docs/`
2. Seguir los notebooks en orden
3. Practicar con los ejercicios propuestos
4. Revisar y usar los scripts en `scripts/`
5. Aplicar lo aprendido en proyectos propios

## Recursos Adicionales

### Documentación oficial
- [Scikit-learn](https://scikit-learn.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)
- [Pandas](https://pandas.pydata.org/)

### Libros recomendados
- "Hands-On Machine Learning" - Aurélien Géron
- "Python for Data Analysis" - Wes McKinney
- "Deep Learning" - Ian Goodfellow

### Datasets
- [Kaggle](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

## Contribución

Este es un proyecto educativo. Si encuentras errores o tienes sugerencias:
1. Abre un issue
2. Propón cambios mediante pull requests
3. Comparte tus notebooks y proyectos

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para consultas sobre el curso:
- Email: mariano.gobea@mercadolibre.com
- Issues: Usa el sistema de issues del repositorio

---

Última actualización: Enero 2026
