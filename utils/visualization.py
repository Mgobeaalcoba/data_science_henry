"""
Funciones para visualización de resultados de modelos.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve, auc
from typing import Optional, List, Any


def plot_confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    classes: Optional[List[str]] = None,
    normalize: bool = False,
    title: str = 'Matriz de Confusión',
    cmap: str = 'Blues',
    figsize: tuple = (8, 6)
) -> None:
    """
    Plotea una matriz de confusión.

    Args:
        y_true: Valores reales
        y_pred: Valores predichos
        classes: Nombres de las clases
        normalize: Si normalizar la matriz
        title: Título del gráfico
        cmap: Mapa de colores
        figsize: Tamaño de la figura
    """
    cm = confusion_matrix(y_true, y_pred)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.figure(figsize=figsize)
    sns.heatmap(
        cm,
        annot=True,
        fmt='.2f' if normalize else 'd',
        cmap=cmap,
        xticklabels=classes,
        yticklabels=classes,
        cbar=True
    )
    plt.title(title)
    plt.ylabel('Valor Real')
    plt.xlabel('Valor Predicho')
    plt.tight_layout()
    plt.show()


def plot_roc_curve(
    y_true: np.ndarray,
    y_proba: np.ndarray,
    title: str = 'Curva ROC',
    figsize: tuple = (8, 6)
) -> None:
    """
    Plotea la curva ROC.

    Args:
        y_true: Valores reales
        y_proba: Probabilidades predichas
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_learning_curves(
    train_sizes: np.ndarray,
    train_scores: np.ndarray,
    val_scores: np.ndarray,
    title: str = 'Curvas de Aprendizaje',
    figsize: tuple = (10, 6)
) -> None:
    """
    Plotea curvas de aprendizaje.

    Args:
        train_sizes: Tamaños del conjunto de entrenamiento
        train_scores: Scores de entrenamiento
        val_scores: Scores de validación
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)

    plt.figure(figsize=figsize)
    plt.plot(train_sizes, train_mean, 'o-', color='r', label='Training score')
    plt.plot(train_sizes, val_mean, 'o-', color='g', label='Validation score')

    plt.fill_between(
        train_sizes,
        train_mean - train_std,
        train_mean + train_std,
        alpha=0.1,
        color='r'
    )
    plt.fill_between(
        train_sizes,
        val_mean - val_std,
        val_mean + val_std,
        alpha=0.1,
        color='g'
    )

    plt.xlabel('Tamaño del conjunto de entrenamiento')
    plt.ylabel('Score')
    plt.title(title)
    plt.legend(loc='best')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_feature_importance(
    feature_names: List[str],
    importances: np.ndarray,
    top_n: int = 20,
    title: str = 'Importancia de Features',
    figsize: tuple = (10, 8)
) -> None:
    """
    Plotea la importancia de las features.

    Args:
        feature_names: Nombres de las features
        importances: Valores de importancia
        top_n: Número de features a mostrar
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    indices = np.argsort(importances)[::-1][:top_n]
    top_features = [feature_names[i] for i in indices]
    top_importances = importances[indices]

    plt.figure(figsize=figsize)
    plt.barh(range(len(top_importances)), top_importances, align='center')
    plt.yticks(range(len(top_importances)), top_features)
    plt.xlabel('Importancia')
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def plot_residuals(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    figsize: tuple = (12, 5)
) -> None:
    """
    Plotea gráficos de residuos para regresión.

    Args:
        y_true: Valores reales
        y_pred: Valores predichos
        figsize: Tamaño de la figura
    """
    residuals = y_true - y_pred

    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # Residuos vs Predicciones
    axes[0].scatter(y_pred, residuals, alpha=0.5)
    axes[0].axhline(y=0, color='r', linestyle='--')
    axes[0].set_xlabel('Valores Predichos')
    axes[0].set_ylabel('Residuos')
    axes[0].set_title('Residuos vs Predicciones')
    axes[0].grid(alpha=0.3)

    # Distribución de residuos
    axes[1].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
    axes[1].axvline(x=0, color='r', linestyle='--')
    axes[1].set_xlabel('Residuos')
    axes[1].set_ylabel('Frecuencia')
    axes[1].set_title('Distribución de Residuos')
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
