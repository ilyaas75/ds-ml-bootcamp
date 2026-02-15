import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1. Load & Inspect
df = pd.read_csv("C:\\Users\\Ilyaas Hassan\\Desktop\\Assigment_ilyaas75- submisisions\\ds-ml-bootcamp\\dataset\\car_l3_dataset.csv")
print(f"Initial Shape: {df.shape}")
# [Insert your head/info/missing print statements here]

# 2. Clean Target Formatting (Price)
df['Price'] = df['Price'].replace(r"[ \$,]", "", regex=True).astype(float)

# 3. Fix Category Errors
# Standardize 'Subrb' and handle the '??' or empty strings
df['Location'] = df['Location'].replace({"Subrb": "Suburb", "??": np.nan, "": np.nan})

# 4. Impute Missing Values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

# 5. Remove Duplicates
df = df.drop_duplicates()

# 6. Outliers (IQR capping)
def get_bounds(series):
    Q1, Q3 = series.quantile([0.25, 0.75])
    IQR = Q3 - Q1
    return Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

for col in ['Price', 'Odometer_km']:
    lb, ub = get_bounds(df[col])
    df[col] = df[col].clip(lower=lb, upper=ub)

# 7. One-Hot Encode (Location)
df = pd.get_dummies(df, columns=["Location"], prefix="Loc")

# 8. Feature Engineering
df["CarAge"] = 2026 - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)
df["Is_Urban"] = (df["Loc_City"] == 1).astype(int)
df["LogPrice"] = np.log1p(df["Price"])

# 9. Feature Scaling (X only)
# Identify continuous features to scale (Exclude Price, LogPrice, and Dummies)
features_to_scale = ["Odometer_km", "Doors", "Accidents", "CarAge", "Km_per_year"]
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# 10. Final Checks & Save
print(df.isnull().sum()) # Should be all 0
df.to_csv("car_l3_clean_ready.csv", index=False)
