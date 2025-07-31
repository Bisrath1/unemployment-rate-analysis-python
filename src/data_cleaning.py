import pandas as pd
import os

def clean_and_merge_data(file1, file2, output_file):
    # Load datasets
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Standardize column names
    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()

    # Convert Date columns to datetime
    df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True)
    df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True)

    # Rename unemployment rate column
    if 'Estimated Unemployment Rate (%)' in df1.columns:
        df1.rename(columns={'Estimated Unemployment Rate (%)': 'Unemployment_Rate'}, inplace=True)
    if 'Estimated Unemployment Rate (%)' in df2.columns:
        df2.rename(columns={'Estimated Unemployment Rate (%)': 'Unemployment_Rate'}, inplace=True)

    # Drop duplicates if any
    df1.drop_duplicates(inplace=True)
    df2.drop_duplicates(inplace=True)

    # Merge datasets
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Handle missing values
    merged_df.dropna(inplace=True)

    # Save cleaned dataset
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    merged_df.to_csv(output_file, index=False)
    print(f"✅ Cleaned dataset saved to: {output_file}")
    print(f"✅ Final shape: {merged_df.shape}")

if __name__ == "__main__":
    file1 = r"C:\10x AIMastery\unemployment-rate-analysis-python\data\Unemployment in India.csv"
    file2 = r"C:\10x AIMastery\unemployment-rate-analysis-python\data\Unemployment_Rate_upto_11_2020.csv"
    output_file = r"C:\10x AIMastery\unemployment-rate-analysis-python\outputs\cleaned_unemployment.csv"
    
    clean_and_merge_data(file1, file2, output_file)
