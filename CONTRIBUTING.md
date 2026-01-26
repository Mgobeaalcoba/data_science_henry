# Guía de Contribución

Gracias por tu interés en contribuir al curso de Data Science y Machine Learning.

## Cómo Contribuir

### Reportar Errores

Si encuentras un error en el código, documentación o notebooks:

1. Verifica que el error no haya sido reportado anteriormente
2. Abre un nuevo issue con:
   - Descripción clara del error
   - Pasos para reproducirlo
   - Comportamiento esperado vs. comportamiento actual
   - Capturas de pantalla si aplica
   - Entorno (Python version, OS, etc.)

### Sugerir Mejoras

Para sugerir nuevas features o mejoras:

1. Abre un issue describiendo:
   - La mejora propuesta
   - Por qué sería útil
   - Cómo se implementaría (opcional)

### Contribuir con Código

1. **Fork** el repositorio
2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Realiza tus cambios**
4. **Commitea** tus cambios:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
5. **Push** a tu fork:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
6. **Abre un Pull Request**

## Estándares de Código

### Python

- Usar **PEP 8** para estilo de código
- Usar **type hints** cuando sea posible
- Docstrings en formato **Google** o **NumPy**
- Nombres descriptivos de variables y funciones

```python
def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """
    Calcula métricas de evaluación para un modelo.

    Args:
        y_true: Valores reales
        y_pred: Valores predichos

    Returns:
        Diccionario con métricas calculadas
    """
    pass
```

### Notebooks

- Título claro en el primer markdown cell
- Secciones bien organizadas
- Comentarios explicativos en el código
- Output limpio (no dejar outputs de debugging)
- Ejecutar todas las celdas antes de commitear

### Estructura de Commits

- Usar mensajes descriptivos en imperativo
- Una funcionalidad por commit cuando sea posible

```bash
# Bueno
git commit -m "Agrega función para calcular RMSE"
git commit -m "Corrige error en preprocessing de datos"

# Malo
git commit -m "Updates"
git commit -m "Fix bug"
```

## Testing

Si agregas nueva funcionalidad:

1. Agrega tests en el directorio `tests/`
2. Asegúrate que los tests pasen:
   ```bash
   poetry run pytest
   ```

## Documentación

Al agregar nuevas funciones o módulos:

1. Actualiza el README si es necesario
2. Agrega docstrings completas
3. Actualiza documentación en `docs/` si aplica

## Code Review

Todos los PRs serán revisados. Por favor:

- Responde a los comentarios
- Realiza los cambios solicitados
- Mantén la discusión profesional y constructiva

## Código de Conducta

### Nuestros Estándares

- Usar lenguaje inclusivo y respetuoso
- Respetar diferentes puntos de vista
- Aceptar críticas constructivas
- Enfocarse en lo mejor para la comunidad

### Comportamiento Inaceptable

- Lenguaje o imágenes inapropiadas
- Ataques personales
- Acoso público o privado
- Publicar información privada de otros

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la MIT License.

## Preguntas

Si tienes preguntas sobre cómo contribuir:
- Abre un issue con la etiqueta "question"
- Contacta al mantenedor: mariano.gobea@mercadolibre.com

---

¡Gracias por contribuir! 🎉
