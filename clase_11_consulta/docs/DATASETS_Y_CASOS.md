# 📊 GUÍA COMPLETA DE DATASETS Y CASOS
## Referencia Rápida para Proyecto Final

**Fecha**: Febrero 2026  
**Propósito**: Ayudarte a elegir un dataset o inspirarte en los casos vistos

---

## 🎯 DATASETS DEL CURSO (Por Dominio)

### 🛒 RETAIL & E-COMMERCE (7 datasets)

#### 1. **RetailBoost - Clientes** (Clases 01-02)
**Archivos**:
- `retailboost_customers.csv` (raw)
- `retailboost_customers_processed.csv`
- `retailboost_customers_regression.csv`

**Características**:
- ~1,000 clientes
- 10-15 columnas
- Variables: edad, ingresos, tiempo como cliente, compras, gastos, segmento

**Problemas abordados**:
- Clase 01: EDA y feature engineering
- Clase 02: Regresión (predecir valor de cliente)

**Métricas logradas**:
- R² ≈ 0.70-0.85 (dependiendo del modelo)
- MAE ≈ $500-800

---

#### 2. **ShopSense - E-commerce** (Clases 07-08)
**Archivos**:
- `shopsense_customers_clean.csv`
- `Mall_Customers.csv`
- `customers_with_clusters.csv`
- `users_clean.csv`
- `items.csv`
- `interactions.csv`

**Características**:
- ~2,000 clientes
- Variables RFM: Recency, Frequency, Monetary
- Transacciones user-item

**Problemas abordados**:
- Clase 07: Segmentación de clientes (K-Means, DBSCAN)
- Clase 08: Segmentación de clientes con aprendizaje no supervisado (K-Means, DBSCAN, PCA y t-SNE). Los clusters pueden utilizarse luego como insumo para recomendación.

**Métricas logradas**:
- Silhouette Score: 0.55-0.65
- Precision@10: 0.35-0.45

---

### 🏦 FINANZAS & FINTECH (4 datasets)

#### 3. **Churn Bancario** (Clase 03)
**Archivo**: `Churn_Modelling.csv`

**Características**:
- ~10,000 clientes bancarios
- 14 columnas
- Target: churn (0/1) - ~20% tasa de abandono
- Variables: geografía, género, edad, balance, productos, actividad

**Problema**: Predecir abandono de clientes

**Métricas típicas**:
- ROC-AUC: 0.75-0.85
- F1-Score: 0.45-0.55 (desbalanceado)
- Precision: 0.60-0.70
- Recall: 0.40-0.50

**Desafío**: Clases desbalanceadas (80/20)

---

#### 4. **MarTech - Leads Fintech** (Clase 04)
**Archivo**: `martech_homework_dataset_fixed.csv`

**Características**:
- ~5,000 leads
- 8 columnas
- Target: conversión (0/1)
- Variables: fuente, dispositivo, tiempo en sitio, páginas vistas

**Problema**: Predecir conversión de leads

**Métricas típicas**:
- ROC-AUC: 0.70-0.80
- Precision@10%: 0.80+ (top 10% de leads)

---

#### 5. **EconoTrend - Índice VIX** (Clase 10)
**Archivo**: `econotrend_vix_sim.csv`

**Características**:
- 1,305 observaciones (5 años: 2020-2025)
- 2 columnas: date, vix
- Serie temporal con tendencia leve (+0.618)
- VIX promedio: 21.54 ± 2.34
- Estacionaria (ADF p-value = 0.000000)
- Alta autocorrelación (lag-1 = 0.88)

**Problema**: Predicción de volatilidad del mercado con LSTM

**Métricas logradas (LSTM 2×64)**:
- MAE: 0.946 puntos VIX
- RMSE: 1.189 puntos
- R²: 0.666 (66.6% varianza explicada)
- Mejora vs baseline: +1.88%
- Tiempo entrenamiento: 5.47s (50 épocas)

**Desafío**: Serie semi-random walk (difícil de predecir)

---

#### 6. **FinShield - Detección de Fraude** (Clase 10)
**Archivo**: `finshield_transactions_clean.csv`

**Características**:
- 10,000 transacciones
- 10 columnas
- Target: fraud_label (0/1) - muy desbalanceado (<1%)
- Variables: monto, país, dispositivo, hora, IP, merchant

**Problema**: Detección de fraude transaccional con redes densas

**Métricas típicas**:
- ROC-AUC: 0.95+ (red densa)
- Precision: Crítica (minimizar FP = no molestar clientes legítimos)
- Recall: También crítica (detectar fraude real)

**Desafío**: Extremadamente desbalanceado

---

### 🛴 MOVILIDAD (1 dataset)

#### 7. **CityScoot - Demanda Diaria** (Clase 09)
**Archivo**: `cityscoot_daily_rides.csv`

**Características**:
- 365 observaciones (1 año)
- 6 columnas: fecha, viajes, temp_media, lluvia, eventos, marketing_spend
- Serie temporal con estacionalidad semanal
- Promedio: ~400 viajes/día

**Problema**: Forecasting de demanda de scooters eléctricos

**Modelos probados**:
- ARIMA/SARIMA
- Prophet
- Random Forest/XGBoost (con lags)

**Métricas típicas**:
- MAE: 40-80 viajes
- RMSE: 60-100 viajes
- MAPE: 15-25%

**Desafío**: Estacionalidad + tendencia + eventos externos

---

## 📋 TABLA COMPARATIVA DE DATASETS

| Dataset | Filas | Target | Tipo | Desbalance | Dificultad | Dominio |
|---------|-------|--------|------|------------|------------|---------|
| **RetailBoost** | ~1,000 | Continuo ($) | Regresión | N/A | ⭐⭐ | Retail |
| **Churn Bancario** | ~10,000 | Binario (0/1) | Clasificación | 80/20 | ⭐⭐⭐ | Finanzas |
| **Leads Fintech** | ~5,000 | Binario (0/1) | Clasificación | 85/15 | ⭐⭐⭐ | Marketing |
| **ShopSense** | ~2,000 | Sin target | Clustering | N/A | ⭐⭐ | E-commerce |
| **ShopSense Recom.** | ~10,000 | Ratings | Recomendación | N/A | ⭐⭐⭐⭐ | E-commerce |
| **CityScoot** | 365 | Continuo | Serie Temporal | N/A | ⭐⭐⭐⭐ | Movilidad |
| **VIX** | 1,305 | Continuo | Serie Temporal | N/A | ⭐⭐⭐⭐⭐ | Finanzas |
| **FinShield** | 10,000 | Binario | Clasificación | 99/1 | ⭐⭐⭐⭐⭐ | Fintech |

**Dificultad:**
- ⭐⭐ = Principiante
- ⭐⭐⭐ = Intermedio
- ⭐⭐⭐⭐ = Avanzado
- ⭐⭐⭐⭐⭐ = Muy avanzado

---

## 🎯 CASOS DE USO POR ALGORITMO

### Si quieres practicar REGRESIÓN:
✅ **RetailBoost** (regresión) - Predecir valor de cliente  
✅ Kaggle: House Prices - Predecir precios de casas  
✅ UCI: Bike Sharing - Predecir demanda de bicicletas

### Si quieres practicar CLASIFICACIÓN:
✅ **Churn Bancario** - Predecir abandono  
✅ **Leads Fintech** - Predecir conversión  
✅ **FinShield** - Detectar fraude  
✅ Kaggle: Titanic - Supervivencia (binaria)  
✅ Kaggle: Credit Card Fraud - Fraude (muy desbalanceado)

### Si quieres practicar CLUSTERING:
✅ **ShopSense** - Segmentación de clientes  
✅ **Mall Customers** - Segmentación demográfica  
✅ UCI: Iris - Clustering clásico (fácil)

### Si quieres practicar RECOMENDACIONES:
✅ **ShopSense** - Recomendación de productos  
✅ Kaggle: MovieLens - Recomendación de películas  
✅ Amazon Product Reviews - Recomendación de productos

### Si quieres practicar SERIES TEMPORALES:
✅ **CityScoot** - Demanda diaria  
✅ **VIX** - Volatilidad del mercado  
✅ Kaggle: Store Sales - Ventas por tienda  
✅ UCI: Air Quality - Predicción de calidad del aire

### Si quieres practicar DEEP LEARNING:
✅ **VIX** - LSTM para series temporales  
✅ **FinShield** - Redes densas para fraude  
✅ Kaggle: MNIST - Clasificación de dígitos (CNNs)  
✅ Kaggle: IMDB Reviews - Sentiment analysis (RNNs)

---

## 💼 CASOS POR INDUSTRIA

### **Retail & E-commerce**
- Segmentación de clientes (Clustering)
- Predicción de valor de cliente (Regresión)
- Sistema de recomendaciones (Collaborative Filtering)
- Predicción de demanda (Series Temporales)
- Detección de fraude en compras (Clasificación)

### **Finanzas**
- Predicción de churn (Clasificación)
- Detección de fraude (Clasificación desbalanceada)
- Predicción de volatilidad (Series Temporales + DL)
- Credit scoring (Clasificación)
- Predicción de precios de activos (Regresión)

### **Marketing**
- Clasificación de leads (Clasificación)
- Segmentación de audiencia (Clustering)
- Predicción de conversión (Clasificación)
- Optimización de campañas (Regresión)

### **Movilidad & Logística**
- Predicción de demanda (Series Temporales)
- Optimización de rutas (No visto, pero aplicable)
- Mantenimiento predictivo (Clasificación)

---

## 🔍 CÓMO ELEGIR TU DATASET PARA EL PROYECTO

### Pregúntate:

1. **¿Qué tipo de problema me interesa más?**
   - Predicción numérica → Regresión
   - Clasificación → Clasificación
   - Patrones sin etiquetas → Clustering
   - Predicción temporal → Series Temporales
   - Reto técnico → Deep Learning

2. **¿Cuánto tiempo tengo?**
   - 1 semana → Dataset simple (Titanic, RetailBoost)
   - 2 semanas → Dataset intermedio (Churn, CityScoot)
   - 3+ semanas → Dataset complejo (VIX, FinShield, proyecto propio)

3. **¿Qué dominio me atrae?**
   - Finanzas → Churn, VIX, Credit Fraud
   - Retail → RetailBoost, ShopSense
   - Marketing → Leads Fintech
   - Movilidad → CityScoot
   - Tecnología → FinShield

4. **¿Quiero usar en mi portfolio?**
   - Proyecto con valor de negocio claro
   - Métricas impresionantes
   - Visualizaciones profesionales
   - README bien documentado

---

## 📈 MÉTRICAS DE REFERENCIA (Para Comparar)

### Regresión

| Dataset | Métrica | Baseline | Buen Modelo | Excelente |
|---------|---------|----------|-------------|-----------|
| RetailBoost | R² | 0.50 | 0.70 | 0.85+ |
| House Prices | R² | 0.60 | 0.80 | 0.90+ |
| VIX | R² | 0.65 (persist.) | 0.67-0.70 | 0.75+ |

### Clasificación

| Dataset | Métrica | Baseline | Buen Modelo | Excelente |
|---------|---------|----------|-------------|-----------|
| Churn | ROC-AUC | 0.50 | 0.75 | 0.85+ |
| Titanic | Accuracy | 0.70 | 0.80 | 0.85+ |
| Fraude | ROC-AUC | 0.50 | 0.90 | 0.95+ |

### Series Temporales

| Dataset | Métrica | Baseline | Buen Modelo | Excelente |
|---------|---------|----------|-------------|-----------|
| CityScoot | MAPE | 25% | 15-20% | <15% |
| VIX | MAE | 0.96 (persist.) | 0.94 | <0.90 |

---

## 🚀 DATASETS EXTERNOS RECOMENDADOS

### Kaggle (Ordenados por dificultad)

#### **Principiante:**
1. **[Titanic](https://www.kaggle.com/c/titanic)** ⭐⭐
   - Clasificación binaria (supervivencia)
   - ~900 pasajeros
   - Features: edad, sexo, clase, etc.
   - **Perfecto para empezar**

2. **[House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)** ⭐⭐
   - Regresión (precio de casas)
   - ~1,400 casas
   - 79 features (muchas categóricas)
   - Requiere feature engineering

#### **Intermedio:**
3. **[Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)** ⭐⭐⭐
   - Clasificación binaria (fraude)
   - ~285,000 transacciones
   - 30 features (PCA anónimas)
   - **MUY desbalanceado** (0.17% fraude)

4. **[Store Sales](https://www.kaggle.com/c/store-sales-time-series-forecasting)** ⭐⭐⭐⭐
   - Series temporales (ventas)
   - ~3 millones de registros
   - Múltiples tiendas y productos
   - Features: promociones, feriados

#### **Avanzado:**
5. **[Santander Customer Satisfaction](https://www.kaggle.com/c/santander-customer-satisfaction)** ⭐⭐⭐⭐
   - Clasificación binaria (satisfacción)
   - ~76,000 clientes
   - 369 features anónimas
   - Requiere feature selection

6. **[M5 Forecasting](https://www.kaggle.com/c/m5-forecasting-accuracy)** ⭐⭐⭐⭐⭐
   - Series temporales jerárquicas
   - ~30,000 series
   - Walmart sales forecasting
   - **Muy desafiante**

---

### UCI Machine Learning Repository

1. **[Iris](https://archive.ics.uci.edu/ml/datasets/iris)** ⭐
   - Clasificación multiclase (flores)
   - 150 muestras, 4 features
   - **Muy simple, ideal para probar código**

2. **[Wine Quality](https://archive.ics.uci.edu/ml/datasets/wine+quality)** ⭐⭐
   - Regresión o clasificación (calidad vino)
   - ~6,500 vinos
   - 11 features químicas

3. **[Adult Income](https://archive.ics.uci.edu/ml/datasets/adult)** ⭐⭐⭐
   - Clasificación binaria (ingreso >50K)
   - ~48,000 personas
   - Features: edad, educación, ocupación, etc.

4. **[Bike Sharing](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)** ⭐⭐⭐
   - Serie temporal (demanda de bicicletas)
   - ~17,000 observaciones (2 años)
   - Features: clima, día de semana, feriados

---

## 💡 RECOMENDACIONES POR OBJETIVO

### **Si quieres impresionar en entrevistas:**
✅ Credit Card Fraud (desbalanceado, técnicas avanzadas)  
✅ House Prices (feature engineering creativo)  
✅ Store Sales (series temporales complejas)

### **Si quieres aprender mucho:**
✅ M5 Forecasting (muy desafiante)  
✅ Santander (feature selection avanzado)  
✅ Proyecto propio con datos reales

### **Si tienes poco tiempo:**
✅ Titanic (simple, completo rápido)  
✅ Iris (muy simple, para probar pipelines)  
✅ Datasets del curso (ya conocidos)

### **Si quieres usar Deep Learning:**
✅ VIX (LSTM para series)  
✅ FinShield (redes densas)  
✅ MNIST (CNNs) - externo  
✅ IMDB Reviews (RNNs/Transformers) - externo

---

## 📚 INSPIRACIÓN: CASOS REALES EXITOSOS

### 1. Netflix Prize ($1M)
**Problema**: Recomendación de películas  
**Solución**: Ensemble de múltiples collaborative filtering  
**Mejora**: 10% sobre baseline  
**Lección**: Ensemble > modelo único

### 2. Kaggle Porto Seguro (2017)
**Problema**: Predicción de reclamos de seguros  
**Solución**: LightGBM + feature engineering  
**Lección**: Feature engineering > arquitectura compleja

### 3. Uber Demand Forecasting
**Problema**: Predecir demanda de viajes por zona  
**Solución**: LSTM + features externas (clima, eventos)  
**Lección**: Combinar temporal + features externas

---

## 🎯 TEMPLATE DE PROPUESTA DE PROYECTO

Usa este template para definir tu proyecto:

```markdown
# Propuesta de Proyecto Final

## 1. Título
[Nombre descriptivo del proyecto]

## 2. Problema de Negocio
[Descripción del problema en lenguaje de negocio]

## 3. Objetivo Cuantificable
[Métrica específica a optimizar]
Ejemplo: "Reducir el churn en 10%" o "Predecir ventas con MAPE < 15%"

## 4. Dataset
- **Fuente**: [Kaggle/UCI/Propio]
- **Tamaño**: X filas, Y columnas
- **Target**: [Variable a predecir]
- **Features**: [Principales variables]

## 5. Enfoque Técnico
- **Tipo de problema**: [Regresión/Clasificación/Clustering/Serie Temporal]
- **Algoritmos a probar**: [Lista de 3-5 modelos]
- **Métrica principal**: [MAE/RMSE/ROC-AUC/etc.]

## 6. Entregables
- [ ] Notebook de EDA
- [ ] Notebook de preprocesamiento
- [ ] Notebook de modelado
- [ ] Notebook de optimización
- [ ] Notebook de evaluación final
- [ ] README profesional

## 7. Cronograma
- **Semana 1**: EDA + Preprocesamiento
- **Semana 2**: Modelado + Optimización
- **Semana 3**: Evaluación + Documentación
```

---

## 📧 CONTACTO

**Dudas sobre datasets:**
- Revisa los notebooks originales en cada clase
- Pregunta en la clase de consulta (lunes próximo)
- Email: mariano.gobea@mercadolibre.com

---

**Última actualización**: Febrero 16, 2026

🚀 **¡Elige tu dataset y comienza tu proyecto!**
