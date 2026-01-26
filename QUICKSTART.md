# Guía de Inicio Rápido

Esta guía te ayudará a configurar el entorno y comenzar con el curso en pocos minutos.

## Prerequisitos

- Python 3.9 o superior
- Git (opcional, para control de versiones)
- 5-10 GB de espacio en disco

## Instalación

### Opción 1: Usando Poetry (Recomendado)

1. **Instalar Poetry**:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clonar o navegar al directorio**:
   ```bash
   cd data_science_henry
   ```

3. **Instalar dependencias**:
   ```bash
   poetry install
   ```

4. **Activar el entorno virtual**:
   ```bash
   poetry shell
   ```

### Opción 2: Usando pip y venv

1. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   ```

2. **Activar entorno**:
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Verificar Instalación

```python
# Ejecuta este código para verificar que todo funciona
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import torch

print("✓ NumPy:", np.__version__)
print("✓ Pandas:", pd.__version__)
print("✓ Scikit-learn:", sklearn.__version__)
print("✓ TensorFlow:", tf.__version__)
print("✓ PyTorch:", torch.__version__)
print("\n¡Todo instalado correctamente!")
```

## Iniciar JupyterLab

### Con Poetry:
```bash
poetry run jupyter lab
```

### Con venv:
```bash
jupyter lab
```

### Usando Makefile:
```bash
make jupyter
# o
make lab
```

## Estructura del Curso

El curso está organizado en 11 clases:

1. **Clase 01**: Introducción al ML
2. **Clase 02**: Regresión
3. **Clase 03**: Regresión Logística
4. **Clase 04**: Clasificación y Métricas
5. **Clase 05**: Modelos de Ensamble
6. **Clase 06**: Optimización de Modelos
7. **Clase 07**: Aprendizaje No Supervisado I
8. **Clase 08**: Aprendizaje No Supervisado II
9. **Clase 09**: Series Temporales
10. **Clase 10**: Deep Learning
11. **Clase 11**: Consulta

Cada clase contiene:
- 📓 `notebooks/` - Jupyter notebooks con teoría y práctica
- 🐍 `scripts/` - Scripts de Python reutilizables
- 📚 `docs/` - Documentación y material de lectura
- 📊 `data/` - Datasets específicos de la clase

## Flujo de Trabajo Recomendado

1. **Leer el README** de la clase
2. **Estudiar la documentación** en `docs/`
3. **Seguir los notebooks** en orden numérico
4. **Experimentar** modificando el código
5. **Resolver ejercicios** propuestos
6. **Revisar scripts** de utilidades

## Comandos Útiles

### Con Makefile:
```bash
make help       # Ver todos los comandos disponibles
make install    # Instalar dependencias
make test       # Ejecutar tests
make format     # Formatear código
make lint       # Verificar estilo de código
make clean      # Limpiar archivos temporales
```

### Con Poetry:
```bash
poetry add <package>        # Agregar nueva dependencia
poetry remove <package>     # Remover dependencia
poetry update               # Actualizar dependencias
poetry show                 # Ver dependencias instaladas
poetry run python script.py # Ejecutar script
```

## Configuración Opcional

### Variables de Entorno

Copia el archivo `.env.example` a `.env` y configura tus variables:

```bash
cp .env.example .env
```

Edita `.env` con tus preferencias:
```
RANDOM_STATE=42
N_JOBS=-1
LOG_LEVEL=INFO
```

### Jupyter Extensions

Para una mejor experiencia, instala extensiones útiles:

```bash
# Con Poetry
poetry run pip install jupyter-contrib-nbextensions
poetry run jupyter contrib nbextension install --user

# O con pip
pip install jupyter-contrib-nbextensions
jupyter contrib nbextension install --user
```

Extensiones recomendadas:
- Table of Contents (TOC)
- Variable Inspector
- ExecuteTime
- Code folding

## Troubleshooting

### Error: "Command not found: poetry"

Asegúrate de que Poetry esté en tu PATH. Reinicia tu terminal o agrega:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Error al importar TensorFlow

Si tienes problemas con TensorFlow:
```bash
# En Mac M1/M2
pip install tensorflow-macos
pip install tensorflow-metal
```

### Error al importar PyTorch

Visita [pytorch.org](https://pytorch.org/) y usa el selector para tu configuración específica.

### Jupyter Kernel no se encuentra

```bash
# Con Poetry
poetry run python -m ipykernel install --user --name=data-science-henry

# Con venv
python -m ipykernel install --user --name=data-science-henry
```

## Recursos Adicionales

- 📖 **Documentación**: Ver `README.md`
- 🤝 **Contribuir**: Ver `CONTRIBUTING.md`
- 📧 **Contacto**: mariano.gobea@mercadolibre.com

## Próximos Pasos

1. ✅ Verificar que la instalación funciona
2. ✅ Abrir JupyterLab
3. ✅ Navegar a `clase_01_introduccion_ml/notebooks/`
4. ✅ Abrir el primer notebook
5. ✅ ¡Comenzar a aprender!

---

¿Listo? ¡Abre tu primera clase con:

```bash
cd clase_01_introduccion_ml/notebooks/
jupyter lab 01_ejemplo_basico.ipynb
```

¡Disfruta el curso! 🚀📊🤖
