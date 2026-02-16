# ⚡ Guía de Inicio Rápido
## Empieza a aprender en 5 minutos

**Última actualización**: Febrero 2026

---

## ✅ Requisitos Previos

- Python 3.9 o superior (recomendado: 3.12)
- 5-10 GB de espacio en disco
- Git (opcional, para control de versiones)
- Conexión a internet (para instalar dependencias)

---

## 🚀 Instalación en 4 Pasos

### **Opción 1: Poetry** (Recomendado por gestión automática)

```bash
# Paso 1: Instalar Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Paso 2: Navegar al proyecto
cd data_science_henry

# Paso 3: Instalar TODAS las dependencias
poetry install

# Paso 4: Activar entorno
poetry shell

# ✅ Listo! Ahora ejecuta:
jupyter lab
```

### **Opción 2: pip + venv** (Más simple, control manual)

```bash
# Paso 1: Crear entorno virtual
python -m venv .venv

# Paso 2: Activar entorno
source .venv/bin/activate      # Mac/Linux
# o
.venv\Scripts\activate         # Windows

# Paso 3: Instalar dependencias
pip install -r requirements.txt

# Paso 4: Instalar kernel de Jupyter
python -m ipykernel install --user --name=data-science-henry

# ✅ Listo! Ahora ejecuta:
jupyter lab
```

---

## 🧪 Verificar Instalación

### Test rápido en Python:

```python
# Copia y pega este código en un notebook o terminal Python
import numpy as np
import pandas as pd
import sklearn
import torch
import matplotlib

print("✅ NumPy:", np.__version__)
print("✅ Pandas:", pd.__version__)
print("✅ Scikit-learn:", sklearn.__version__)
print("✅ PyTorch:", torch.__version__)
print("✅ Matplotlib:", matplotlib.__version__)
print("\n🎉 ¡Todo instalado correctamente!")
```

**Versiones esperadas**:
- NumPy: 1.26.4
- Pandas: 2.3.3
- PyTorch: 2.2.2
- Scikit-learn: 1.5.2

---

## 📚 Iniciar JupyterLab

### Con Poetry:
```bash
poetry run jupyter lab
# o
poetry shell
jupyter lab
```

### Con venv:
```bash
# Asegúrate de tener el entorno activado
jupyter lab
```

### Con Makefile (Atajos):
```bash
make jupyter    # Inicia JupyterLab
# o
make lab        # Alias de lo anterior
```

JupyterLab se abrirá automáticamente en tu navegador en `http://localhost:8888`

---

## 🎯 Primer Notebook

### Ruta sugerida:

```bash
cd clase_01_introduccion_ml/notebooks/
jupyter lab resumen_actividad_clase_01.ipynb
```

### Orden de estudio:

1. **Clase 01**: EDA de RetailBoost
   - `resumen_actividad_clase_01.ipynb`
   - `actividad_clase_01_eda_retailboost.ipynb`
   
2. **Clase 02**: Regresión
   - `actividad_clase_02_presentacion.ipynb`
   - `actividad_clase_02_regresion_retailboost.ipynb`
   
3. **... y así sucesivamente hasta clase 10**

---

## 🗺️ Estructura del Curso

| Clase | Tema | Notebooks | Datasets | Duración |
|-------|------|-----------|----------|----------|
| 01 | Introducción al ML | 3 | 5 | 3h |
| 02 | Regresión | 3 | 1 | 3h |
| 03 | Regresión Logística | 2 | 1 | 3h |
| 04 | Clasificación y Métricas | 1 | 1 | 3h |
| 05 | Modelos de Ensamble | 1 | 0 | 3h |
| 06 | Optimización de Modelos | 3 | 0 | 3h |
| 07 | Clustering | 2 | 3 | 3h |
| 08 | Recomendaciones | 2 | 4 | 3h |
| 09 | Series Temporales | 2 | 1 | 3h |
| 10 | Deep Learning ⭐ | 4 | 2 | 4h |
| 11 | Consulta | 0 | 0 | 2h |

**Duración total**: ~32 horas de contenido práctico

---

## 🛠️ Comandos Útiles (Con Makefile)

```bash
make help       # Ver todos los comandos disponibles
make install    # Instalar dependencias
make test       # Ejecutar tests
make format     # Formatear código (black)
make lint       # Verificar estilo (flake8)
make clean      # Limpiar archivos temporales (__pycache__, .ipynb_checkpoints)
```

---

## 🔧 Troubleshooting

### Error: "Command not found: poetry"

Poetry no está en tu PATH. Solución:

```bash
# Mac/Linux: Agregar a ~/.bashrc o ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Reinicia terminal
source ~/.bashrc
```

### Error al importar PyTorch

Visita [pytorch.org](https://pytorch.org/get-started/locally/) y usa el selector para tu configuración:
- **Sistema operativo**: Mac / Windows / Linux
- **Package**: Pip / Conda
- **Compute platform**: CPU / CUDA 11.8 / CUDA 12.1

### Jupyter Kernel no aparece

```bash
# Con Poetry
poetry run python -m ipykernel install --user --name=ds-henry

# Con venv
python -m ipykernel install --user --name=ds-henry
```

Luego en Jupyter: Kernel → Change Kernel → ds-henry

### JupyterLab no se lanza

```bash
# Verificar que está instalado
jupyter --version

# Si no está, instalar:
poetry add jupyterlab
# o
pip install jupyterlab
```

---

## 📈 Progreso Sugerido

### Semana 1-2: Fundamentos
- ✅ Clase 01: Introducción
- ✅ Clase 02: Regresión
- ✅ Clase 03: Regresión Logística
- ✅ Clase 04: Clasificación

### Semana 3-4: Modelos Avanzados
- ✅ Clase 05: Ensambles
- ✅ Clase 06: Optimización

### Semana 5-6: No Supervisado
- ✅ Clase 07: Clustering
- ✅ Clase 08: Recomendaciones

### Semana 7-8: Avanzado
- ✅ Clase 09: Series Temporales
- ✅ Clase 10: Deep Learning
- ✅ Clase 11: Consulta y proyecto

---

## 🎓 Recursos Externos

### Documentación Oficial
- [Scikit-learn](https://scikit-learn.org/stable/)
- [PyTorch](https://pytorch.org/docs/)
- [Pandas](https://pandas.pydata.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)

### Tutoriales Interactivos
- [Kaggle Learn](https://www.kaggle.com/learn)
- [DataCamp](https://www.datacamp.com/)
- [Fast.ai](https://www.fast.ai/)

### Comunidades
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [PyTorch Forums](https://discuss.pytorch.org/)
- [Data Science Stack Exchange](https://datascience.stackexchange.com/)

---

## ⚙️ Configuración Opcional

### Variables de Entorno

```bash
# Copiar template
cp .env.example .env

# Editar .env con tus preferencias
RANDOM_STATE=42
N_JOBS=-1              # Usar todos los cores
LOG_LEVEL=INFO
```

### Jupyter Extensions (Opcional)

```bash
# Extensiones útiles
poetry run pip install jupyter-contrib-nbextensions
poetry run jupyter contrib nbextension install --user

# Extensiones recomendadas:
# - Table of Contents (TOC)
# - Variable Inspector
# - ExecuteTime
# - Code Folding
```

---

## 🚦 Próximos Pasos

1. ✅ Verificar instalación (ejecutar script de verificación arriba)
2. ✅ Lanzar JupyterLab
3. ✅ Abrir `clase_01_introduccion_ml/notebooks/resumen_actividad_clase_01.ipynb`
4. ✅ Ejecutar todas las celdas (Run → Run All Cells)
5. ✅ Leer los comentarios y experimentar
6. ✅ Continuar con el resto de las clases en orden

---

## 💡 Tips para el Éxito

1. **No saltes clases**: El curso es progresivo
2. **Ejecuta TODO el código**: No solo leas, practica
3. **Experimenta**: Cambia parámetros y observa qué pasa
4. **Documenta**: Agrega tus propios comentarios
5. **Pregunta**: Usa la clase 11 para resolver dudas

---

**¿Listo? ¡Ejecuta tu primer notebook!** 🚀

```bash
cd clase_01_introduccion_ml/notebooks/
jupyter lab resumen_actividad_clase_01.ipynb
```

---

**Problemas?** → Revisa la sección de Troubleshooting o contacta: mariano.gobea@mercadolibre.com

¡Disfruta el curso! 📊🤖🎉
