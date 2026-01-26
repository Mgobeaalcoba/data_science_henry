"""
Funciones de preprocesamiento de datos.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from typing import List, Union, Tuple


def handle_missing_values(
    df: pd.DataFrame,
    strategy: str = 'mean',
    columns: List[str] = None
) -> pd.DataFrame:
    """
    Maneja valores faltantes en el DataFrame.

    Args:
        df: DataFrame con valores faltantes
        strategy: Estrategia de imputación ('mean', 'median', 'most_frequent', 'constant')
        columns: Columnas a imputar. Si None, se imputan todas las numéricas

    Returns:
        DataFrame con valores imputados
    """
    df_copy = df.copy()

    if columns is None:
        columns = df_copy.select_dtypes(include=[np.number]).columns.tolist()

    imputer = SimpleImputer(strategy=strategy)
    df_copy[columns] = imputer.fit_transform(df_copy[columns])

    return df_copy


def encode_categorical(
    df: pd.DataFrame,
    columns: List[str],
    method: str = 'onehot'
) -> pd.DataFrame:
    """
    Codifica variables categóricas.

    Args:
        df: DataFrame con variables categóricas
        columns: Columnas a codificar
        method: Método de codificación ('onehot', 'label')

    Returns:
        DataFrame con variables codificadas
    """
    df_copy = df.copy()

    if method == 'label':
        for col in columns:
            le = LabelEncoder()
            df_copy[col] = le.fit_transform(df_copy[col].astype(str))

    elif method == 'onehot':
        df_copy = pd.get_dummies(df_copy, columns=columns, drop_first=True)

    return df_copy


def scale_features(
    df: pd.DataFrame,
    columns: List[str],
    method: str = 'standard'
) -> Tuple[pd.DataFrame, Union[StandardScaler, MinMaxScaler]]:
    """
    Escala features numéricas.

    Args:
        df: DataFrame con features a escalar
        columns: Columnas a escalar
        method: Método de escalado ('standard', 'minmax')

    Returns:
        Tupla con DataFrame escalado y objeto scaler
    """
    df_copy = df.copy()

    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError(f"Método no soportado: {method}")

    df_copy[columns] = scaler.fit_transform(df_copy[columns])

    return df_copy, scaler


def remove_outliers(
    df: pd.DataFrame,
    columns: List[str],
    method: str = 'iqr',
    threshold: float = 1.5
) -> pd.DataFrame:
    """
    Remueve outliers del DataFrame.

    Args:
        df: DataFrame con outliers
        columns: Columnas a analizar
        method: Método de detección ('iqr', 'zscore')
        threshold: Umbral para considerar outliers

    Returns:
        DataFrame sin outliers
    """
    df_copy = df.copy()

    if method == 'iqr':
        for col in columns:
            Q1 = df_copy[col].quantile(0.25)
            Q3 = df_copy[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR

            df_copy = df_copy[
                (df_copy[col] >= lower_bound) & (df_copy[col] <= upper_bound)
            ]

    elif method == 'zscore':
        from scipy import stats
        for col in columns:
            z_scores = np.abs(stats.zscore(df_copy[col]))
            df_copy = df_copy[z_scores < threshold]

    return df_copy


def create_feature_bins(
    df: pd.DataFrame,
    column: str,
    n_bins: int = 5,
    labels: List[str] = None
) -> pd.DataFrame:
    """
    Crea bins para una variable continua.

    Args:
        df: DataFrame
        column: Columna a dividir en bins
        n_bins: Número de bins
        labels: Etiquetas para los bins

    Returns:
        DataFrame con nueva columna binned
    """
    df_copy = df.copy()
    new_col_name = f"{column}_binned"

    df_copy[new_col_name] = pd.cut(df_copy[column], bins=n_bins, labels=labels)

    return df_copy


if __name__ == "__main__":
    # Ejemplo de uso
    from data_loader import load_iris

    print("Ejemplo de preprocesamiento...\n")

    # Cargar datos
    df = load_iris()

    # Imputar valores faltantes (aunque Iris no tiene)
    df_imputed = handle_missing_values(df)

    # Escalar features
    feature_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    df_scaled, scaler = scale_features(df_imputed, feature_cols, method='standard')

    print("Dataset original:")
    print(df.head())
    print("\nDataset escalado:")
    print(df_scaled.head())
