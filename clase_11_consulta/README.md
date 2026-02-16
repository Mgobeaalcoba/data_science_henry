# 🎓 Clase 11: Consulta y Repaso Pre-Proyecto Final

**Fecha**: Lunes próximo  
**Duración**: 2 horas  
**Modalidad**: Consulta abierta + Repaso estructurado

---

## 🎯 Objetivos de esta Clase

1. ✅ **Repasar** conceptos clave de las 10 clases anteriores
2. ✅ **Resolver dudas** específicas antes del proyecto final
3. ✅ **Proporcionar guías** para abordar el proyecto exitosamente
4. ✅ **Compartir mejores prácticas** y errores comunes a evitar
5. ✅ **Q&A abierto** sobre cualquier tema del curso

**Esta clase NO introduce contenido nuevo**. Todo es repaso y consulta.

---

## 📚 Material Preparado

### En `notebooks/`:

#### **📓 RESUMEN_TEMAS_CURSADA.ipynb** ⭐
Notebook completo de repaso con:
- Resumen de los 4 módulos del curso
- Fórmulas y conceptos clave por clase
- Código esencial (cheat sheets)
- Templates listos para usar
- Errores comunes y cómo evitarlos
- Guía paso a paso para el proyecto final

**Cómo usar**: Ábrelo en Jupyter y síguelo durante la clase.

---

### En `data/`:

#### **📊 RESUMEN_COMPLETO_CURSADA.md** ⭐
Documento maestro con:
- Estadísticas de lo aprendido (25+ algoritmos, 20+ métricas)
- Resumen detallado de cada clase
- Checklist de habilidades adquiridas
- Guía completa para el proyecto final
- Consejos para presentación y evaluación

**Cómo usar**: Documento de referencia durante el proyecto.

---

#### **📋 DATASETS_Y_CASOS.md**
Catálogo completo de todos los datasets:
- 20 datasets del curso descritos
- Tabla comparativa (filas, tipo, dificultad)
- Casos de uso por algoritmo
- Datasets externos recomendados (Kaggle, UCI)
- Template de propuesta de proyecto

**Cómo usar**: Para elegir dataset del proyecto o inspirarte.

---

## 📋 Agenda de la Clase

### Parte 1: Repaso Estructurado (60 min)

**Módulo 1: Fundamentos** (15 min)
- Regresión y clasificación básica
- Métricas fundamentales
- Preprocesamiento

**Módulo 2: Avanzado** (15 min)
- Ensambles (Bagging, Boosting)
- Optimización (Grid Search, Optuna)

**Módulo 3: No Supervisado** (15 min)
- Clustering (K-Means, DBSCAN)
- Recomendaciones

**Módulo 4: Series Temporales y DL** (15 min)
- ARIMA, Prophet
- LSTM en PyTorch
- Caso VIX: Lecciones aprendidas

### Parte 2: Proyecto Final (30 min)

- Estructura sugerida
- Checklist de entregables
- Criterios de evaluación
- Errores comunes a evitar
- Datasets recomendados

### Parte 3: Q&A Abierto (30 min)

- Dudas específicas
- Problemas técnicos
- Discusión de enfoques
- Revisión de propuestas (si traen)

---

## 🎯 PROYECTO FINAL: Requisitos Mínimos

### **Estructura Obligatoria:**

1. **📓 Notebooks**:
   - `01_eda.ipynb` - Análisis exploratorio
   - `02_preprocessing.ipynb` - Limpieza y transformaciones
   - `03_modeling.ipynb` - Al menos 3 modelos diferentes
   - `04_evaluation.ipynb` - Métricas y comparación

2. **📄 Documentación**:
   - `README.md` - Descripción, instalación, ejecución
   - `requirements.txt` - Dependencias

3. **📊 Datos**:
   - Dataset(s) en carpeta `data/`
   - Documentar origen y licencia

---

### **Criterios de Evaluación:**

| Aspecto | Peso | Qué se evalúa |
|---------|------|---------------|
| **Definición del problema** | 10% | Claridad, relevancia de negocio |
| **EDA** | 20% | Profundidad, visualizaciones, insights |
| **Preprocesamiento** | 10% | Justificación de decisiones |
| **Modelado** | 25% | Al menos 3 modelos, baseline incluido |
| **Evaluación** | 15% | Métricas apropiadas, validación cruzada |
| **Optimización** | 10% | Tuning de hyperparámetros |
| **Interpretabilidad** | 5% | Feature importance mínimo |
| **Conclusiones** | 10% | Recomendaciones de negocio |
| **Documentación** | 5% | README, comentarios, reproducibilidad |

**Total**: 110% (hay 10% de bonus en interpretabilidad)

---

## ✅ CHECKLIST PRE-ENTREGA

Verifica que tu proyecto cumple:

### Código
- [ ] Todos los notebooks ejecutan sin errores
- [ ] Seeds fijas (reproducibilidad)
- [ ] Imports al inicio de cada notebook
- [ ] Código comentado (especialmente decisiones importantes)
- [ ] No hay "magic numbers" (usar constantes)

### Datos
- [ ] Train/test split documentado
- [ ] No hay data leakage (normalización después de split)
- [ ] Faltantes manejados y justificado cómo
- [ ] Outliers analizados (eliminar o no, justificado)

### Modelos
- [ ] Mínimo 3 modelos diferentes
- [ ] Baseline simple incluido (Linear Regression o Persistencia)
- [ ] Validación cruzada (K-Fold con k≥5)
- [ ] Comparación de modelos en tabla

### Métricas
- [ ] Métricas apropiadas al problema
- [ ] Train Y test scores reportados
- [ ] Comparación con baseline
- [ ] Interpretación de resultados (no solo números)

### Visualizaciones
- [ ] Gráficos con títulos y labels
- [ ] Distribuciones del target
- [ ] Correlaciones importantes
- [ ] Curva de aprendizaje (si aplica)
- [ ] Matriz de confusión (si clasificación)

### Documentación
- [ ] README.md con:
  - Descripción del problema
  - Instrucciones de instalación
  - Cómo ejecutar el código
  - Resultados principales
- [ ] Conclusiones de negocio (no solo técnicas)
- [ ] Limitaciones reconocidas
- [ ] Próximos pasos sugeridos

---

## 💬 PREGUNTAS FRECUENTES

### **"¿Puedo usar un dataset del curso?"**

✅ **Sí**, perfectamente válido. Sugerimos:
- RetailBoost (regresión)
- Churn Bancario (clasificación)
- ShopSense (clustering + recomendaciones)
- CityScoot (series temporales)

Ventaja: Ya conoces los datos, puedes enfocarte en modelado.

---

### **"¿Debo usar Deep Learning?"**

❌ **No es obligatorio**. Deep Learning es apropiado si:
- Tienes >10,000 observaciones
- El problema es muy complejo (no lineal)
- Tienes GPU disponible
- Quieres experimentar con PyTorch

✅ **Para la mayoría de proyectos**: XGBoost/Random Forest es suficiente y a veces superior.

---

### **"¿Cuántos modelos debo probar?"**

**Mínimo**: 3 modelos diferentes + 1 baseline

**Ejemplos de combinaciones:**

**Para Clasificación:**
1. Baseline: Logistic Regression
2. Random Forest
3. XGBoost
4. SVM (opcional)

**Para Regresión:**
1. Baseline: Linear Regression
2. Ridge/Lasso
3. Random Forest
4. XGBoost

**Para Series Temporales:**
1. Baseline: Persistencia (ŷ_t = y_{t-1})
2. ARIMA/SARIMA
3. Prophet
4. XGBoost con lags
5. LSTM (opcional)

---

### **"¿Cómo sé si mi modelo es bueno?"**

**Compara con baseline:**
- Si no superas baseline → modelo no está aprendiendo
- Mejora de 1-5% → bueno
- Mejora de 5-15% → muy bueno
- Mejora de 15%+ → excelente (o posible data leakage, verificar)

**Compara con literatura:**
- Busca en Kaggle/papers problemas similares
- Ve qué métricas logran otros
- Tu modelo debe estar en el rango

**Ejemplo**:
- Titanic: Accuracy típico = 78-82%
- Si logras 85% → Excelente
- Si logras 95% → Revisa data leakage

---

### **"¿Cuánto tiempo debería tomar?"**

**Estimación realista:**

| Fase | Días | Horas |
|------|------|-------|
| Selección y EDA | 2-3 | 6-9h |
| Preprocesamiento | 1-2 | 3-6h |
| Modelado | 2-3 | 6-9h |
| Optimización | 1-2 | 3-6h |
| Interpretabilidad | 1 | 3h |
| Documentación | 1 | 3h |
| **TOTAL** | **8-12 días** | **24-36h** |

**Recomendación**: Empieza YA, no esperes al último día.

---

## 📅 CRONOGRAMA SUGERIDO

**Hoy (después de esta clase)**:
- Elegir dataset
- Definir problema
- Crear estructura de carpetas

**Esta semana (Lun-Vie)**:
- EDA completo
- Baseline implementado
- Preprocesamiento terminado

**Próxima semana**:
- Modelos avanzados
- Optimización
- Evaluación

**3 días antes de entrega**:
- Interpretabilidad
- Visualizaciones finales
- Documentación

**1 día antes**:
- Revisión final
- Código limpio
- README profesional

---

## 🔗 ENLACES ÚTILES

### Documentación del Curso
- [README Principal](../README.md)
- [QUICKSTART](../QUICKSTART.md)
- [ARCHITECTURE](../ARCHITECTURE.md)

### Material de Esta Clase
- [Notebook Resumen](./notebooks/RESUMEN_TEMAS_CURSADA.ipynb)
- [Resumen Completo Cursada](./data/RESUMEN_COMPLETO_CURSADA.md)
- [Datasets y Casos](./data/DATASETS_Y_CASOS.md)

### Clase 10 (Ejemplo de Proyecto Ejemplar)
- [Notebook VIX-LSTM](../clase_10_deep_learning/notebooks/homework_vix_lstm_completo_didactico.ipynb)
- [Análisis Completo](../clase_10_deep_learning/docs/ANALISIS_COMPLETO_VIX_LSTM.md)
- [Lecturas Recomendadas](../clase_10_deep_learning/docs/LECTURAS_RECOMENDADAS_VIX_LSTM.md)

---

## 💡 MENSAJE FINAL

### Has aprendido:
- ✅ 25+ algoritmos de ML/DL
- ✅ 20+ métricas de evaluación
- ✅ Scikit-learn, XGBoost, PyTorch
- ✅ Preprocesamiento, EDA, feature engineering
- ✅ Validación, optimización, interpretabilidad

### Ahora puedes:
- ✅ Resolver problemas reales de Data Science
- ✅ Construir pipelines completos de ML
- ✅ Elegir el algoritmo apropiado para cada problema
- ✅ Evaluar e interpretar resultados correctamente

### Para el proyecto:
- 🎯 Empieza simple (baseline)
- 🎯 Documenta decisiones
- 🎯 Compara modelos
- 🎯 Piensa en negocio (no solo técnica)

---

## 📧 CONTACTO

**Instructor**: Mariano Gobea  
**Email**: mariano.gobea@mercadolibre.com  
**Consultas**: Durante la clase del lunes o por email

---

## 🎉 ¡ÉXITO EN TU PROYECTO FINAL!

**Nos vemos el lunes para resolver tus dudas.** 🚀

---

**Última actualización**: Febrero 16, 2026
