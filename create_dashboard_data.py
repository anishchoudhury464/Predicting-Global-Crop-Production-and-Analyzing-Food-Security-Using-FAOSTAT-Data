import pandas as pd

input_file = "data/clean_dataset.csv"

print("Reading large dataset in chunks...")
print("This may take a few minutes.")


# ============================================================
# 1. CREATE SMALL DASHBOARD DATASET
# ============================================================

print("\nCreating dashboard_data.csv...")

sample_parts = []

for chunk in pd.read_csv(
    input_file,
    chunksize=100000
):
    sample = chunk.sample(
        min(6250, len(chunk)),
        random_state=42
    )

    sample_parts.append(sample)

dashboard_df = pd.concat(
    sample_parts,
    ignore_index=True
)

dashboard_df = dashboard_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

dashboard_df.to_csv(
    "data/dashboard_data.csv",
    index=False
)

print(
    "dashboard_data.csv created:",
    dashboard_df.shape
)


# ============================================================
# 2. CREATE EXACT YEARLY PRODUCTION TOTALS
# ============================================================

print("\nCreating yearly_production.csv...")

yearly_parts = []

for chunk in pd.read_csv(
    input_file,
    usecols=["Year", "Production"],
    chunksize=100000
):

    yearly = (
        chunk.groupby("Year")["Production"]
        .sum()
        .reset_index()
    )

    yearly_parts.append(yearly)

yearly_df = pd.concat(
    yearly_parts,
    ignore_index=True
)

yearly_df = (
    yearly_df
    .groupby("Year")["Production"]
    .sum()
    .reset_index()
)

yearly_df.to_csv(
    "data/yearly_production.csv",
    index=False
)

print(
    "yearly_production.csv created:",
    yearly_df.shape
)


# ============================================================
# 3. CREATE EXACT COUNTRY TOTALS
# ============================================================

print("\nCreating country_production.csv...")

country_parts = []

for chunk in pd.read_csv(
    input_file,
    usecols=["Area", "Production"],
    chunksize=100000
):

    country = (
        chunk.groupby("Area")["Production"]
        .sum()
        .reset_index()
    )

    country_parts.append(country)

country_df = pd.concat(
    country_parts,
    ignore_index=True
)

country_df = (
    country_df
    .groupby("Area")["Production"]
    .sum()
    .reset_index()
)

country_df.to_csv(
    "data/country_production.csv",
    index=False
)

print(
    "country_production.csv created:",
    country_df.shape
)


# ============================================================
# 4. CREATE EXACT COUNTRY + YEAR TOTALS
# ============================================================

print("\nCreating country_year_production.csv...")

country_year_parts = []

for chunk in pd.read_csv(
    input_file,
    usecols=["Area", "Year", "Production"],
    chunksize=100000
):

    country_year = (
        chunk
        .groupby(["Area", "Year"])["Production"]
        .sum()
        .reset_index()
    )

    country_year_parts.append(country_year)

country_year_df = pd.concat(
    country_year_parts,
    ignore_index=True
)

country_year_df = (
    country_year_df
    .groupby(["Area", "Year"])["Production"]
    .sum()
    .reset_index()
)

country_year_df.to_csv(
    "data/country_year_production.csv",
    index=False
)

print(
    "country_year_production.csv created:",
    country_year_df.shape
)


# ============================================================
# FINISHED
# ============================================================

print("\n========================================")
print("ALL DASHBOARD DATA FILES CREATED!")
print("========================================")

print("\nCreated files:")

print("1. data/dashboard_data.csv")
print("2. data/yearly_production.csv")
print("3. data/country_production.csv")
print("4. data/country_year_production.csv")