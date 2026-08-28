# ⚡ Guía de inicio rápido

## Requisitos

- Python 3.9+ (recomendado 3.12)
- ~3 GB de espacio en disco (las librerías de ML/DL pesan, sobre todo PyTorch)
- Conexión a internet para instalar dependencias

## Instalación

### Opción 1 — con Makefile

```bash
cd data_science_henry
make install                  # crea .venv e instala requirements.txt
source .venv/bin/activate
make jupyter                  # levanta JupyterLab
```

### Opción 2 — manual

```bash
cd data_science_henry
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

## Cómo usar el repo

1. Cada clase es independiente — no hace falta correrlas en orden para que funcionen, aunque el curso está pensado para seguirse 01 → 11.
2. Entrá a `clase_XX_tema/notebooks/` y abrí el único `.ipynb` de esa clase.
3. Antes de correr código, mirá `clase_XX_tema/docs/` — ahí está la consigna original que el notebook resuelve.
4. Cada notebook está escrito para leerse: la celda de Markdown antes de cada bloque de código explica qué hace y por qué. Corré celda por celda, no todo de una.
5. Los datasets ya están en `clase_XX_tema/data/` — ningún notebook descarga nada externo (clase_09 usa un dataset simulado, ver su README).

## Si algo no corre

- Revisá que activaste el `.venv` (`which python` debería apuntar a `.venv/bin/python`).
- Revisá que instalaste `requirements.txt` completo — algunas clases usan librerías pesadas (PyTorch en clase 10, XGBoost/LightGBM/CatBoost en clases 05/06).
- Cada notebook fija `random_state=42` (o `torch.manual_seed`) para que los resultados sean reproducibles — si algo da distinto, revisá que no se haya salteado una celda.

## Siguiente paso

Ver [`README.md`](README.md) para el mapa completo de las 11 clases, o [`ARCHITECTURE.md`](ARCHITECTURE.md) para el detalle de cómo está organizado el repo.
