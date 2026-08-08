# 🌾 Crop Production Prediction Dashboard

An interactive Streamlit dashboard developed as part of the **ADS-599 Capstone Project** for the **University of San Diego – MS in Applied Data Science**.

The dashboard enables users to explore historical crop production data, visualize agricultural trends, and predict crop production using a trained machine learning model.

---

## Features

- Interactive dataset exploration
- Global crop production trends
- Top crop-producing countries
- Production distribution analysis
- Feature correlation heatmap
- Country-wise production trends
- Crop production prediction
- Machine learning model performance comparison

---

## Dataset

Source: **FAOSTAT – Food and Agriculture Organization of the United Nations**

<https://www.fao.org/faostat/>

---

## Machine Learning Model

Final deployed model:

- Linear Regression

Evaluation Metrics:

- R² Score: **0.0637**
- RMSE: **28,860,372.08**
- MAE: **4,084,985.80**

---

## Project Structure

```
dashboard/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── clean_dataset.csv
│
├── model/
│   ├── best_crop_production_model.pkl
│   └── feature_names.pkl
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/anishchoudhury464/Predicting-Global-Crop-Production-and-Analyzing-Food-Security-Using-FAOSTAT-Data.git
```

Navigate to the dashboard directory

```bash
cd dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Dashboard Pages

- Home
- Dataset Explorer
- Data Visualizations
- Crop Production Prediction
- Model Performance
- About

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Joblib

---

## Author

- Anish Choudhury
- Krishna Sindhu Karri
- Praseeda Saripalle

MS Applied Data Science

University of San Diego
