# Guía de contribución

Este repositorio es material de una cursada de Data Science. Contribuciones bienvenidas, sobre todo si encontrás un error en un notebook o una consigna desactualizada.

## Reportar un error

Abrí un issue con:
- En qué clase/notebook está (`clase_XX/notebooks/nombre.ipynb`)
- Qué esperabas que pasara vs. qué pasó
- Si es un error de código: el traceback completo

## Proponer un cambio

1. Fork del repositorio
2. Rama descriptiva: `git checkout -b fix/clase-05-typo-en-metricas`
3. Cambios + commit: `git commit -m "Corrige cálculo de RMSE en clase 05"`
4. Push y Pull Request

## Reglas para tocar un notebook

Cada clase tiene **un único notebook** — esa es la regla central del repo (ver `ARCHITECTURE.md`). Si tu cambio agrega una sección nueva, que sea porque cubre algo que la consigna pide y que hoy falta, no porque "estaría bueno agregar". Si el notebook ya cubre lo obligatorio de `docs/homework.md` (o de la consigna del PI), no hace falta ampliarlo.

Para que un notebook sea aceptable en este repo tiene que ser:

- **Didáctico**: antes de cada celda de código, una celda de Markdown que explique qué hace y por qué — pensado para poder explicarse en vivo en clase, no solo para correrse.
- **Corto**: lo mínimo necesario para cubrir la parte obligatoria de la consigna. Si algo es "extra credit" u opcional en la consigna, no hace falta implementarlo (y si se implementa, que sea breve y quede claramente marcado como opcional).
- **Ejecutable de punta a punta**: corré `Kernel → Restart & Run All` antes de subirlo. Un notebook con celdas fuera de orden o con errores no se acepta.
- **Reproducible**: usá `random_state=42` (o el seed equivalente de la librería) en cualquier paso con aleatoriedad.
- **Sin rutas absolutas**: los datasets se cargan con rutas relativas (`../data/archivo.csv`), nunca con la ruta absoluta de tu máquina.

Si tu cambio es a un notebook de las clases que forman parte del Proyecto Integrador (03, 06, 08, 09 — ver `README.md`), respetá el nombre de archivo existente (`1_...`, `2_...`, `3_...`): es parte de la consigna, no un detalle de estilo.

## Actualizar documentación

Si tu cambio afecta la consigna, el dataset o el resultado principal de una clase, actualizá también el `README.md` de esa clase (una tabla o párrafo corto alcanza — no hace falta que sea extenso).
