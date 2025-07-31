

# 📊 Unemployment Rate Analysis with Python

## 📌 Project Overview

This project analyzes unemployment rates during the Covid-19 pandemic in India using Python.
It provides:

* ✅ Data cleaning and merging
* ✅ Statistical analysis
* ✅ Data visualizations (bar, line, interactive)
* ✅ Predictive modeling with Linear Regression

---

## 📂 Folder Structure

```
unemployment-rate-analysis-python/
│── data/
│   ├── Unemployment in India.csv
│   └── Unemployment_Rate_upto_11_2020.csv
│── notebooks/
│   └── 01_data_exploration.ipynb
│── src/
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── predictive_model.py
│── outputs/
│   ├── figures/
│   │   ├── unemployment_by_region.png
│   │   ├── unemployment_trend.png
│   │   └── predictive_model_results.png
│   ├── cleaned_unemployment.csv
│   └── unemployment_summary_by_region.csv
│── requirements.txt
│── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/unemployment-rate-analysis-python.git
cd unemployment-rate-analysis-python

# 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage (Step-by-Step)

### 1️⃣ Data Cleaning & Merging

```bash
python src/data_cleaning.py
```

* Merges the two raw CSVs
* Cleans missing values
* Saves: `outputs/cleaned_unemployment.csv`

---

### 2️⃣ Statistical Analysis

```bash
python src/analysis.py
```

* Prints overall unemployment stats
* Finds highest/lowest regions
* Saves summary → `outputs/unemployment_summary_by_region.csv`

---

### 3️⃣ Visualizations

```bash
python src/visualization.py
```

* Generates:

  * 📊 Bar chart → `outputs/figures/unemployment_by_region.png`
  * 📈 Line chart → `outputs/figures/unemployment_trend.png`
  * 🌐 Interactive Plotly chart (opens dynamically)

---

### 4️⃣ Predictive Modeling

```bash
python src/predictive_model.py
```

* Trains a **Linear Regression** model
* Forecasts unemployment for upcoming months
* Saves plot → `outputs/figures/predictive_model_results.png`

---

## 📊 Outputs

* **Processed Dataset:** `outputs/cleaned_unemployment.csv`
* **Regional Summary:** `outputs/unemployment_summary_by_region.csv`
* **Visual Charts:** `outputs/figures/`
* **Interactive Visualization:** Opens in browser

---

## 💻 Git Workflow

```bash
git init
git add .
git commit -m "Initialize complete unemployment analysis project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/unemployment-rate-analysis-python.git
git push -u origin main
```

---

## ✨ Future Improvements

* Use **Time Series Models (ARIMA, Prophet)** for better forecasting
* Build a **Streamlit or Dash dashboard** for interactive web visualization
* Integrate real-time unemployment data APIs

---

## 📜 License

This project is open-source and available under the MIT License.

---

