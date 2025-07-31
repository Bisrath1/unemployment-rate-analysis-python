import pandas as pd

def analyze_unemployment(cleaned_data):
    df = pd.read_csv(cleaned_data)
    avg_rate = df['Unemployment_Rate'].mean()
    region_data = df.groupby('Region')['Unemployment_Rate'].mean().reset_index()
    return avg_rate, region_data
