# 🎓 Curso de Data Science y Machine Learning - Henry
## Formación Completa: Del ML Clásico al Deep Learning

**Duración**: 11 clases (10 teórico-prácticas + 1 consulta)  
**Nivel**: Principiante a Intermedio  
**Última actualización**: Febrero 2026

---

## 📚 Contenido del Curso

### **Módulo 1: Fundamentos de Machine Learning**

#### **📌 Clase 01: Introducción al Machine Learning**
- Conceptos fundamentales: IA, ML, DL, GenAI
- Tipos de aprendizaje (supervisado, no supervisado, por refuerzo)
- Pipeline completo de un proyecto de ML
- Elementos de un modelo: features, target, parámetros, hiperparámetros
- Underfitting vs Overfitting
- Feature engineering básico
- **Caso práctico**: EDA de clientes RetailBoost
- **Datasets**: `retailboost_customers.csv`

#### **📌 Clase 02: Regresión**
- Regresión lineal simple y múltiple
- Métricas: MSE, RMSE, MAE, R², MAPE
- Regularización: Ridge (L2), Lasso (L1), ElasticNet
- Regresión polinómica
- Validación cruzada (K-Fold)
- Análisis de residuos
- **Caso práctico**: Predicción de valor de clientes RetailBoost
- **Datasets**: `retailboost_customers_regression.csv`

#### **📌 Clase 03: Regresión Logística**
- Fundamentos y función sigmoide
- Clasificación binaria y multiclase (OvR, OvO, Softmax)
- Interpretación: odds, log-odds, odds ratio
- Métricas de clasificación (Accuracy, Precision, Recall, F1-Score, ROC-AUC)
- Log-loss y regularización
- **Caso práctico**: Predicción de churn bancario
- **Datasets**: `Churn_Modelling.csv`

#### **📌 Clase 04: Modelos de Clasificación y Métricas**
- K-Nearest Neighbors (KNN)
- Decision Trees (árboles de decisión)
- Random Forest
- Support Vector Machines (SVM) con kernels
- Métricas avanzadas para clasificación
- Manejo de clases desbalanceadas
- **Caso práctico**: Clasificación de leads fintech
- **Datasets**: `martech_homework_dataset_fixed.csv`

---

### **Módulo 2: Modelos Avanzados y Optimización**

#### **📌 Clase 05: Modelos de Ensamble**
- Trade-off sesgo-varianza
- Bagging: Random Forest en profundidad
- Boosting: Gradient Boosting, XGBoost, LightGBM, CatBoost
- Stacking y Blending
- Voting ensembles
- Bootstrap y submuestreo de características
- **Caso práctico**: Comparación de algoritmos de boosting

#### **📌 Clase 06: Optimización de Modelos**
- Overfitting vs Underfitting
- Grid Search y Random Search
- Búsqueda bayesiana (Optuna)
- Feature selection y feature importance
- Regularización avanzada (L1, L2, ElasticNet)
- Ajuste fino de Gradient Boosting
- **Caso práctico**: Optimización de hyperparámetros con Optuna

---

### **Módulo 3: Aprendizaje No Supervisado**

#### **📌 Clase 07: Clustering y Segmentación**
- Algoritmos: K-Means, DBSCAN, Hierarchical
- Métricas: Elbow method, Silhouette, Davies-Bouldin
- Reducción de dimensionalidad: PCA, t-SNE
- Análisis RFM (Recency, Frequency, Monetary)
- **Caso práctico**: Segmentación de clientes ShopSense Retail
- **Datasets**: `Mall_Customers.csv`, `shopsense_customers_clean.csv`

#### **📌 Clase 08: Sistemas de Recomendación**
- Filtrado colaborativo (user-based, item-based)
- Filtrado basado en contenido
- Modelos híbridos
- Métricas: Precision@K, Recall@K, NDCG@K
- Librería Surprise
- **Caso práctico**: Sistema de recomendación ShopSense
- **Datasets**: `users_clean.csv`, `items.csv`, `interactions.csv`

---

### **Módulo 4: Series Temporales y Deep Learning**

#### **📌 Clase 09: Análisis de Series Temporales**
- Componentes: tendencia, estacionalidad, ruido
- Estacionariedad y pruebas estadísticas (ADF)
- Autocorrelación: ACF, PACF
- Modelos clásicos: ARIMA, SARIMA
- Prophet (Facebook)
- Forecasting como problema supervisado (Random Forest, XGBoost)
- Validación temporal y prevención de data leakage
- **Caso práctico**: Predicción de demanda diaria CityScoot
- **Datasets**: `cityscoot_daily_rides.csv`

#### **📌 Clase 10: Introducción al Deep Learning** ⭐
- Fundamentos de redes neuronales
- Perceptrón, activaciones, backpropagation
- PyTorch: Tensors, Autograd, Dataset, DataLoader, nn.Module
- Redes densas (feedforward) para clasificación
- LSTM para series temporales
- Regularización: dropout, early stopping
- Optimizadores: Adam, SGD
- **Casos prácticos**:
  - FinShield: Detección de fraude con redes densas
  - EconoTrend: Predicción del VIX con LSTM
- **Datasets**: `finshield_transactions_clean.csv`, `econotrend_vix_sim.csv`
- **⭐ Material extra**: Documentación extensa en `docs/` con análisis completo, lecturas recomendadas, y verificaciones

#### **📌 Clase 11: Consulta y Repaso**
- Repaso de conceptos clave de todo el curso
- Resolución de dudas
- Preparación para proyecto final
- Q&A abierto

---

## 🗂️ Estructura de Directorios

```
data_science_henry/
├── clase_01_introduccion_ml/
│   ├── notebooks/          # 3 notebooks (EDA RetailBoost)
│   ├── scripts/            # 2 scripts (preprocessing, data_loader)
│   ├── docs/               # 3 documentos
│   ├── data/               # 5 datasets
│   └── README.md
├── clase_02_regresion/
│   ├── notebooks/          # 3 notebooks (Regresión RetailBoost)
│   ├── scripts/            # 1 script (get_metrics)
│   ├── docs/               # 3 documentos
│   ├── data/               # 1 dataset
│   └── README.md
├── clase_03_regresion_logistica/
│   ├── notebooks/          # 2 notebooks (Churn prediction)
│   ├── docs/               # 4 documentos
│   ├── data/               # 1 dataset
│   └── README.md
├── clase_04_clasificacion_metricas/
│   ├── notebooks/          # 1 notebook (Leads fintech)
│   ├── docs/               # 2 documentos
│   └── data/               # 1 dataset
├── clase_05_modelos_ensamble/
│   ├── notebooks/          # 1 notebook
│   └── docs/               # 2 documentos
├── clase_06_optimizacion_modelos/
│   ├── notebooks/          # 3 notebooks (+ catboost_info/)
│   └── docs/               # 2 documentos
├── clase_07_aprendizaje_no_supervisado_i/
│   ├── notebooks/          # 2 notebooks (Clustering Mall/ShopSense)
│   ├── docs/               # 2 documentos
│   └── data/               # 3 datasets
├── clase_08_aprendizaje_no_supervisado_ii/
│   ├── notebooks/          # 2 notebooks (Recomendaciones ShopSense)
│   ├── docs/               # 2 documentos
│   └── data/               # 4 datasets
├── clase_09_series_temporales/
│   ├── notebooks/          # 2 notebooks (CityScoot forecasting)
│   ├── docs/               # 4 documentos
│   └── data/               # 1 dataset
├── clase_10_deep_learning/ ⭐
│   ├── notebooks/          # 4 notebooks + 2 markdown guías
│   ├── docs/               # 7 documentos (análisis exhaustivo)
│   ├── data/               # 2 datasets
│   └── README.md
├── clase_11_consulta/
│   └── README.md
├── utils/                  # Módulo de utilidades compartidas
│   ├── __init__.py
│   ├── data_processing.py
│   ├── visualization.py
│   └── model_evaluation.py
├── pyproject.toml          # Configuración de herramientas de desarrollo
├── requirements.txt        # Gestión de dependencias con pip
├── README.md               # Este archivo
├── QUICKSTART.md           # Guía de inicio rápido
├── ARCHITECTURE.md         # Arquitectura del proyecto
├── CONTRIBUTING.md         # Guía de contribución
├── LICENSE                 # Licencia MIT
└── Makefile                # Comandos automatizados
```

**Nota**: Las carpetas `scripts/` vacías fueron eliminadas. Solo `clase_01` y `clase_02` mantienen scripts útiles.

---

## 📊 Estadísticas del Proyecto

- **Total de notebooks**: 23
- **Total de datasets**: 20
- **Total de documentos**: 31
- **Scripts útiles**: 3 (en clase_01 y clase_02)
- **Clases con README**: 5 de 11

---

## 🚀 Instalación Rápida

### Opción 1: Con Makefile (Recomendado y automatizado)

```bash
# 1. Navegar al proyecto
cd data_science_henry

# 2. Crear entorno virtual e instalar dependencias automáticamente
make install

# 3. Activar entorno virtual
source .venv/bin/activate

# 4. Lanzar JupyterLab
make jupyter
```

### Opción 2: Con pip + venv (Manual)

```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar entorno
source .venv/bin/activate  # Mac/Linux
# o
.venv\Scripts\activate     # Windows

# 3. Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Lanzar Jupyter
jupyter lab
```

---

## 🛠️ Tecnologías y Librerías

### **Core Data Science**
- **NumPy** (1.26.4): Operaciones numéricas
- **Pandas** (2.3.3): Manipulación de datos
- **Matplotlib/Seaborn**: Visualización
- **SciPy**: Funciones científicas

### **Machine Learning**
- **Scikit-learn**: Algoritmos clásicos de ML
- **XGBoost**: Gradient Boosting optimizado
- **LightGBM**: Gradient Boosting rápido
- **CatBoost**: GB para variables categóricas
- **Optuna**: Optimización bayesiana

### **Deep Learning**
- **PyTorch** (2.2.2): Framework de DL
- **TorchVision**: Visión por computadora

### **Series Temporales**
- **Statsmodels**: Modelos estadísticos (ARIMA, SARIMA)
- **Prophet**: Forecasting (Facebook)

### **Interpretabilidad**
- **SHAP**: Explicación de modelos
- **LIME**: Interpretabilidad local
- **Yellowbrick**: Visualización para ML

### **Entorno**
- **JupyterLab**: IDE para notebooks
- **Pip/Venv**: Gestión de dependencias

---

## 📖 Guías de Uso

### Para Estudiantes

1. **Inicio**: Lee `QUICKSTART.md`
2. **Orden**: Sigue las clases secuencialmente (01 → 11)
3. **Práctica**: Ejecuta cada notebook celda por celda
4. **Experimentación**: Modifica código y parámetros
5. **Consulta**: Usa clase_11 para dudas finales

### Para Instructores

1. **Estructura**: Ver `ARCHITECTURE.md` para detalles técnicos
2. **Material**: Cada clase tiene docs/ con presentaciones y guías
3. **Scripts**: clase_01 y clase_02 tienen scripts reutilizables
4. **Evaluación**: Homeworks en notebooks claramente etiquetados

---

## 🎯 Casos Prácticos por Dominio

| Dominio | Clase | Caso | Dataset |
|---------|-------|------|---------|
| **Retail** | 01-02 | RetailBoost: EDA y regresión | retailboost_customers.csv |
| **Finanzas** | 03 | Churn bancario | Churn_Modelling.csv |
| **Marketing** | 04 | Clasificación de leads fintech | martech_homework.csv |
| **Retail** | 07-08 | ShopSense: clustering y recomendaciones | shopsense_customers.csv |
| **Movilidad** | 09 | CityScoot: forecasting de demanda | cityscoot_daily_rides.csv |
| **Finanzas** | 10 | EconoTrend: predicción del VIX con LSTM | econotrend_vix_sim.csv |
| **Fintech** | 10 | FinShield: detección de fraude con DL | finshield_transactions.csv |

---

## 🔥 Highlights del Curso

### **Clase 10: Deep Learning** ⭐ **[MÁS COMPLETA]**

La clase de Deep Learning incluye material pedagógico extenso:

- **4 notebooks** (2 casos prácticos + 2 guías)
- **7 documentos** de análisis y referencias
- **Material extra**:
  - `ANALISIS_COMPLETO_VIX_LSTM.md`: Análisis exhaustivo de resultados
  - `LECTURAS_RECOMENDADAS_VIX_LSTM.md`: 30+ recursos organizados por nivel
  - `VERIFICACION_AFIRMACIONES_DATOS.md`: 87 afirmaciones verificadas
  - `LECTURAS_COMPLETAS_POR_CELDA.md`: Guía para instructores
  - `CORRECCIONES.md`: Documentación de soluciones a problemas comunes

**Notebooks destacados:**
1. `homework_vix_lstm_completo_didactico.ipynb` (3,066 líneas, 1.6 MB)
   - Tutorial completo de LSTM en PyTorch
   - 100% didáctico con explicaciones exhaustivas
   - Predice el índice VIX (volatilidad del mercado)
   - Incluye WIKIs, visualizaciones, y lecturas recomendadas

2. `finshield_pytorch_dense_Edited_Leo2.ipynb`
   - Detección de fraude transaccional
   - Redes densas en PyTorch
   - Pipeline completo de clasificación

---

## 📊 Recursos Adicionales

### Librerías Principales

**Data Processing**:
- NumPy, Pandas, SciPy

**Visualización**:
- Matplotlib, Seaborn, Plotly, Yellowbrick

**Machine Learning**:
- Scikit-learn, XGBoost, LightGBM, CatBoost, Imbalanced-learn, Optuna

**Deep Learning**:
- PyTorch, TorchVision

**Series Temporales**:
- Statsmodels, Prophet

### Libros Recomendados

- **"Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow"** - Aurélien Géron
- **"Python for Data Analysis"** - Wes McKinney
- **"Deep Learning"** - Ian Goodfellow, Yoshua Bengio, Aaron Courville
- **"Forecasting: Principles and Practice"** - Rob J Hyndman & George Athanasopoulos (online gratis)

### Datasets Públicos

- [Kaggle](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

## 🎓 Proyecto Final

El curso culmina con un proyecto integrador que debe incluir:

1. **Definición del problema** de negocio
2. **EDA exhaustivo** con visualizaciones
3. **Preprocesamiento** y feature engineering
4. **Modelado** con al menos 3 algoritmos diferentes
5. **Optimización** de hiperparámetros
6. **Evaluación** con métricas apropiadas
7. **Interpretabilidad** (SHAP/LIME)
8. **Conclusiones** y recomendaciones de negocio

**Consulta previa al proyecto**: Clase 11 (próximo lunes)

---

## 🤝 Contribución

Este es un proyecto educativo activo. Contribuciones bienvenidas:

1. Abre un **issue** para reportar errores
2. Propón **mejoras** mediante pull requests
3. Comparte tus **notebooks** y proyectos

Ver `CONTRIBUTING.md` para más detalles.

---

## 📧 Contacto

**Instructor**: Mariano Gobea  
**Email**: mariano.gobea@mercadolibre.com / gobeamariano@gmail.com  
**Consultas**: Usa el sistema de issues del repositorio

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver el archivo `LICENSE` para más detalles.

---

**Última actualización**: Febrero 2026  
**Versión del curso**: 1.0.0

🚀 **¿Listo para comenzar? → Abre `QUICKSTART.md`**
