# AGENTS.md — Guía Operativa y Reglas para Agentes de IA

Este documento contiene **todo el contexto estructural, esquemas de datos y reglas pedagógicas/técnicas** del repositorio `data_science_henry`. **Leé este archivo antes de explorar el repositorio**: no hace falta barrer todas las carpetas ni abrir los `.ipynb` crudos para saber qué hay en cada clase.

---

## 1. Propósito y Regla de Oro del Repositorio

Este es un repositorio de **material didáctico** para el curso de *Data Science y Machine Learning* (Henry, 11 clases). No es una librería de software ni tiene un paquete en `src/`.

- **Regla de Oro:** Existe **exactamente un notebook `.ipynb` por clase** (`clase_XX_.../notebooks/*.ipynb`).
- **Entorno Python:** Usar **siempre** el entorno virtual local `.venv` (`.venv/bin/python`, `.venv/bin/pip`, `.venv/bin/jupyter`). Nunca instalar paquetes en el Python global.
- **Herramienta de inspección y validación rápida:** Para auditar o re-ejecutar notebooks sin saturar la ventana de contexto con imágenes en base64, ejecutá:
  ```bash
  make audit          # Audita estructura, reglas pedagógicas, errores y outputs de los 11 notebooks
  make execute        # Re-ejecuta los 11 notebooks en .venv y valida 0 errores
  .venv/bin/python .agents/skills/notebook-workflow/scripts/validate_notebooks.py --inspect clase_03
  ```

---

## 2. Mapa Completo de Clases, Notebooks y Esquemas de Datasets

Cada clase `01` a `10` tiene las subcarpetas `data/`, `docs/`, `notebooks/`, `presentations/` y su `README.md`. La `clase_11_consulta` solo tiene `docs/`, `notebooks/` y `README.md`.

| Clase | Carpeta | Notebook único (`notebooks/`) | Dataset (`data/`) | Filas × Cols | Columnas exactas (`df.columns`) | Target y Tarea |
|---|---|---|---|---|---|---|
| **01** | `clase_01_introduccion_ml` | `eda_retailboost.ipynb` | `retailboost_customers.csv` | `500 × 6` | `customer_id`, `edad`, `ingresos_mensuales` *(15 nulos)*, `region` *(15 nulos)*, `frecuencia_visitas`, `compró` | `compró` (0/1) — Solo EDA y preprocesamiento sin *leakage* |
| **02** | `clase_02_regresion` | `regresion_retailboost.ipynb` | `retailboost_customers_regression.csv` | `500 × 7` | `customer_id`, `age`, `income`, `visits_per_month`, `satisfaction_score`, `membership_years`, `monthly_spent` | `monthly_spent` ($) — Regresión simple, múltiple, diagnóstico de residuos |
| **03** | `clase_03_regresion_logistica` | `1_EDA_RegresionLogistica.ipynb` *(PI Avance 1 — no renombrar)* | `Churn_Modelling.csv` | `10000 × 14` | `RowNumber`, `CustomerId`, `Surname`, `CreditScore`, `Geography`, `Gender`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`, `EstimatedSalary`, `Exited` | `Exited` (0/1, ~20.4% churn) — LogReg baseline, VIF, Odds Ratios + IC 95%, ajuste de umbral |
| **04** | `clase_04_clasificacion_metricas` | `homework_clasificacion_leads_fintech.ipynb` | `martech_homework_dataset_fixed.csv` | `1000 × 8` | `age`, `income`, `web_visits`, `clicked_ad`, `device_type`, `time_on_site`, `past_purchases`, `converted` | `converted` (0/1) — KNN vs. Decision Tree vs. SVM (foco en Recall y AUC) |
| **05** | `clase_05_modelos_ensamble` | `homework_modelos_ensamble.ipynb` | `ENB2012_data.xlsx` | `768 × 10` | `X1`..`X8` (renombradas a nombres de dominio edilicio), `Y1` (*Heating Load*), `Y2` (*Cooling Load*) | `Y1`, `Y2` (continuos) — Árbol vs. Random Forest vs. XGBoost (sesgo-varianza Train/Test) |
| **06** | `clase_06_optimizacion_modelos` | `2_GradientBoosting_Optimizacion.ipynb` *(PI Avance 2 — no renombrar)* | `Churn_Modelling.csv` | `10000 × 14` | Mismo esquema que Clase 03 | `Exited` (0/1) — LogReg baseline, RF, XGBoost, LightGBM, CatBoost, Stacking, GridSearch/RandomizedSearch en XGBoost |
| **07** | `clase_07_aprendizaje_no_supervisado_i` | `clustering_mall_customers.ipynb` | `Mall_Customers.csv` | `200 × 5` | `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, `Spending Score (1-100)` | Sin target — K-Means (`k=6` por silueta en 3D), Codo, Silueta, PCA 2D y vista 3D |
| **08** | `clase_08_aprendizaje_no_supervisado_ii` | `3_AprendizajeNoSupervisado.ipynb` *(PI Avance 3 — no renombrar)* | `Churn_Modelling.csv` | `10000 × 14` | Mismo esquema que Clases 03 y 06 | `Exited` usado solo *ex-post* — K-Means (`K=3`), DBSCAN (con curva k-NN), PCA (con *loadings*), t-SNE |
| **09** | `clase_09_series_temporales` | `series_temporales_cityscoot.ipynb` | `cityscoot_daily_rides.csv` *(sintético)* | `730 × 2` | `fecha`, `viajes` | `viajes` — Descomposición aditiva (`period=7`), ADF, ACF/PACF, Baselines de persistencia vs. ML con lags |
| **10** | `clase_10_deep_learning` | `vix_lstm_didactico.ipynb` | `econotrend_vix_sim.csv` | `1305 × 2` | `date`, `vix` | `vix` — PyTorch LSTM (`lookback=10`), `TimeSeriesSplit` sin *leakage*, curva Train/Val, comparación con Persistencia y Regresión Lineal |
| **11** | `clase_11_consulta` | `RESUMEN_TEMAS_CURSADA.ipynb` | — | — | — | Repaso integrador de las 10 clases, Cheat Sheet de pipelines sin *leakage* y guía del proyecto final |

---

## 3. Hilo Conductor del Proyecto Integrador (PI — FinanceGuard)

Las clases **03, 06, 08 y 09** conforman los 4 avances del Proyecto Integrador sobre **FinanceGuard** (`Churn_Modelling.csv`, 10.000 clientes bancarios, 20,37% de tasa de abandono en `Exited`):

1. **Avance 1 (`clase_03` → `1_EDA_RegresionLogistica.ipynb`):** Descarta `RowNumber`, `CustomerId`, `Surname`. One-Hot Encoding (`drop="first"`) para `Geography` y `Gender`; `StandardScaler` para las 6 continuas (`CreditScore`, `Age`, `Tenure`, `Balance`, `NumOfProducts`, `EstimatedSalary`); `HasCrCard` e `IsActiveMember` quedan en `0/1`. Diagnóstico VIF, Odds Ratios con IC 95% (`statsmodels`), matriz de confusión, ROC-AUC (~0.77–0.84) y optimización de umbral / `class_weight="balanced"`.
2. **Avance 2 (`clase_06` → `2_GradientBoosting_Optimizacion.ipynb`):** Compara bajo la misma partición (`test_size=0.2, stratify=y, random_state=42`) y `StratifiedKFold(n_splits=5)` el baseline de Regresión Logística contra Random Forest, XGBoost, LightGBM, CatBoost y `StackingClassifier` (meta-learner `LogisticRegression`). Optimiza hiperparámetros únicamente sobre XGBoost (`GridSearchCV` y `RandomizedSearchCV`), reporta ROC-AUC y PR-AUC, y analiza la importancia de variables.
3. **Avance 3 (`clase_08` → `3_AprendizajeNoSupervisado.ipynb`):** Entrena clustering **sin usar `Exited`**. Selecciona **`K=3`** en K-Means (óptimo según coeficiente de silueta), compara con DBSCAN (usando gráfico de distancias k-NN para elegir `eps`), proyecta con PCA (interpretando varianza explicada y *loadings*) y t-SNE, y finalmente cruza los clusters con `Exited` identificando el segmento de mayor riesgo (~32.4% de churn en Alemania / balance alto).
4. **Avance 4 (`clase_09/docs/Reporte_Modelos.md`):** Documento técnico de cierre (no es un notebook) que consolida las métricas y recomendaciones de los Avances 1, 2 y 3. Cualquier cambio en las métricas o en `K` de las clases 03, 06 u 08 debe mantenerse coherente con este reporte.

---

## 4. Reglas Pedagógicas y de Estilo (Obligatorias)

1. **Narrativa "Antes y Después" de cada bloque de código:**
   - **Antes** de cada celda de código debe existir una celda Markdown que explique **qué** se va a hacer, **por qué** se hace de esa manera y **qué mirar** en la salida.
   - **Después** de salidas analíticas clave (tablas de métricas, matrices de confusión, test estadísticos, gráficos de residuos o clustering), debe incluirse una breve lectura interpretativa de los números reales obtenidos.
2. **Estructura lineal con una única Conclusión:**
   - Cada notebook debe fluir de principio a fin y cerrar con **una única sección de Conclusión** conectada con el problema de negocio.
   - **PROHIBIDO** agregar apéndices post-conclusión, celdas sueltas que contradigan celdas previas, o marcas de agua/comentarios de agente como `#gemini`, `#claude`, `#todo`, etc.
3. **Idioma y ortografía:**
   - Español claro y didáctico, con **tildes y puntuación completas** tanto en celdas Markdown como en títulos/ejes de gráficos y comentarios de código.

---

## 5. Reglas de Código y Buenas Prácticas de Machine Learning

1. **Cero Data Leakage (Estrictamente vigilado):**
   - En aprendizaje supervisado, dividir siempre en `train` y `test` **antes** de imputar valores faltantes, codificar categóricas o escalar numéricas.
   - Ajustar transformadores (`fit` / `fit_transform`) **exclusivamente sobre `train`** y aplicar solo `transform` sobre `test` (preferiblemente encapsulado en `sklearn.pipeline.Pipeline` y `ColumnTransformer`).
   - En series temporales (`clase_09`, `clase_10`), dividir siempre de forma **cronológica** (`shuffle=False`). En `TimeSeriesSplit`, instanciar y ajustar un `Scaler` nuevo **dentro de cada fold** usando solo los índices de `train` de ese fold.
2. **Tratamiento correcto por tipo de variable:**
   - Variables identificadoras (`customer_id`, `CustomerID`, `RowNumber`, `CustomerId`, `Surname`) deben descartarse antes de modelar.
   - Variables binarias (`0/1` como `clicked_ad`, `HasCrCard`, `IsActiveMember`) no deben pasarse por `StandardScaler` cuando se busca preservar la interpretación de coeficientes o no distorsionar distancias; dejarlas como `"passthrough"`.
3. **Comparación justa de modelos y Baselines:**
   - Todo problema supervisado o de series temporales debe incluir un **baseline explícito** (media en regresión, clase mayoritaria/regresión logística en clasificación, persistencia $y_{t-1}$ o estacional $y_{t-7}$ en series temporales) evaluado sobre **exactamente las mismas observaciones de `test`** que el resto de los modelos.
   - Reportar métricas en `train` y `test` (o media ± desvío en CV) cuando se discuta sobreajuste (*overfitting*) o el trade-off sesgo-varianza.
4. **Reproducibilidad y limpieza de ejecución:**
   - Definir `RANDOM_STATE = 42` al inicio del notebook y pasarlo a todos los estimadores, splits, `KMeans(..., n_init=10)` y semillas (`np.random.seed(42)`, `torch.manual_seed(42)`).
   - Al modificar cualquier celda de un `.ipynb`, **re-ejecutar el notebook completo** (`make execute` o script de validación) para garantizar que los `execution_count` sean correlativos (`1..N`) y que los outputs coincidan con el código sin errores ni warnings.

