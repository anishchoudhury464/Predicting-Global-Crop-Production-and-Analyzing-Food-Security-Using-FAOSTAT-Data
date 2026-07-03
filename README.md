# 🌾 Predicting Global Crop Production and Analyzing Food Security Using FAOSTAT Data

> **ADS-599 Capstone Project | University of San Diego (MS in Applied Data Science)**

## 📖 Project Overview

Global food security has become one of the world's most pressing challenges due to rapid population growth, climate variability, and increasing pressure on agricultural resources. Traditional agricultural planning primarily relies on historical reporting and reactive decision-making, making it difficult to anticipate future food shortages.

This capstone project aims to develop an **end-to-end machine learning framework** for predicting global crop production using historical **FAOSTAT** datasets and analyzing food security indicators. The project integrates agricultural production, demographic, environmental, and food security data to generate predictive insights that can support evidence-based agricultural planning and policy decisions.

---

## 🎯 Problem Statement

Can historical FAOSTAT data be used to accurately forecast crop production while providing meaningful insights into global food security?

The objective is to build predictive machine learning models capable of forecasting crop production and analyzing how agricultural production relates to food security indicators across different countries.

---

## 🎯 Objectives

- Forecast global crop production using historical FAOSTAT data.
- Analyze the relationship between crop production and food security indicators.
- Compare multiple machine learning regression models.
- Identify key factors influencing crop production.
- Develop an interactive Streamlit dashboard for visualization and prediction.
- Deliver a reproducible end-to-end data science solution.

---

# 📊 Dataset

## Primary Data Source

**Food and Agriculture Organization (FAO)**

FAOSTAT

https://www.fao.org/faostat/

### Datasets Used

- Crop Production
- Food Security Indicators
- Population
- Land Use
- Fertilizers
- Food Balance Sheets
- Temperature Change
- Agricultural Trade
- Agricultural Emissions

### Coverage

- Global
- 180+ Countries
- Historical data (1961–Present depending on dataset)

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn
- Plotly

## Machine Learning

- Scikit-learn
- XGBoost
- LightGBM

## Dashboard

- Streamlit

## Version Control

- Git
- GitHub

---

# 📈 Machine Learning Workflow

Business Understanding

↓

Data Collection

↓

Data Cleaning

↓

Exploratory Data Analysis (EDA)

↓

Feature Engineering

↓

Model Development

↓

Model Evaluation

↓

Prediction

↓

Streamlit Dashboard

---

# 🤖 Machine Learning Models

The following regression models will be evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

Performance will be compared using

- RMSE
- MAE
- R² Score

---

# 📂 Repository Structure

```
project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate.py
│
├── dashboard/
│   ├── app.py
│
├── models/
│
├── reports/
│
├── images/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 📊 Expected Deliverables

- Machine Learning Prediction Models
- Data Cleaning Pipeline
- Feature Engineering Pipeline
- Interactive Streamlit Dashboard
- GitHub Repository
- Technical Documentation
- Capstone Research Paper
- Final Presentation

---

# 📌 Expected Outcomes

The project is expected to

- Improve crop production forecasting.
- Support evidence-based agricultural planning.
- Assist governments and policymakers in food security planning.
- Provide an interactive decision-support dashboard.
- Demonstrate an end-to-end data science workflow.

---

# 🌍 Real-World Impact

This project contributes toward **United Nations Sustainable Development Goal (SDG 2 – Zero Hunger)** by enabling data-driven agricultural forecasting and food security analysis.

Potential beneficiaries include

- Food and Agriculture Organization (FAO)
- Government agencies
- Agricultural researchers
- Farmers
- NGOs
- Policy makers

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<username>/crop-production-food-security.git
```

Navigate to the project

```bash
cd crop-production-food-security
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run dashboard/app.py
```

---

# 📷 Dashboard Preview

*(Screenshots will be added after dashboard development.)*

---

# 📚 References

- Food and Agriculture Organization of the United Nations (FAO). FAOSTAT. https://www.fao.org/faostat/
- CRISP-DM Process Model
- Peer-reviewed journal articles referenced in the capstone report (APA 7th edition).

---

# 👥 Team Members

- Anish Choudhury
- Krishna Sindhu Karri
- Praseeda Saripalle

---

# 📄 License

This repository is developed for academic purposes as part of the **ADS-599 Capstone Project** in the **Master of Science in Applied Data Science** program at the **University of San Diego**.
