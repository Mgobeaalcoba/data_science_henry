# 📚 RESUMEN COMPLETO DE LA CURSADA
## Data Science y Machine Learning - Henry

**Fecha**: Febrero 2026  
**Propósito**: Repaso pre-proyecto final  
**Clase de Consulta**: Lunes próximo

---

## 🎯 ÍNDICE RÁPIDO

1. [Estadísticas de la Cursada](#estadisticas)
2. [Módulo 1: Fundamentos de ML](#modulo1)
3. [Módulo 2: Modelos Avanzados](#modulo2)
4. [Módulo 3: No Supervisado](#modulo3)
5. [Módulo 4: Series Temporales y Deep Learning](#modulo4)
6. [Resumen de Datasets](#datasets)
7. [Resumen de Algoritmos](#algoritmos)
8. [Métricas por Tipo de Problema](#metricas)
9. [Checklist de Habilidades](#checklist)
10. [Recursos para Proyecto Final](#proyecto)

---

<a id='estadisticas'></a>
## 📊 ESTADÍSTICAS DE LA CURSADA

### Contenido Total

| Métrica | Cantidad | Detalles |
|---------|----------|----------|
| **Clases teórico-prácticas** | 10 | + 1 clase de consulta |
| **Notebooks ejecutados** | 23 | Jupyter notebooks interactivos |
| **Datasets analizados** | 20 | Casos reales de diferentes dominios |
| **Algoritmos cubiertos** | 25+ | De regresión lineal a LSTM |
| **Líneas de código** | ~15,000 | Entre todos los notebooks |
| **Horas de contenido** | ~32h | Teoría + práctica |
| **Scripts Python** | 3 | En clase_01 y clase_02 |
| **Documentos de referencia** | 31 | Teoría, homeworks, guías |

### Tecnologías Dominadas

| Categoría | Herramientas |
|-----------|-------------|
| **Data Science** | NumPy, Pandas, Matplotlib, Seaborn |
| **ML Clásico** | Scikit-learn |
| **Gradient Boosting** | XGBoost, LightGBM, CatBoost |
| **Deep Learning** | PyTorch |
| **Series Temporales** | Statsmodels, Prophet |
| **Optimización** | Optuna |
| **Interpretabilidad** | SHAP, LIME |

---

<a id='modulo1'></a>
## 📖 MÓDULO 1: FUNDAMENTOS DE MACHINE LEARNING

### **Clase 01: Introducción al ML**

**Conceptos clave:**
- IA vs ML vs DL vs GenAI (jerarquía de términos)
- Tipos de aprendizaje: supervisado, no supervisado, por refuerzo
- Elementos de un modelo: features, target, parámetros, hiperparámetros
- Función de costo y proceso de optimización
- Underfitting (alto sesgo) vs Overfitting (alta varianza)
- Pipeline de ML: problema → datos → modelo → evaluación → deployment

**Caso práctico**: RetailBoost - EDA de clientes  
**Dataset**: `retailboost_customers.csv` (5 versiones)  
**Técnicas**: Análisis exploratorio, detección de outliers, correlaciones

**Lo más importante para recordar:**
- **Feature engineering** es el 70% del éxito en ML
- **EDA** es obligatorio antes de modelar
- **Overfitting** es el enemigo #1 (más datos, menos complejidad, regularización)

---

### **Clase 02: Regresión**

**Algoritmos:**
- Regresión Lineal Simple
- Regresión Lineal Múltiple
- Regresión Polinómica
- Ridge Regression (L2)
- Lasso Regression (L1)
- ElasticNet (L1 + L2)

**Métricas:**
```
MAE  = (1/n) Σ|y_true - y_pred|
MSE  = (1/n) Σ(y_true - y_pred)²
RMSE = √MSE
R²   = 1 - (SS_res / SS_tot)
MAPE = (100/n) Σ|(y_true - y_pred) / y_true|
```

**Caso práctico**: RetailBoost - Predicción de valor de cliente  
**Dataset**: `retailboost_customers_regression.csv`

**Lo más importante:**
- **R² = 0.70** es bueno, **0.85** es muy bueno, **0.95** es sospechoso (posible overfitting)
- **Regularización** (Ridge/Lasso) previene overfitting
- **Validación cruzada** es esencial (K-Fold, típicamente k=5 o 10)
- **Multicolinealidad** afecta interpretabilidad pero no predicción

---

### **Clase 03: Regresión Logística**

**Conceptos:**
- Función sigmoide: σ(z) = 1 / (1 + e^(-z))
- Log-loss (Binary Cross-Entropy)
- Odds ratio e interpretación de coeficientes
- Clasificación multiclase: One-vs-Rest (OvR), One-vs-One (OvO), Softmax

**Métricas de clasificación:**
```
Accuracy  = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)       # "De lo que predije positivo, cuánto acerté"
Recall    = TP / (TP + FN)       # "De lo realmente positivo, cuánto detecté"
F1-Score  = 2 × (Precision × Recall) / (Precision + Recall)
ROC-AUC   = Área bajo la curva ROC
```

**Caso práctico**: Churn bancario  
**Dataset**: `Churn_Modelling.csv`

**Lo más importante:**
- **Regresión logística** es clasificación (nombre confuso pero estándar)
- **ROC-AUC = 0.50** es random, **0.70** es aceptable, **0.85+** es excelente
- **Precision vs Recall**: Trade-off según costos de FP vs FN
- **Umbral = 0.5** es default pero debe ajustarse según el negocio

---

### **Clase 04: Clasificación y Métricas**

**Algoritmos:**
- K-Nearest Neighbors (KNN)
- Decision Trees (CART)
- Random Forest (Bagging de árboles)
- Support Vector Machines (SVM) con kernels (linear, RBF, poly)

**Caso práctico**: Clasificación de leads fintech  
**Dataset**: `martech_homework_dataset_fixed.csv`

**Lo más importante:**
- **KNN**: Simple pero lento (cálculo de distancias), sensible a escala
- **Decision Trees**: Interpretables pero propensos a overfitting
- **Random Forest**: Robusto, menos overfitting, más lento
- **SVM con kernel RBF**: Poderoso pero requiere tuning (C, gamma)
- **Clases desbalanceadas**: Usar F1-Score, ROC-AUC, o balancear datos

---

<a id='modulo2'></a>
## 🔧 MÓDULO 2: MODELOS AVANZADOS Y OPTIMIZACIÓN

### **Clase 05: Modelos de Ensamble**

**Conceptos:**
- **Trade-off sesgo-varianza**: Sesgo = error sistemático, Varianza = sensibilidad a datos
- **Bagging**: Reduce varianza (ej: Random Forest)
- **Boosting**: Reduce sesgo (ej: XGBoost)
- **Stacking**: Combina modelos heterogéneos
- **Voting**: Promedio de predicciones

**Algoritmos de Boosting:**
1. **XGBoost**: El más popular, muy rápido
2. **LightGBM**: Más rápido aún, para datasets grandes
3. **CatBoost**: Maneja categóricas automáticamente

**Lo más importante:**
- **Boosting** suele ganar en Kaggle (XGBoost, LightGBM)
- **Random Forest** es más robusto (menos overfitting)
- **Hiperparámetros clave**: n_estimators, max_depth, learning_rate
- **Riesgo**: Boosting puede hacer overfitting si no se regula

---

### **Clase 06: Optimización de Modelos**

**Técnicas:**
1. **Grid Search**: Busca exhaustivamente (lento pero seguro)
2. **Random Search**: Busca aleatoriamente (más rápido)
3. **Búsqueda Bayesiana** (Optuna): Inteligente, aprende de intentos previos

**Validación:**
- K-Fold Cross-Validation (típicamente k=5 o 10)
- Stratified K-Fold (para clasificación desbalanceada)
- Time Series Split (para series temporales)

**Regularización:**
- L1 (Lasso): Fuerza coeficientes a cero (feature selection)
- L2 (Ridge): Reduce magnitud de coeficientes
- Dropout: Apaga neuronas aleatoriamente (DL)
- Early Stopping: Detiene entrenamiento antes de overfitting

**Lo más importante:**
- **Optuna** es superior a Grid Search (más eficiente)
- **Validación cruzada** es obligatoria (no confiar en un solo split)
- **Feature selection** mejora generalización y interpretabilidad
- **Regularización** siempre debe considerarse

---

<a id='modulo3'></a>
## 🔍 MÓDULO 3: APRENDIZAJE NO SUPERVISADO

### **Clase 07: Clustering y Segmentación**

**Algoritmos:**
1. **K-Means**: Simple, rápido, asume clusters esféricos
2. **DBSCAN**: Detecta formas arbitrarias, identifica outliers
3. **Hierarchical**: Dendrogram, decide k después

**Métricas:**
- **Elbow method**: Encuentra k óptimo (punto de inflexión)
- **Silhouette Score**: [-1, 1], >0.5 es bueno
- **Davies-Bouldin Index**: Menor es mejor
- **Calinski-Harabasz**: Mayor es mejor

**Técnicas complementarias:**
- **PCA**: Reducción de dimensionalidad lineal
- **t-SNE**: Visualización en 2D/3D (no lineal)
- **Análisis RFM**: Recency, Frequency, Monetary (retail)

**Caso práctico**: ShopSense - Segmentación de clientes  
**Datasets**: `Mall_Customers.csv`, `shopsense_customers_clean.csv`

**Lo más importante:**
- **K-Means** requiere normalización (sensible a escala)
- **No hay "verdad" en clustering** (no hay y_true)
- **PCA** para reducir dimensiones antes de clustering
- **Interpretar clusters** es tan importante como crearlos

---

### **Clase 08: Sistemas de Recomendación**

**Enfoques:**
1. **Filtrado Colaborativo**:
   - User-Based: "Usuarios similares a ti compraron..."
   - Item-Based: "Ítems similares a los que te gustan..."
   
2. **Filtrado Basado en Contenido**:
   - Usa features de ítems (género, categoría, etc.)
   
3. **Híbridos**:
   - Combina colaborativo + contenido

**Métricas:**
```
Precision@K = (# relevant items in top-K) / K
Recall@K    = (# relevant items in top-K) / (total relevant)
NDCG@K      = Normalized Discounted Cumulative Gain (considera orden)
```

**Librería**: Surprise (para collaborative filtering)

**Caso práctico**: ShopSense - Recomendación de productos  
**Datasets**: `users_clean.csv`, `items.csv`, `interactions.csv`

**Lo más importante:**
- **Cold start problem**: Nuevos usuarios/ítems sin historial
- **Precision@K** más importante que Recall@K en producción
- **Diversidad** y **novedad** también importan (no solo accuracy)
- **Escalabilidad** es crítica (millones de usuarios × productos)

---

<a id='modulo4'></a>
## 📈 MÓDULO 4: SERIES TEMPORALES Y DEEP LEARNING

### **Clase 09: Análisis de Series Temporales**

**Componentes:**
- **Tendencia**: Movimiento a largo plazo (↗️ ↘️ →)
- **Estacionalidad**: Patrones repetitivos (diario, semanal, anual)
- **Ciclo**: Fluctuaciones no periódicas
- **Ruido**: Variabilidad aleatoria

**Test de Estacionariedad:**
- **ADF (Augmented Dickey-Fuller)**:
  - H0: Serie tiene raíz unitaria (NO estacionaria)
  - Si p < 0.05 → Serie es estacionaria
  
**Autocorrelación:**
- **ACF**: Correlación con lags pasados
- **PACF**: Correlación directa (sin intermediarios)

**Modelos:**
1. **ARIMA(p,d,q)**: Clásico, requiere estacionariedad
   - p = orden AR (autoregressive)
   - d = orden de diferenciación
   - q = orden MA (moving average)
   
2. **SARIMA**: ARIMA + componente estacional

3. **Prophet** (Facebook): Automático, maneja holidays y outliers

4. **ML para forecasting**: Random Forest, XGBoost con lags como features

**Caso práctico**: CityScoot - Predicción de demanda diaria  
**Dataset**: `cityscoot_daily_rides.csv`

**Lo más importante:**
- **Validación temporal**: NUNCA shuffle, respetar orden cronológico
- **Data leakage**: No usar información del futuro
- **Baseline**: Modelo de persistencia (ŷ_t = y_{t-1})
- **Walk-forward validation**: Reentrenar con ventana deslizante

---

### **Clase 10: Introducción al Deep Learning** ⭐

**Fundamentos:**
- **Perceptrón**: Neurona artificial básica
- **Activaciones**: ReLU, Sigmoid, Tanh, Softmax
- **Forward pass**: Datos → Predicciones
- **Backward pass**: Gradientes → Actualización de pesos
- **Función de pérdida**: MSE (regresión), Cross-Entropy (clasificación)
- **Optimizadores**: SGD, Adam, RMSprop

**Arquitecturas:**
1. **Redes Densas (Feedforward)**:
   - Para datos tabulares
   - Capas fully connected
   - Activación ReLU en ocultas
   
2. **LSTM (Long Short-Term Memory)**:
   - Para series temporales
   - Memoria a largo plazo
   - Gates: forget, input, output, cell state

**PyTorch - Componentes:**
- **Tensors**: Arrays multidimensionales (como NumPy + GPU)
- **Autograd**: Diferenciación automática
- **nn.Module**: Clase base para modelos
- **Dataset/DataLoader**: Carga eficiente de datos
- **Loss functions**: nn.MSELoss(), nn.CrossEntropyLoss()
- **Optimizers**: torch.optim.Adam(), torch.optim.SGD()

**Casos prácticos:**

#### 1. **FinShield: Detección de Fraude**
- **Dataset**: `finshield_transactions_clean.csv` (10k transacciones)
- **Modelo**: Red densa (3 capas)
- **Técnica**: Clasificación binaria
- **Métricas**: ROC-AUC, Precision, Recall

#### 2. **EconoTrend: Predicción del VIX**
- **Dataset**: `econotrend_vix_sim.csv` (1,305 observaciones, 5 años)
- **Modelo**: LSTM (2 capas × 64 unidades = 50K parámetros)
- **Técnica**: Predicción de series temporales
- **Resultados reales**:
  - MAE = 0.946 puntos VIX
  - R² = 0.666 (66.6% varianza explicada)
  - Mejora vs baseline = 1.88%
  - Tiempo entrenamiento = 5.47s (50 épocas)

**Lo más importante:**
- **Normalización** es crítica (MinMaxScaler o StandardScaler)
- **Batch size**: Típicamente 32, 64, 128 (potencias de 2)
- **Learning rate**: 0.001 es un buen default para Adam
- **Dropout** (0.2-0.5) previene overfitting
- **Early stopping**: Monitorear validation loss
- **GPU** acelera 5-10x vs CPU (pero no esencial para datasets pequeños)

**Ventanas deslizantes (LSTM)**:
```
Serie: [v1, v2, v3, v4, v5, v6, ...]

Con LOOKBACK=3:
X               y
[v1, v2, v3] → v4
[v2, v3, v4] → v5
[v3, v4, v5] → v6
...
```

---

<a id='datasets'></a>
## 📊 RESUMEN DE DATASETS

### Por Dominio

**Retail & E-commerce:**
1. `retailboost_customers.csv` - Clientes retail (EDA + Regresión)
2. `Mall_Customers.csv` - Segmentación de clientes mall
3. `shopsense_customers_clean.csv` - Clientes e-commerce
4. `items.csv` - Catálogo de productos
5. `interactions.csv` - Interacciones user-item

**Finanzas & Fintech:**
6. `Churn_Modelling.csv` - Churn bancario
7. `martech_homework_dataset_fixed.csv` - Leads fintech
8. `econotrend_vix_sim.csv` - Índice VIX (volatilidad mercado)
9. `finshield_transactions_clean.csv` - Transacciones (fraude)

**Movilidad:**
10. `cityscoot_daily_rides.csv` - Demanda diaria scooters

### Características de los Datasets

| Dataset | Filas | Columnas | Tipo | Desbalance |
|---------|-------|----------|------|------------|
| retailboost | ~1,000 | 10-15 | Tabular | Balanceado |
| Churn_Modelling | ~10,000 | 14 | Tabular | Desbalanceado (20% churn) |
| martech | ~5,000 | 8 | Tabular | Desbalanceado |
| shopsense | ~2,000 | 8 | Tabular | Balanceado |
| cityscoot | 365 | 6 | Series temporal | N/A |
| econotrend_vix | 1,305 | 2 | Series temporal | N/A |
| finshield | 10,000 | 10 | Tabular | Muy desbalanceado (<1% fraude) |

---

<a id='algoritmos'></a>
## 🤖 RESUMEN DE ALGORITMOS

### Clasificación (Completa)

| Algoritmo | Ventajas | Desventajas | Cuándo usar |
|-----------|----------|-------------|-------------|
| **Regresión Logística** | Simple, interpretable, rápido | Solo fronteras lineales | Baseline, interpretabilidad |
| **KNN** | No paramétrico, simple | Lento, sensible a escala | Pocos datos, fronteras complejas |
| **Decision Tree** | Interpretable, no requiere normalización | Overfitting fácil | Interpretabilidad |
| **Random Forest** | Robusto, feature importance | Menos interpretable, lento | Buena relación performance/effort |
| **XGBoost** | Muy preciso, rápido | Requiere tuning | Competencias, producción |
| **SVM (RBF)** | Fronteras complejas | Lento, tuning difícil | Pocos datos, alta dimensionalidad |
| **Red Densa (DL)** | Aprende features, no lineal | Caja negra, requiere más datos | Datos tabulares complejos |

### Regresión

| Algoritmo | Regularización | Complejidad | Cuándo usar |
|-----------|----------------|-------------|-------------|
| **Regresión Lineal** | No | Baja | Baseline, relaciones lineales |
| **Ridge** | L2 | Baja | Multicolinealidad |
| **Lasso** | L1 | Baja | Feature selection automático |
| **ElasticNet** | L1 + L2 | Baja | Muchas features correlacionadas |
| **Polynomial Reg** | - | Media | Relaciones no lineales |
| **Random Forest** | - | Alta | No linealidad, robustez |
| **XGBoost** | L1/L2 | Alta | Máxima precisión |
| **LSTM** | Dropout | Muy Alta | Series temporales |

### Clustering

| Algoritmo | Ventajas | Desventajas | Cuándo usar |
|-----------|----------|-------------|-------------|
| **K-Means** | Rápido, simple | Asume esferas, requiere k | Clusters esféricos |
| **DBSCAN** | Formas arbitrarias, detecta outliers | Sensible a ε y min_samples | Densidad variable |
| **Hierarchical** | No requiere k, dendrogram | Lento (O(n³)) | Visualización jerárquica |

---

<a id='metricas'></a>
## 📏 MÉTRICAS POR TIPO DE PROBLEMA

### Regresión

```python
from sklearn.metrics import (
    mean_absolute_error,         # MAE
    mean_squared_error,          # MSE, RMSE
    r2_score,                    # R²
    mean_absolute_percentage_error  # MAPE
)

mae = mean_absolute_error(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)
r2 = r2_score(y_true, y_pred)
```

**Interpretación:**
- **MAE**: Error promedio en unidades de y
- **RMSE**: Penaliza errores grandes más que MAE
- **R²**: [0, 1], fracción de varianza explicada
- **MAPE**: Error porcentual (cuidado con y=0)

---

### Clasificación

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
auc = roc_auc_score(y_true, y_proba)
```

**Cuándo usar cada métrica:**
- **Accuracy**: Solo si clases están balanceadas
- **Precision**: Minimizar falsos positivos (ej: spam detection)
- **Recall**: Minimizar falsos negativos (ej: detección de fraude)
- **F1-Score**: Balance entre Precision y Recall
- **ROC-AUC**: Rendimiento global, robusto a desbalance

---

### Clustering

```python
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

silhouette = silhouette_score(X, labels)  # [-1, 1], mayor mejor
davies_bouldin = davies_bouldin_score(X, labels)  # [0, ∞), menor mejor
calinski = calinski_harabasz_score(X, labels)  # [0, ∞), mayor mejor
```

---

### Series Temporales

```python
# Mismas que regresión + específicas:
from sklearn.metrics import mean_absolute_percentage_error

mape = mean_absolute_percentage_error(y_true, y_pred)

# Baseline: Modelo de persistencia
baseline_pred = y_test[:-1]  # ŷ_t = y_{t-1}
baseline_mae = mean_absolute_error(y_test[1:], baseline_pred)

# Tu modelo debe superar el baseline
if model_mae < baseline_mae:
    print("✅ Modelo funciona")
else:
    print("❌ Modelo no supera baseline (random walk)")
```

---

<a id='checklist'></a>
## ✅ CHECKLIST DE HABILIDADES ADQUIRIDAS

### Data Science

- [ ] Cargar y explorar datos con Pandas
- [ ] Visualizar distribuciones (histogramas, boxplots, scatter)
- [ ] Detectar y manejar valores faltantes
- [ ] Identificar y tratar outliers
- [ ] Analizar correlaciones
- [ ] Feature engineering (crear nuevas variables)
- [ ] Normalización y estandarización
- [ ] Encoding de variables categóricas (One-Hot, Label Encoding)

### Machine Learning

#### Supervisado
- [ ] Regresión lineal simple y múltiple
- [ ] Regularización (Ridge, Lasso, ElasticNet)
- [ ] Regresión logística para clasificación
- [ ] Interpretar odds ratios
- [ ] K-Nearest Neighbors
- [ ] Decision Trees
- [ ] Random Forest
- [ ] Gradient Boosting (XGBoost, LightGBM, CatBoost)
- [ ] Support Vector Machines
- [ ] Ensambles (Voting, Stacking, Blending)

#### No Supervisado
- [ ] K-Means clustering
- [ ] DBSCAN
- [ ] Hierarchical clustering
- [ ] PCA para reducción de dimensionalidad
- [ ] t-SNE para visualización
- [ ] Sistemas de recomendación (collaborative filtering)

#### Series Temporales
- [ ] Descomposición (tendencia, estacionalidad, residuos)
- [ ] Test de estacionariedad (ADF)
- [ ] ACF y PACF
- [ ] ARIMA y SARIMA
- [ ] Prophet
- [ ] Forecasting con ML (lags como features)
- [ ] Validación temporal

#### Deep Learning
- [ ] Redes neuronales densas
- [ ] Función de activación (ReLU, Sigmoid, Softmax)
- [ ] Forward y backward propagation
- [ ] Funciones de pérdida (MSE, Cross-Entropy)
- [ ] Optimizadores (Adam, SGD)
- [ ] Regularización (Dropout, Early Stopping)
- [ ] LSTM para series temporales
- [ ] PyTorch: Tensors, nn.Module, DataLoader

### Evaluación y Optimización

- [ ] Train/test split (y validación)
- [ ] K-Fold cross-validation
- [ ] Grid Search
- [ ] Random Search
- [ ] Búsqueda bayesiana (Optuna)
- [ ] Métricas de regresión (MAE, RMSE, R²)
- [ ] Métricas de clasificación (Accuracy, Precision, Recall, F1, ROC-AUC)
- [ ] Matriz de confusión
- [ ] Curva ROC
- [ ] Feature importance
- [ ] SHAP values (interpretabilidad)

### Herramientas

- [ ] Jupyter/JupyterLab
- [ ] Git para control de versiones
- [ ] Pip/Venv para gestión de dependencias
- [ ] Pandas para manipulación de datos
- [ ] Scikit-learn para ML clásico
- [ ] PyTorch para Deep Learning
- [ ] Matplotlib/Seaborn para visualización
- [ ] Optuna para optimización

---

<a id='proyecto'></a>
## 🎯 RECURSOS PARA PROYECTO FINAL

### Estructura Sugerida del Proyecto

```
mi_proyecto_final/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_models.ipynb
│   ├── 04_advanced_models.ipynb
│   ├── 05_optimization.ipynb
│   └── 06_final_model_evaluation.ipynb
├── src/
│   ├── data/
│   ├── models/
│   └── utils/
├── data/
│   ├── raw/
│   └── processed/
├── models/                    # Modelos guardados
├── reports/                   # PDFs, presentaciones
├── README.md
└── requirements.txt
```

### Checklist del Proyecto

**1. Definición del Problema** (10%)
- [ ] Descripción clara del problema de negocio
- [ ] Objetivo cuantificable
- [ ] Justificación de por qué ML es apropiado

**2. Datos** (15%)
- [ ] Descripción del dataset (origen, tamaño, features)
- [ ] Justificación de train/test split
- [ ] Manejo de datos faltantes documentado

**3. EDA** (20%)
- [ ] Estadísticas descriptivas
- [ ] Visualizaciones de distribuciones
- [ ] Análisis de correlaciones
- [ ] Detección de outliers
- [ ] Feature engineering justificado

**4. Preprocesamiento** (10%)
- [ ] Normalización/estandarización
- [ ] Encoding de categóricas
- [ ] Manejo de outliers
- [ ] Feature selection (si aplica)

**5. Modelado** (25%)
- [ ] Al menos 3 algoritmos diferentes
- [ ] Baseline simple (ej: persistencia, media, regresión lineal)
- [ ] Modelos avanzados (RF, XGBoost, DL, etc.)
- [ ] Validación cruzada

**6. Optimización** (10%)
- [ ] Tuning de hiperparámetros (Grid Search, Optuna)
- [ ] Comparación de modelos
- [ ] Selección del mejor modelo justificada

**7. Evaluación** (15%)
- [ ] Métricas apropiadas al problema
- [ ] Matriz de confusión (si clasificación)
- [ ] Análisis de errores
- [ ] Comparación con baseline

**8. Interpretabilidad** (5% bonus)
- [ ] Feature importance
- [ ] SHAP values
- [ ] Explicación de predicciones específicas

**9. Conclusiones** (5%)
- [ ] Resumen de resultados
- [ ] Recomendaciones de negocio
- [ ] Limitaciones y próximos pasos

---

## 💡 CONSEJOS PARA EL PROYECTO FINAL

### Errores Comunes a Evitar

❌ **NO hacer:**
1. Saltar el EDA (ir directo al modelo)
2. Usar Accuracy en datos desbalanceados
3. No comparar con un baseline
4. Overfitting ignorado (solo reportar train metrics)
5. No documentar decisiones
6. Modelos sin interpretabilidad
7. Conclusiones genéricas (no específicas al negocio)
8. Data leakage (usar información del futuro/test en train)

✅ **SÍ hacer:**
1. EDA exhaustivo con visualizaciones
2. Baseline simple primero
3. Al menos 3 modelos diferentes
4. Validación cruzada obligatoria
5. Documentar cada decisión importante
6. Feature importance o SHAP
7. Conclusiones de negocio (no solo técnicas)
8. README profesional con instrucciones de reproducción

### Datasets Recomendados

**Opción 1: Usa los del curso**
- RetailBoost (regresión)
- Churn bancario (clasificación)
- ShopSense (clustering + recomendaciones)
- CityScoot (series temporales)

**Opción 2: Kaggle**
- [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) - Regresión
- [Titanic](https://www.kaggle.com/c/titanic) - Clasificación binaria
- [Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud) - Clasificación desbalanceada
- [Store Sales Forecasting](https://www.kaggle.com/c/store-sales-time-series-forecasting) - Series temporales

**Opción 3: UCI ML Repository**
- [Adult Income](https://archive.ics.uci.edu/ml/datasets/adult) - Clasificación
- [Wine Quality](https://archive.ics.uci.edu/ml/datasets/wine+quality) - Regresión/Clasificación
- [Bike Sharing](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) - Series temporales

### Métricas Mínimas Requeridas

**Regresión:**
- MAE
- RMSE
- R²

**Clasificación:**
- Matriz de confusión
- Precision, Recall, F1-Score
- ROC-AUC (si binaria)

**Series Temporales:**
- MAE
- RMSE
- Comparación con baseline (persistencia)

**Clustering:**
- Silhouette Score
- Elbow plot
- Interpretación de clusters

---

## 📅 CRONOGRAMA SUGERIDO PARA PROYECTO

**2 semanas antes de entrega:**
- Selección de dataset y definición de problema
- EDA completo
- Baseline implementado

**1 semana antes:**
- Modelos avanzados implementados
- Optimización de hiperparámetros
- Evaluación comparativa

**3 días antes:**
- Interpretabilidad y visualizaciones finales
- Documentación completa
- Revisión final

**1 día antes:**
- Presentación preparada
- Código limpio y ejecutable
- README profesional

---

## 🔗 ENLACES RÁPIDOS

### Documentación del Curso
- [README Principal](../README.md)
- [QUICKSTART](../QUICKSTART.md)
- [ARCHITECTURE](../ARCHITECTURE.md) (este archivo)
- [CONTRIBUTING](../CONTRIBUTING.md)

### Clase 10 (Deep Learning) - Material Extra
- [Análisis Completo VIX-LSTM](../clase_10_deep_learning/docs/ANALISIS_COMPLETO_VIX_LSTM.md)
- [Lecturas Recomendadas](../clase_10_deep_learning/docs/LECTURAS_RECOMENDADAS_VIX_LSTM.md)
- [Verificación de Datos](../clase_10_deep_learning/docs/VERIFICACION_AFIRMACIONES_DATOS.md)
- [Guía para Instructores](../clase_10_deep_learning/notebooks/LECTURAS_COMPLETAS_POR_CELDA.md)

---

## 📧 Contacto y Soporte

**Instructor**: Mariano Gobea  
**Email**: mariano.gobea@mercadolibre.com  
**Clase de Consulta**: Lunes próximo

**Para dudas urgentes**: Usa el sistema de issues del repositorio

---

**Última actualización**: Febrero 16, 2026  
**Próxima revisión**: Post proyecto final

🎓 **¡Éxito en tu proyecto!**
