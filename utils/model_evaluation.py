"""
Funciones para evaluación de modelos.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)
from sklearn.model_selection import cross_val_score
from typing import Dict, Any, Optional


def evaluate_classification(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: Optional[np.ndarray] = None,
    average: str = 'binary'
) -> Dict[str, float]:
    """
    Evalúa un modelo de clasificación con múltiples métricas.

    Args:
        y_true: Valores reales
        y_pred: Valores predichos
        y_proba: Probabilidades predichas (para ROC-AUC)
        average: Tipo de promedio para métricas multiclase

    Returns:
        Diccionario con métricas de evaluación
    """
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average=average, zero_division=0),
        'recall': recall_score(y_true, y_pred, average=average, zero_division=0),
        'f1_score': f1_score(y_true, y_pred, average=average, zero_division=0),
    }

    if y_proba is not None:
        try:
            metrics['roc_auc'] = roc_auc_score(y_true, y_proba, average=average)
        except ValueError:
            metrics['roc_auc'] = None

    return metrics


def evaluate_regression(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> Dict[str, float]:
    """
    Evalúa un modelo de regresión con múltiples métricas.

    Args:
        y_true: Valores reales
        y_pred: Valores predichos

    Returns:
        Diccionario con métricas de evaluación
    """
    metrics = {
        'mse': mean_squared_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred),
        'mape': np.mean(np.abs((y_true - y_pred) / y_true)) * 100,
    }

    return metrics


def cross_validate_model(
    model: Any,
    X: np.ndarray,
    y: np.ndarray,
    cv: int = 5,
    scoring: str = 'accuracy'
) -> Dict[str, Any]:
    """
    Realiza validación cruzada de un modelo.

    Args:
        model: Modelo a evaluar
        X: Features
        y: Target
        cv: Número de folds
        scoring: Métrica de evaluación

    Returns:
        Diccionario con resultados de validación cruzada
    """
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)

    results = {
        'scores': scores,
        'mean': scores.mean(),
        'std': scores.std(),
        'min': scores.min(),
        'max': scores.max(),
    }

    return results


def print_metrics(metrics: Dict[str, float], title: str = "Métricas de Evaluación") -> None:
    """
    Imprime métricas de evaluación de forma formateada.

    Args:
        metrics: Diccionario con métricas
        title: Título a mostrar
    """
    print(f"\n{'='*50}")
    print(f"{title:^50}")
    print(f"{'='*50}")

    for metric, value in metrics.items():
        if value is not None:
            if isinstance(value, float):
                print(f"{metric.upper():.<30} {value:.4f}")
            else:
                print(f"{metric.upper():.<30} {value}")

    print(f"{'='*50}\n")


def compare_models(
    models_results: Dict[str, Dict[str, float]],
    metric: str = 'accuracy'
) -> pd.DataFrame:
    """
    Compara resultados de múltiples modelos.

    Args:
        models_results: Diccionario con resultados de cada modelo
        metric: Métrica principal para ordenar

    Returns:
        DataFrame con comparación de modelos
    """
    df = pd.DataFrame(models_results).T

    if metric in df.columns:
        df = df.sort_values(metric, ascending=False)

    return df
