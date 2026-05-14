# Inventory Demand Forecasting with Holt-Winters

## 1. Project Overview
This project builds a time-series forecasting model to predict logistics inventory demand using the Holt-Winters exponential smoothing method.

The goal is to help warehouse managers estimate future demand, reduce stockout risk, and improve replenishment planning.

## 2. Business Problem
Inventory demand often shows both trend and seasonality. Without a forecasting model, companies may face:
- Overstocking and higher storage costs
- Stockouts and delayed delivery
- Poor quarterly purchasing plans

## 3. Dataset
The dataset contains simulated logistics sales records from 2022 to 2025.

Main fields:
- Date
- Sales_Quantity
- Monthly_Sales
- 7_Day_Moving_Average

Note: The current version uses simulated data for demonstration. Future versions will replace it with real business or public retail/logistics data.

## 4. Methodology
- Data generation / data loading
- Daily-to-monthly resampling
- Moving average smoothing
- Train-test split
- Holt-Winters exponential smoothing
- Forecast evaluation using MAE

## 5. Tools
- Python
- pandas
- numpy
- matplotlib
- statsmodels
- scikit-learn

## 6. Key Results
- Built a demand forecasting model based on 4 years of daily sales data.
- Captured trend and seasonality in logistics demand.
- Evaluated model performance using Mean Absolute Error.
- Generated visual reports to support inventory planning decisions.

## 7. How to Run
```bash
pip install -r requirements.txt
python src/forecast_holt_winters.py
