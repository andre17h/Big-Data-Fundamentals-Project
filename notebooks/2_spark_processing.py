import duckdb
import pandas as pd

print("--- DuckDB Analytical Engine Started Successfully ---")

# 1. Load the cleaned data 
# DuckDB can query data right out of a pandas dataframe or directly from the file!
cleaned_data_path = "data/cleaned_car_data.csv"

# 2. Run an enterprise-level SQL Aggregation 
# Business Logic: Group vehicles by brand to calculate market-wide average price and mileage.
query = """
    SELECT 
        brand,
        ROUND(AVG(price), 2) AS average_price,
        ROUND(AVG(mileage), 2) AS average_mileage
    FROM read_csv_auto('data/cleaned_car_data.csv')
    GROUP BY brand
    ORDER BY average_price DESC
"""

# 3. Execute the processing
market_insights = duckdb.sql(query).df()

print("\n--- Processed Market Insights (Calculated via Analytical Engine) ---")
print(market_insights)

# 4. Export the findings to feed our visual dashboard folder
market_insights.to_csv("data/spark_market_insights.csv", index=False)
print("\nAggregated market insights successfully saved for Dashboarding!")