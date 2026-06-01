# Big Data Project: Automotive Marketplace Valuation Dashboard

Welcome to my final project! This page acts as a quick summary of what this project is about, the real-world problem it solves, where the data comes from, and how the entire pipeline works from start to finish.

## What Problem Are We Solving?
**Problem:** Manual car valuation at dealerships is slow and prone to human errors, which hurts profit margins. 
**Solution:** This project builds an automated data pipeline that collects messy, raw car listings, cleans them, calculates market price averages per brand, and displays them on a live dashboard.

## Architecture Diagram

* **Data Acquisition:** Secondary-market car listings loaded from a local file (`data/raw_car_data.csv`).
It includes important information about each car, such as:
* Car Brand (Audi, BMW, Ford, Volkswagen, Dacia)
* Market Price
* Mileage (mechanical wear)
* Fuel Type and Engine Size.

* **Preprocessing:** Python (`pandas`) used to delete duplicates, remove unpriced cars, and fill missing mileage.
* **Big Data Processing:** `DuckDB` engine used to run high-performance SQL analytics on the clean data.
* **Analytics & Insights:** SQL queries group the cars by brand to automatically calculate average prices and mileage.
* **Visualization:** Tableau Public deployed to present cloud-hosted interactive charts for management.

## Installation & Usage

1. Clone this repository to your Mac.
2. Install the required libraries: `pip install pandas duckdb`
3. Run `python notebooks/1_cleaning.py` to clean the raw listings.
4. Run `python notebooks/2_spark_processing.py` to calculate the market averages.

## Key Findings

* **Market Overview:** The engine automatically sorted the market, revealing that Audi commands the highest average price ($13,833.33) and Dacia the lowest ($4,500.00).
* **Business Value:** The scatter plot proves that BMW has a lower average price on our platform simply because the listed models have a much higher average mileage usage than competitors. This helps managers make smart, risk-adjusted pricing decisions.