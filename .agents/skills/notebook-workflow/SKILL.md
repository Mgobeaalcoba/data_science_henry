---
name: notebook-workflow
description: >-
  Audita, inspecciona, modifica y re-ejecuta los Jupyter notebooks (.ipynb) de las 11 clases del repositorio
  sin saturar el contexto con imágenes base64. Usá esta skill siempre que debas revisar, editar, validar o
  ejecutar notebooks en data_science_henry.
---

# Flujo de Trabajo para Notebooks (`data_science_henry`)

Esta skill provee un script utilitario en [`.agents/skills/notebook-workflow/scripts/validate_notebooks.py`](./scripts/validate_notebooks.py) para inspeccionar celdas, auditar reglas pedagógicas/técnicas y re-ejecutar notebooks dentro del entorno `.venv`.

## 1. Inspeccionar un notebook sin cargar imágenes base64

Nunca leas un `.ipynb` crudo completo si tiene gráficos renderizados (las imágenes `image/png` en base64 consumen miles de tokens). En su lugar, ejecutá:

```bash
.venv/bin/python .agents/skills/notebook-workflow/scripts/validate_notebooks.py --inspect clase_03
```

Esto imprime todas las celdas (`[markdown]` y `[code]`) y los outputs de texto/tablas de forma compacta.

## 2. Auditar reglas pedagógicas y técnicas en los 11 notebooks

Para verificar que los notebooks cumplen las reglas de [`AGENTS.md`](../../../AGENTS.md):

```bash
.venv/bin/python .agents/skills/notebook-workflow/scripts/validate_notebooks.py --audit
```

El auditor comprueba automáticamente:
- Existencia de exactamente 1 notebook por clase (`clase_01` a `clase_11`).
- Ausencia de etiquetas residuales prohibidas (`#gemini`, `<!-- #gemini -->`).
- Ausencia de errores de ejecución (`output_type == "error"`) y advertencias en `stderr`.
- Que todas las celdas de código no vacías estén ejecutadas con `execution_count` secuencial (`1..N`) en los notebooks prácticos (`clase_01` a `clase_10`).
- Balance adecuado entre celdas Markdown y celdas de código, y cierre con sección de conclusión.

## 3. Re-ejecutar uno o todos los notebooks tras editarlos

Después de modificar un notebook, re-ejecutalo de punta a punta en su propio directorio (`clase_XX/notebooks/`) para que las rutas relativas `../data/...` funcionen y los outputs queden actualizados:

```bash
# Re-ejecutar una clase específica:
.venv/bin/python .agents/skills/notebook-workflow/scripts/validate_notebooks.py --execute clase_08

# Re-ejecutar todas las clases y auditar al finalizar:
.venv/bin/python .agents/skills/notebook-workflow/scripts/validate_notebooks.py --execute --audit
```

