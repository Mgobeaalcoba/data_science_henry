"""
Utilidades compartidas para el curso de Data Science y Machine Learning.
"""

from .data_processing import (
    load_data,
    clean_data,
    split_data,
    scale_features,
)
from .visualization import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_learning_curves,
    plot_feature_importance,
)
from .model_evaluation import (
    evaluate_classification,
    evaluate_regression,
    cross_validate_model,
)

__version__ = "1.0.0"

__all__ = [
    "load_data",
    "clean_data",
    "split_data",
    "scale_features",
    "plot_confusion_matrix",
    "plot_roc_curve",
    "plot_learning_curves",
    "plot_feature_importance",
    "evaluate_classification",
    "evaluate_regression",
    "cross_validate_model",
]
