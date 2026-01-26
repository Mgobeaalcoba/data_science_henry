"""
Script para cargar y explorar datasets comunes.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional


def load_iris() -> pd.DataFrame:
    """
    Carga el dataset Iris.

    Returns:
        DataFrame con el dataset Iris
    """
    from sklearn.datasets import load_iris

    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['species'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    return df


def load_boston_housing() -> pd.DataFrame:
    """
    Carga el dataset Boston Housing.

    Returns:
        DataFrame con el dataset Boston Housing
    """
    from sklearn.datasets import fetch_california_housing

    # Usando California housing como alternativa (Boston está deprecated)
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df['target'] = housing.target

    return df


def load_titanic(filepath: Optional[str] = None) -> pd.DataFrame:
    """
    Carga el dataset del Titanic.

    Args:
        filepath: Ruta al archivo CSV del Titanic

    Returns:
        DataFrame con el dataset del Titanic
    """
    if filepath is None:
        # URL de ejemplo
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
    else:
        df = pd.read_csv(filepath)

    return df


def get_dataset_info(df: pd.DataFrame) -> dict:
    """
    Obtiene información resumida de un dataset.

    Args:
        df: DataFrame a analizar

    Returns:
        Diccionario con información del dataset
    """
    info = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'missing_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum() / 1024**2,  # MB
        'duplicates': df.duplicated().sum(),
    }

    return info


def print_dataset_summary(df: pd.DataFrame, name: str = "Dataset") -> None:
    """
    Imprime un resumen del dataset.

    Args:
        df: DataFrame a resumir
        name: Nombre del dataset
    """
    print(f"\n{'='*60}")
    print(f" {name} Summary")
    print(f"{'='*60}\n")

    info = get_dataset_info(df)

    print(f"Shape: {info['shape'][0]} rows x {info['shape'][1]} columns")
    print(f"Memory usage: {info['memory_usage']:.2f} MB")
    print(f"Duplicates: {info['duplicates']}")

    print(f"\nColumns and types:")
    for col, dtype in info['dtypes'].items():
        missing = info['missing_values'][col]
        missing_pct = info['missing_percentage'][col]
        print(f"  - {col:<30} {str(dtype):<15} Missing: {missing} ({missing_pct:.1f}%)")

    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    # Ejemplo de uso
    print("Cargando datasets de ejemplo...\n")

    # Iris
    iris_df = load_iris()
    print_dataset_summary(iris_df, "Iris Dataset")
    print(iris_df.head())

    # California Housing
    housing_df = load_boston_housing()
    print_dataset_summary(housing_df, "California Housing Dataset")
    print(housing_df.head())
