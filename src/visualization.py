import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

def plot_unemployment_by_region(cleaned_file):
    df = pd.read_csv(cleaned_file)

    # Group data by Region
    region_data = df.groupby('Region')['Unemployment_Rate'].mean().reset_index()
    region_data = region_data.sort_values(by='Unemployment_Rate', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Unemployment_Rate', y='Region', data=region_data, palette='viridis')
    plt.title('Average Unemployment Rate by Region')
    plt.xlabel('Unemployment Rate (%)')
    plt.ylabel('Region')

    os.makedirs("outputs/figures", exist_ok=True)
    plt.savefig("outputs/figures/unemployment_by_region.png", dpi=300)
    plt.show()
    print("✅ Bar chart saved to outputs/figures/unemployment_by_region.png")

def plot_unemployment_trend(cleaned_file):
    df = pd.read_csv(cleaned_file)

    plt.figure(figsize=(14, 6))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=df, hue='Region', marker='o')
    plt.title('Unemployment Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    os.makedirs("outputs/figures", exist_ok=True)
    plt.savefig("outputs/figures/unemployment_trend.png", dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Line chart saved to outputs/figures/unemployment_trend.png")

def plot_interactive_scatter(cleaned_file):
    df = pd.read_csv(cleaned_file)

    fig = px.scatter(
        df,
        x="Region",
        y="Unemployment_Rate",
        color="Region",
        animation_frame="Date",
        size="Unemployment_Rate",
        hover_name="Region",
        title="Interactive Unemployment Rate Visualization"
    )
    fig.show()

if __name__ == "__main__":
    cleaned_file = r"C:\10x AIMastery\unemployment-rate-analysis-python\outputs\cleaned_unemployment.csv"
    
    plot_unemployment_by_region(cleaned_file)
    plot_unemployment_trend(cleaned_file)
    plot_interactive_scatter(cleaned_file)
