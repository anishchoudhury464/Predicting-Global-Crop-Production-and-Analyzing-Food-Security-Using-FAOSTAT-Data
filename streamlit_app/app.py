import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib
import os






# -------------------------------
# LOAD DATASET
# -------------------------------

# -------------------------------
# LOAD DASHBOARD DATA
# -------------------------------

@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(
        BASE_DIR,
        "data",
        "dashboard_data.csv"
    )

    return pd.read_csv(path)

df = load_data()


# -------------------------------
# LOAD PRE-COMPUTED SUMMARIES
# -------------------------------

@st.cache_data
def load_yearly_production():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(
        BASE_DIR,
        "data",
        "yearly_production.csv"
    )

    return pd.read_csv(path)


@st.cache_data
def load_country_production():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(
        BASE_DIR,
        "data",
        "country_production.csv"
    )

    return pd.read_csv(path)


@st.cache_data
def load_country_year_production():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(
        BASE_DIR,
        "data",
        "country_year_production.csv"
    )

    return pd.read_csv(path)


yearly_production_data = load_yearly_production()
country_production_data = load_country_production()
country_year_production_data = load_country_year_production()

# @st.cache_data
# def get_yearly_production(df):
#     return (
#         df.groupby("Year")["Production"]
#         .sum()
#         .reset_index()
#     )

@st.cache_resource
def load_model():
    MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model",
    "best_crop_production_model.pkl"
    )
    model = joblib.load(MODEL_PATH)
    return model

model = load_model()


@st.cache_resource
def load_feature_names():
    FEATURE_PATH = os.path.join(
        os.path.dirname(__file__),
        "model",
        "feature_names.pkl"
    )
    return joblib.load(FEATURE_PATH)
feature_names = load_feature_names()


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Crop Production Prediction Dashboard",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("🌾 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📊 Dataset Explorer",
        "📈 Visualizations",
        "🤖 Crop Prediction",
        "📉 Model Performance",
        "ℹ️ About"
    ]
)

# -------------------------------
# TITLE
# -------------------------------
if page == "🏠 Home":
    
    st.title("🌾 Crop Production Prediction Dashboard")

    st.markdown("""
    ### AI-Driven Crop Production Prediction using Machine Learning

    This dashboard was developed as part of the **USD MS Applied Data Science Capstone Project**.

    The objective of this project is to predict crop production using socioeconomic and agricultural indicators collected from FAOSTAT datasets.

    ---
    """)

    st.header("📌 Project Overview")

    st.write("""
    This dashboard allows users to:

    - Explore the dataset
    - Visualize crop production trends
    - Predict crop production using the trained Linear Regression model
    - Review model performance
    """)

    st.header("📊 Dataset")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Models Compared", "4")
    col2.metric("Final Model", "Linear Regression")
    col3.metric("Target Variable", "Crop Production")
    col4.metric(
    "Dataset Size",
    f"{df.shape[0]:,}"
    )

    st.success("Application setup completed successfully.")

# -------------------------------
# DATASET EXPLORER
# -------------------------------

if page == "📊 Dataset Explorer":
    
    st.title("📊 Dataset Explorer")

    st.write("Explore the cleaned dataset used for model development.")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", f"{df.shape[0]:,}")
    col2.metric("Columns", df.shape[1])
    missing = df.isna().sum().sum()
    total = df.shape[0] * df.shape[1]
    missing_percent = (missing / total) * 100

    col3.metric(
        "Missing Values",
        f"{missing:,}",
        f"{missing_percent:.2f}%"
    )

    
    st.markdown("---")

    st.subheader("Dataset Preview")

    country = st.selectbox(
        "Select Country",
        sorted(df["Area"].dropna().unique())
    )

    filtered_df = df[df["Area"] == country]

    st.dataframe(
        filtered_df.head(100),
        width="stretch"
    )


    csv = filtered_df.to_csv(index=False).encode("utf-8")


    st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name=f"{country}_dataset.csv",
    mime="text/csv"
    )

    st.subheader("Column Information")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(
        column_info,
        width="stretch"
    )

    st.subheader("Summary Statistics")

    sample_df = df.sample(
    min(100000, len(df)),
    random_state=42
    )   

    st.dataframe(
    sample_df.describe().round(2),
    width="stretch"
    )

    

# -------------------------------
# VISUALIZATIONS
# -------------------------------

if page == "📈 Visualizations":
    
    st.title("📈 Data Visualizations")

    st.write("Interactive visualizations of the crop production dataset.")

    st.markdown("---")

    # -----------------------------
    # Chart 1: Crop Production Over Time
    # -----------------------------

    st.subheader("🌾 Global Crop Production Over Time")

    yearly_production = yearly_production_data

    fig1 = px.line(
        yearly_production,
        x="Year",
        y="Production",
        markers=True,
        title="Total Crop Production by Year"
    )

    fig1.update_layout(
    hovermode="x unified",
    height=550
    )

    st.plotly_chart(fig1, width="stretch")

    st.markdown("---")

    # -----------------------------
    # Chart 2: Top Producing Countries
    # -----------------------------

    st.subheader("🌍 Top 10 Producing Countries")

    exclude_regions = [
        "World",
        "Asia",
        "Europe",
        "Africa",
        "Americas",
        "Oceania",
        "Eastern Asia",
        "Southern Asia",
        "Northern America",
        "South America",
        "European Union (27)",
        "China, mainland",
        "Net Food Importing Developing Countries",
        "Least Developed Countries (LDC)",
        "Low Income Food Deficit Countries (LIFDC)",
        "Eastern Europe",
        "Western Europe",
        "Northern Europe",
        "Southern Europe",
        "Developed Regions",
        "Developing Regions",
        "Land Locked Developing Countries",
        "Small Island Developing States"
    ]

    country_df = country_production_data[
    ~country_production_data["Area"].isin(exclude_regions)
    ]

    top_countries = (
        country_df
        .nlargest(10, "Production")
        .reset_index(drop=True)
    )

    fig2 = px.bar(
        top_countries,
        x="Area",
        y="Production",
        color="Production",
        text_auto=".2s",
        title="Top 10 Crop Producing Countries"
    )

    fig2.update_layout(
        xaxis_title="Country",
        yaxis_title="Production",
        height=550
    )

    st.plotly_chart(fig2, width="stretch")

    st.markdown("---")

    # -----------------------------
    # Chart 3: Production Distribution
    # -----------------------------

    st.subheader("📊 Production Distribution")

    hist_df = df.loc[
    df["Production"] > 0,
    ["Production"]
    ].copy()

    hist_df = hist_df.sample(
        min(100000, len(hist_df)),
        random_state=42
    )
    
    hist_df["Log_Production"] = np.log10(hist_df["Production"])


    fig3 = px.histogram(
        hist_df,
        x="Log_Production",
        nbins=60,
        title="Distribution of Crop Production (Log Scale)"
    )

    fig3.update_layout(
        xaxis_title="Log10(Production)",
        yaxis_title="Frequency",
        height=500
    )

    st.plotly_chart(fig3, width="stretch")

    st.markdown("---")

    # -----------------------------
    # Chart 4: Correlation Heatmap
    # -----------------------------

    st.subheader("🔥 Feature Correlation")

    numeric_df = df.select_dtypes(include="number")

    numeric_df = numeric_df.sample(
        min(50000, len(numeric_df)),
        random_state=42
    )

    corr = numeric_df.corr(numeric_only=True)


    fig4 = px.imshow(
        corr.round(2),
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
        title="Feature Correlation Matrix"
    )

    fig4.update_layout(
        height=700
    )

    st.plotly_chart(
    fig4,
    width="stretch"
    )

    st.markdown("---")

    st.subheader("📍 Crop Production Trend by Country")

    country = st.selectbox(
        "Select Country",
        sorted(df["Area"].dropna().unique()),
        key="country_trend"
    )

    # country_df = df[df["Area"] == country]

    country_year = country_year_production_data[
    country_year_production_data["Area"] == country
    ].copy()

    fig5 = px.line(
        country_year,
        x="Year",
        y="Production",
        markers=True,
        title=f"Production Trend - {country}"
    )

    fig5.update_layout(
    hovermode="x unified",
    height=550
    )

    st.plotly_chart(fig5, width="stretch")

    csv = country_year.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Country Trend",
        csv,
        file_name=f"{country}_production.csv",
        mime="text/csv"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Average Production",
            f"{country_year['Production'].mean():,.0f}"
        )

    with col2:
        st.metric(
            "Maximum Production",
            f"{country_year['Production'].max():,.0f}"
        )
# -------------------------------
# PREDICTION
# -------------------------------

if page == "🤖 Crop Prediction":
    
    st.title("🤖 Crop Production Prediction")

    st.write("Enter agricultural indicators to estimate crop production.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        population = st.number_input(
            "Population",
            min_value=0.0,
            value=1000000.0
        )

        agricultural_land = st.number_input(
            "Agricultural Land",
            min_value=0.0,
            value=50000.0
        )

        arable_land = st.number_input(
            "Arable Land",
            min_value=0.0,
            value=20000.0
        )

        cropland = st.number_input(
            "Cropland",
            min_value=0.0,
            value=18000.0
        )

    with col2:

        nitrogen = st.number_input(
            "Nitrogen",
            min_value=0.0,
            value=50000.0
        )

        phosphate = st.number_input(
            "Phosphate",
            min_value=0.0,
            value=15000.0
        )

        potash = st.number_input(
            "Potash",
            min_value=0.0,
            value=12000.0
        )

    st.markdown("---")

    if st.button("🚀 Predict Crop Production"):

        input_values = {
            "Population": population,
            "Agricultural_Land": agricultural_land,
            "Arable_Land": arable_land,
            "Cropland": cropland,
            "Nitrogen": nitrogen,
            "Phosphate": phosphate,
            "Potash": potash,
        }

        input_df = pd.DataFrame([input_values])

        # Ensure feature order matches training
        input_df = input_df.reindex(columns=feature_names, fill_value=0)

        prediction = model.predict(input_df)[0]

        st.success(f"### 🌾 Predicted Crop Production: {prediction:,.2f}")

# -------------------------------
# MODEL PERFORMANCE
# -------------------------------

if page == "📉 Model Performance":
    
    st.title("📉 Model Performance")

    st.write("Evaluation results of the final Linear Regression model.")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
    "Final Model",
    "Linear Regression"
    )

    col2.metric(
        "R² Score",
        "0.0637"
    )

    col3.metric(
        "RMSE",
        "28,860,372.08"
    )

    col4.metric(
        "MAE",
        "4,084,985.80"
        )
    


    st.markdown("---")

    st.subheader("Model Comparison")

    comparison = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost"
        ],

        "R² Score":[
            0.063709,
            0.057401,
            0.057416,
            0.058646
        ]

    })

    fig = px.bar(
    comparison,
    x="Model",
    y="R² Score",
    color="R² Score",
    text_auto=".4f",
    title="Model Comparison (R² Score)"
    )

    fig.update_layout(
        height=550,
        yaxis_title="R² Score",
        xaxis_title="Model"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Evaluation Metrics")

    results = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost"
        ],

        "MAE":[
            4084985.80,
            4044786.56,
            4045803.82,
            4032441.51
        ],

        "RMSE":[
            28860372.08,
            28957427.83,
            28957198.08,
            28938300.19
        ],

        "R²":[
            0.063709,
            0.057401,
            0.057416,
            0.058646
        ]

    })

    st.dataframe(
        results.style.format({
            "MAE":"{:,.2f}",
            "RMSE":"{:,.2f}",
            "R²":"{:.4f}"
        }),
        width="stretch"
    )

    st.markdown("---")

    st.subheader("Final Model Summary")

    st.success("""
Linear Regression achieved the highest R² score among the four evaluated regression 
models and was selected as the final deployment model.

Although the overall predictive performance remains modest, Linear Regression
provides the best balance between predictive performance, simplicity and
interpretability for the current FAOSTAT feature set.

The relatively low R² indicates that additional factors such as rainfall,
temperature, soil quality, irrigation and crop-specific characteristics are
likely required to improve prediction accuracy.
""")

# -------------------------------
# ABOUT
# -------------------------------

if page == "ℹ️ About":

    st.title("ℹ️ About")

    st.write("""
    This dashboard was developed for the USD MS Applied Data Science Capstone Project.

    **Dataset:** FAOSTAT

    **Final Model:** Linear Regression

    **Framework:** Streamlit

    **Language:** Python
    """)



