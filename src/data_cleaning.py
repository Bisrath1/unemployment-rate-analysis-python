import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.rename(columns={'Estimated Unemployment Rate (%)': 'Unemployment_Rate'}, inplace=True)
    df.to_csv(output_path, index=False)
