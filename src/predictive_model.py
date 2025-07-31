import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

def build_predictive_model(cleaned_file):
    df = pd.read_csv(cleaned_file)

    # Convert Date to numeric (ordinal) for regression
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date_ordinal'] = df['Date'].map(lambda x: x.toordinal())

    # Feature and target
    X = df[['Date_ordinal']]
    y = df['Unemployment_Rate']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"✅ Model trained successfully")
    print(f"📉 Mean Squared Error: {mse:.2f}")
    print(f"📊 R² Score: {r2:.2f}")

    # Future predictions
    future_dates = pd.date_range(df['Date'].max(), periods=12, freq='M')
    future_ordinal = future_dates.map(lambda x: x.toordinal()).values.reshape(-1, 1)
    future_pred = model.predict(future_ordinal)

    # Plot actual vs predicted
    plt.figure(figsize=(12, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.scatter(X_test, y_pred, color='red', label='Predicted')
    plt.title('Actual vs Predicted Unemployment Rate')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()

    os.makedirs("outputs/figures", exist_ok=True)
    plt.savefig("outputs/figures/predictive_model_results.png", dpi=300)
    plt.show()
    print("✅ Prediction results plot saved to outputs/figures/predictive_model_results.png")

if __name__ == "__main__":
    cleaned_file = r"C:\10x AIMastery\unemployment-rate-analysis-python\outputs\cleaned_unemployment.csv"
    build_predictive_model(cleaned_file)
