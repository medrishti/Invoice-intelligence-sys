# Invoice Intelligence System

## Table of Contents
- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Models Used](#models-used)
- [Evaluation Metrics](#evaluation-metrics)
- [Application](#application)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [Future Improvements](#future-improvements)

## Project Overview

Invoice Intelligence System is a solution to support vendor invoice verification and freight cost planning. It combines data ingestion from a SQLite database, preprocessing, ML model training, and an interactive Streamlit application for prediction.

## Business Objectives

- Detect risky invoices requiring manual approval.
- Predict freight cost for incoming invoices.
- Reduce fraud and improve finance operations efficiency.
- Provide a productionized UI for business users.

## Data Sources

- `inventory.db` (SQLite): key tables include `vendor_invoice` and `Purchases`.
- Feature aggregation via SQL query (PO-level total quantity, total dollars, avg receiving delay).

## Exploratory Data Analysis

- Summary statistics: quantity, dollars, freight, payment delays.
- Correlation analysis and feature relationship inspection.
- Cleaned invalid rows, engineered delay, difference, and ratio features.

## Models Used

- RandomForestClassifier (invoice risk flagging) with GridSearchCV.
- RandomForestRegressor or LinearRegression (freight cost prediction) in freight pipeline.

## Evaluation Metrics

- Classification: accuracy, precision, recall, F1-score, confusion matrix.
- Regression: MAE, MSE, RMSE.

## Application

- `app.py`: Streamlit UI with two modules:
  - Freight cost prediction (Quantity + Invoice Dollars -> estimated freight)
  - Invoice risk flagging (invoice details -> safe/manual review)

## Project Structure

- `Invoice_flagging/`
  - `data_preprocessing_IF.py`
  - `model_evaluation_IF.py`
  - `train_IF.py`
  - `models/` (trained models & scalers)
- `freight-cost-prediction/`
  - preprocessing, model training for freight prediction
- `inference/`
  - `Predict_freight.py`, `Predict_invoice_flag.py`
- `app.py` (Streamlit app entry point)
- `README.md` (this file)

## How to Run This Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train models (if not already trained):
   - `python Invoice_flagging/train_IF.py`
   - `python freight-cost-prediction/train.py`
3. Run app:
   ```bash
   python -m streamlit run app.py
   ```
4. Validate inferences at:
   - `python inference/Predict_freight.py`
   - `python inference/Predict_invoice_flag.py`

## Future Improvements

- Add test automation and CI pipeline.
- Add drift monitoring and feature tracking.
- Implement API endpoint for inference (FastAPI/Flask).
- Add quantile regression for freight uncertainty.
- Add production deployment docs and Docker compose.
