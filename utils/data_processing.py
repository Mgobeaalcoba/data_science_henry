"""
Funciones para procesamiento de datos.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from typing import Tuple, Optional, Union


def load_data(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Carga datos desde diferentes formatos.

    Args:
        filepath: Ruta al archivo de datos
        **kwargs: Argumentos adicionales para la función de lectura

    Returns:
        DataFrame con los datos cargados
    """
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath, **kwargs)
    elif filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        return pd.read_excel(filepath, **kwargs)
    elif filepath.endswith('.json'):
        return pd.read_json(filepath, **kwargs)
    elif filepath.endswith('.parquet'):
        return pd.read_parquet(filepath, **kwargs)
    else:
        raise ValueError(f"Formato de archivo no soportado: {filepath}")


def clean_data(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    handle_missing: str = 'drop',
    missing_threshold: float = 0.5
) -> pd.DataFrame:
    """
    Limpia un DataFrame eliminando duplicados y manejando valores faltantes.

    Args:
        df: DataFrame a limpiar
        drop_duplicates: Si eliminar filas duplicadas
        handle_missing: Estrategia para valores faltantes ('drop', 'mean', 'median', 'mode')
        missing_threshold: Umbral de valores faltantes para eliminar columnas

    Returns:
        DataFrame limpio
    """
    df_clean = df.copy()

    # Eliminar duplicados
    if drop_duplicates:
        df_clean = df_clean.drop_duplicates()

    # Eliminar columnas con muchos valores faltantes
    missing_pct = df_clean.isnull().sum() / len(df_clean)
    cols_to_drop = missing_pct[missing_pct > missing_threshold].index
    df_clean = df_clean.drop(columns=cols_to_drop)

    # Manejar valores faltantes
    if handle_missing == 'drop':
        df_clean = df_clean.dropna()
    elif handle_missing == 'mean':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].mean())
    elif handle_missing == 'median':
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].median())
    elif handle_missing == 'mode':
        for col in df_clean.columns:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    return df_clean


def split_data(
    X: Union[pd.DataFrame, np.ndarray],
    y: Union[pd.Series, np.ndarray],
    test_size: float = 0.2,
    val_size: Optional[float] = None,
    random_state: int = 42,
    stratify: bool = False
) -> Union[Tuple, Tuple]:
    """
    Divide los datos en conjuntos de entrenamiento, validación y prueba.

    Args:
        X: Features
        y: Target
        test_size: Proporción del conjunto de prueba
        val_size: Proporción del conjunto de validación (opcional)
        random_state: Semilla para reproducibilidad
        stratify: Si mantener la distribución de clases

    Returns:
        Tupla con los conjuntos divididos
    """
    stratify_param = y if stratify else None

    if val_size is not None:
        # Split en train+val y test
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=stratify_param
        )

        # Split en train y val
        val_size_adjusted = val_size / (1 - test_size)
        stratify_param_temp = y_temp if stratify else None
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_size_adjusted,
            random_state=random_state, stratify=stratify_param_temp
        )

        return X_train, X_val, X_test, y_train, y_val, y_test
    else:
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=stratify_param
        )


def scale_features(
    X_train: Union[pd.DataFrame, np.ndarray],
    X_test: Union[pd.DataFrame, np.ndarray],
    method: str = 'standard',
    return_scaler: bool = False
) -> Union[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray, object]]:
    """
    Escala las features usando StandardScaler o MinMaxScaler.

    Args:
        X_train: Features de entrenamiento
        X_test: Features de prueba
        method: Método de escalado ('standard' o 'minmax')
        return_scaler: Si retornar el objeto scaler

    Returns:
        Features escaladas y opcionalmente el scaler
    """
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError(f"Método no soportado: {method}")

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    if return_scaler:
        return X_train_scaled, X_test_scaled, scaler
    else:
        return X_train_scaled, X_test_scaled
