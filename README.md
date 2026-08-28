# 🎓 Curso de Data Science y Machine Learning — Henry
## Del ML clásico al Deep Learning, en 11 clases

**Instructor**: Mariano Gobea
**Última actualización**: Agosto 2026

---

## Cómo está organizado

Cada clase vive en su propia carpeta `clase_XX_tema/` con esta estructura:

```
clase_XX_tema/
├── presentations/   # el PPT/PDF de la clase (teoría)
├── docs/            # la consigna de la actividad/homework en Markdown
├── data/            # el o los datasets que usa el notebook
├── notebooks/       # UN ÚNICO notebook .ipynb: la resolución didáctica
└── README.md        # qué cubre esa clase, en 1 minuto de lectura
```

**Regla del repo: un notebook por clase.** Cada notebook está escrito para poder explicarse en vivo — antes de cada bloque de código hay una celda de Markdown que responde *qué* vamos a hacer y *por qué*, y qué mirar en el resultado. Están pensados para ser cortos: cubren lo **obligatorio** de la consigna de esa clase, no todo lo que podría hacerse.

## Las 11 clases

| # | Clase | Caso de negocio | Dataset | Notebook |
|---|---|---|---|---|
| 01 | Introducción al ML | RetailBoost — EDA para un futuro clasificador de compra | `retailboost_customers.csv` | `eda_retailboost.ipynb` |
| 02 | Regresión | RetailBoost — predecir gasto mensual | `retailboost_customers_regression.csv` | `regresion_retailboost.ipynb` |
| 03 | Regresión logística | FinanceGuard — baseline de churn bancario *(PI, avance 1)* | `Churn_Modelling.csv` | `1_EDA_RegresionLogistica.ipynb` |
| 04 | Clasificación y métricas | Fintech — scoring de leads (KNN, Árbol, SVM) | `martech_homework_dataset_fixed.csv` | `homework_clasificacion_leads_fintech.ipynb` |
| 05 | Modelos de ensamble | Eficiencia energética de edificios (RF vs. XGBoost) | `ENB2012_data.xlsx` | `homework_modelos_ensamble.ipynb` |
| 06 | Optimización de modelos | FinanceGuard — boosting + tuning *(PI, avance 2)* | `Churn_Modelling.csv` | `2_GradientBoosting_Optimizacion.ipynb` |
| 07 | Aprendizaje no supervisado I | Mall Customers — segmentación con K-Means | `Mall_Customers.csv` | `clustering_mall_customers.ipynb` |
| 08 | Aprendizaje no supervisado II | FinanceGuard — clustering de clientes *(PI, avance 3)* | `Churn_Modelling (1).csv` | `3_AprendizajeNoSupervisado.ipynb` |
| 09 | Series temporales | CityScoot — descomposición de viajes diarios | `cityscoot_daily_rides.csv` *(simulado)* | `series_temporales_cityscoot.ipynb` |
| 10 | Introducción al Deep Learning | EconoTrend — predicción del VIX con LSTM en PyTorch | `econotrend_vix_sim.csv` | `vix_lstm_didactico.ipynb` |
| 11 | Consulta | Repaso general de la cursada, sin homework propio | — | `RESUMEN_TEMAS_CURSADA.ipynb` |

### El hilo del Proyecto Integrador (PI)

Las clases **03, 06, 08 y 09** son, además, los 4 avances de un mismo Proyecto Integrador sobre **FinanceGuard** (un banco digital con 20% de abandono anual de clientes). Por eso esos notebooks tienen nombres numerados (`1_...`, `2_...`, `3_...`) — es la consigna del PI, no los renombres. El cierre del PI es un reporte (no un notebook): `clase_09_series_temporales/docs/Reporte_Modelos.md`.

## Instalación

Ver [`QUICKSTART.md`](QUICKSTART.md) para la guía paso a paso. Resumen:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Más documentación

- [`QUICKSTART.md`](QUICKSTART.md) — instalación y primeros pasos
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — estructura de carpetas en detalle
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — cómo reportar errores o proponer mejoras

## Licencia

MIT — ver [`LICENSE`](LICENSE).
