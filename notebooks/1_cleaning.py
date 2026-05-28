import pandas as pd

# 1. Load the data into a digital spreadsheet (DataFrame)
df = pd.read_csv("data/raw_car_data.csv")
print("--- Raw Data ---")
print(df)

# 2. Remove completely duplicate rows
# Business logic: Duplicates skew our market averages.
df = df.drop_duplicates()

# 3. Handle missing values (Data Cleansing)
# Business logic: We can't predict price if mileage is blank. 
# We fill missing mileage with the average (mean) mileage of all cars.
mean_mileage = df['mileage'].mean()
df['mileage'] = df['mileage'].fillna(mean_mileage)

# Business logic: If a car has no price, it doesn't help our valuation model.
# We will drop rows where the price is missing.
df = df.dropna(subset=['price'])

df.to_csv("data/cleaned_car_data.csv", index=False)
print(df)

# 4. Save the polished data for our Big Data processing step
df.to_csv("data/cleaned_car_data.csv", index=False)
print("\nCleaned data successfully saved!")