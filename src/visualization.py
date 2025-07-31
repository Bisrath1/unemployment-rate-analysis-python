import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def plot_unemployment_by_region(region_data):
    plt.figure(figsize=(10,6))
    sns.barplot(x='Unemployment_Rate', y='Region', data=region_data, palette='viridis')
    plt.title('Average Unemployment Rate by Region')
    plt.savefig('outputs/figures/unemployment_by_region.png')
    plt.show()

def plot_unemployment_trend(cleaned_data):
    df = pd.read_csv(cleaned_data)
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=df, hue='Region')
    plt.title('Unemployment Rate Over Time')
    plt.savefig('outputs/figures/unemployment_trend.png')
    plt.show()
