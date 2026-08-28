# Arquitectura del repositorio

**Última actualización**: Agosto 2026 — tras una simplificación completa del scaffolding.

## Principio de diseño

Este es un repositorio de **material de clase**, no un paquete de software. No hay código de producción, así que no tiene sentido tratarlo como uno: no hay `src/` instalable, no hay suite de tests, no hay linters obligatorios. Lo único que importa es que cada clase tenga **un notebook claro, corto y ejecutable** que resuelva su consigna.

## Estructura real

```
data_science_henry/
├── clase_01_introduccion_ml/
│   ├── presentations/   # Hands On (PDF) + Kick Off del módulo
│   ├── docs/            # actividad_clase.md, homework.md, resumen_contenidos.md
│   ├── data/            # retailboost_customers.csv
│   ├── notebooks/       # eda_retailboost.ipynb  (único)
│   └── README.md
│
├── clase_02_regresion/            → regresion_retailboost.ipynb
├── clase_03_regresion_logistica/  → 1_EDA_RegresionLogistica.ipynb   (PI avance 1)
├── clase_04_clasificacion_metricas/ → homework_clasificacion_leads_fintech.ipynb
├── clase_05_modelos_ensamble/     → homework_modelos_ensamble.ipynb
├── clase_06_optimizacion_modelos/ → 2_GradientBoosting_Optimizacion.ipynb (PI avance 2)
├── clase_07_aprendizaje_no_supervisado_i/  → clustering_mall_customers.ipynb
├── clase_08_aprendizaje_no_supervisado_ii/ → 3_AprendizajeNoSupervisado.ipynb (PI avance 3)
├── clase_09_series_temporales/    → series_temporales_cityscoot.ipynb (dataset simulado, ver nota)
├── clase_10_deep_learning/        → vix_lstm_didactico.ipynb
├── clase_11_consulta/
│   ├── docs/             # guía de datasets del curso + resumen completo de la cursada
│   └── notebooks/        # RESUMEN_TEMAS_CURSADA.ipynb
│
├── requirements.txt      # única fuente de dependencias (pip + venv)
├── Makefile               # 3 comandos: install, jupyter, clean
├── README.md / QUICKSTART.md / ARCHITECTURE.md / CONTRIBUTING.md
└── LICENSE
```

Cada carpeta `clase_XX/` sigue el mismo patrón — `presentations/` (teoría), `docs/` (consigna), `data/` (dataset), `notebooks/` (un único `.ipynb`) — salvo cuando una clase no lo necesita (p. ej. clase_11 no tiene `presentations/` ni `data/` propios, es repaso).

## Por qué se eliminó todo lo demás

Hasta agosto de 2026 el repo tenía además `src/`, `tests/`, `utils/`, un `data/` raíz vacío, `setup.py` y un `pyproject.toml` con configuración de `black`/`isort`/`pytest`/`mypy`. Se auditó el repo entero (`grep` de imports en todos los notebooks) y **ningún notebook importaba nada de `utils/` ni de los `scripts/` por clase**: era scaffolding de un template genérico de Python, nunca conectado al contenido real. Se eliminó porque:

- No cumplía ninguna función — no había paquete que instalar ni tests que correr.
- Agregaba fricción para nuevos colaboradores (¿tengo que mantener tests de algo que no existe?).
- Los `scripts/` de clase_01 y clase_02 tampoco los usaba ningún notebook — se eliminaron junto con los notebooks redundantes de esas clases.

Lo que sí se mantuvo: `.venv/` (entorno local del usuario), `requirements.txt` (simplificado a lo que realmente usan los notebooks: pandas, numpy, scikit-learn, xgboost, lightgbm, catboost, statsmodels, torch, openpyxl, optuna, jupyter).

## El hilo del Proyecto Integrador (PI)

Cuatro clases (03, 06, 08, 09) comparten un mismo caso de punta a punta — **FinanceGuard**, banco digital con problema de churn — sobre el dataset `Churn_Modelling.csv`. Cada avance construye sobre el anterior:

1. **Avance 1** (clase 03): regresión logística baseline → `1_EDA_RegresionLogistica.ipynb`
2. **Avance 2** (clase 06): boosting + tuning de XGBoost → `2_GradientBoosting_Optimizacion.ipynb`
3. **Avance 3** (clase 08): clustering para segmentar clientes → `3_AprendizajeNoSupervisado.ipynb`
4. **Avance 4 / cierre** (clase 09): no es un notebook, es un reporte que consolida los 3 avances anteriores → `clase_09_series_temporales/docs/Reporte_Modelos.md`

Estos nombres de archivo (`1_...`, `2_...`, `3_...`) son parte de la consigna del PI — no renombrarlos.

## Nota sobre clase_09: dataset simulado

El dataset original `cityscoot_daily_rides.csv` que pedía la consigna de la clase 09 no estaba en el repo (se perdió en algún punto y no quedó rastro en el historial de git). Se generó un dataset sintético equivalente (2 años de viajes diarios, con tendencia creciente + estacionalidad semanal + ruido, semilla fija `42`) para que el notebook de descomposición de series temporales sea ejecutable de punta a punta. Si en algún momento aparece el dataset real, basta con reemplazar el CSV — el notebook no depende de que los datos sean sintéticos.
