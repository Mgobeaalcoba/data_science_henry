import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Cargar datos
df = pd.read_csv('/Users/mgobea/Documents/Personal_Develop/data_science_henry/clase_02_regresion/data/retailboost_customers_regression.csv')

# Variables
numeric_cols = ['age', 'income', 'visits_per_month', 'satisfaction_score', 'membership_years']
X = df[numeric_cols]
y = df['monthly_spent']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo Simple (income)
X_train_simple = X_train[['income']]
X_test_simple = X_test[['income']]
modelo_simple = LinearRegression()
modelo_simple.fit(X_train_simple, y_train)
y_pred_simple = modelo_simple.predict(X_test_simple)

# Modelo Múltiple
modelo_multiple = LinearRegression()
modelo_multiple.fit(X_train, y_train)
y_pred_multiple = modelo_multiple.predict(X_test)

# Métricas
print("="*80)
print("MÉTRICAS MODELO SIMPLE (Income)")
print("="*80)
print(f"Intercepto: {modelo_simple.intercept_:.4f}")
print(f"Coeficiente income: {modelo_simple.coef_[0]:.4f}")
print(f"R²: {r2_score(y_test, y_pred_simple):.4f}")
print(f"MAE: ${mean_absolute_error(y_test, y_pred_simple):.2f}")
print(f"RMSE: ${np.sqrt(mean_squared_error(y_test, y_pred_simple)):.2f}")

print("\n" + "="*80)
print("MÉTRICAS MODELO MÚLTIPLE")
print("="*80)
print(f"Intercepto: {modelo_multiple.intercept_:.4f}")
print("\nCoeficientes:")
for col, coef in zip(numeric_cols, modelo_multiple.coef_):
    print(f"  {col:20s}: {coef:8.4f}")
print(f"\nR²: {r2_score(y_test, y_pred_multiple):.4f}")
print(f"MAE: ${mean_absolute_error(y_test, y_pred_multiple):.2f}")
print(f"RMSE: ${np.sqrt(mean_squared_error(y_test, y_pred_multiple)):.2f}")

print("\n" + "="*80)
print("ESTADÍSTICAS DEL DATASET")
print("="*80)
print(f"Total registros: {len(df)}")
print(f"Train: {len(X_train)}, Test: {len(X_test)}")
print(f"\nMonthly Spent:")
print(f"  Media: ${y.mean():.2f}")
print(f"  Std: ${y.std():.2f}")
print(f"  Min: ${y.min():.2f}")
print(f"  Max: ${y.max():.2f}")

print("\n" + "="*80)
print("CORRELACIONES CON MONTHLY_SPENT")
print("="*80)
correlations = df[numeric_cols + ['monthly_spent']].corr()['monthly_spent'].sort_values(ascending=False)
print(correlations)
