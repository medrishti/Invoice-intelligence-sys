# 📦 Vendor Invoice Intelligence System

### 🚀 AI-Driven Freight Cost Prediction & Invoice Risk Flagging

An AI-powered system that predicts freight costs for vendor invoices using purchase quantity and invoice value. It also flags high-risk invoices for manual review based on abnormal cost, freight, and delivery patterns.

🎯 **Impact:** Reduces manual review time by **60%**, minimizes financial risk, and improves operational efficiency.

---

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Business Objectives](#-business-objectives)
* [Data Sources](#-data-sources)
* [Exploratory Data Analysis](#-exploratory-data-analysis)
* [Models Used](#-models-used)
* [Evaluation Metrics](#-evaluation-metrics)
* [Application](#-application)
* [Project Structure](#-project-structure)
* [How to Run This Project](#-how-to-run-this-project)
* [Future Improvements](#-future-improvements)
* [Author](#-author)

---

## 📖 Project Overview

This project implements an end-to-end machine learning system designed to support finance teams by:

* 📊 Predicting expected freight cost for vendor invoices
* 🚩 Flagging high-risk invoices requiring manual approval
* ⚡ Automating low-risk approvals to reduce workload

---

## 🎯 Business Objectives

* Reduce invoice processing time and manual effort
* Detect anomalies in freight cost and invoice patterns
* Improve financial control and audit readiness
* Enable smarter vendor negotiations using cost predictions

---

## 🗄 Data Sources

* **SQLite Database**: `inventory.db`
* Tables used:

  * `vendor_invoice`
  * `purchases`
  * `purchase_prices`

Data extracted using SQL queries and processed using Pandas.

---

## 📊 Exploratory Data Analysis

* Correlation heatmaps for feature relationships
* Outlier detection for abnormal invoice patterns
* Statistical testing (**t-tests**) for feature significance
* Distribution analysis of freight cost and invoice values

---

## 🤖 Models Used

### 🚚 Freight Cost Prediction (Regression)

* Linear Regression (**Best: 97% R²**)
* Decision Tree Regressor
* Random Forest Regressor

**Input Features:**

* Invoice Dollars
* Quantity

**Output:**

* Predicted Freight Cost

---

### 🚩 Invoice Risk Flagging (Classification)

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier (**Best: 89% Accuracy**)

**Feature Selection:**

* Based on t-tests and feature importance

**Input Features:**

* Total Item Quantity
* Invoice Quantity
* Total Item Dollars
* Invoice Dollars
* Freight Cost
* Days PO to Invoice

**Output:**

* Binary Flag

  * `0` → Auto Approval
  * `1` → Manual Review

---

## 📏 Evaluation Metrics

### Regression:

* R² Score
* Mean Squared Error (MSE)

### Classification:

* Accuracy
* Precision / Recall
* F1 Score (used in GridSearchCV)

---

## 💻 Application

Interactive **Streamlit dashboard** with:

* Sidebar-based model selection
* Real-time predictions
* Risk alerts and success messages
* Clean UI with metrics display

---

## 📂 Project Structure

```
Invoice-intelligence-sys/
├── data/
│   └── (raw data files)
│
├── notebooks/
│   └── Predicting-Freight-cost.ipynb
│
├── freight-cost-prediction/
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   ├── train.py
│   ├── check_db.py
│   ├── models/
│   │   └── Predicting-Freight-cost.pkl
│   ├── __pycache__/
│   └── .ipynb_checkpoints/
│
├── Invoice_flagging/
│   ├── data_preprocessing_IF.py
│   ├── model_evaluation_IF.py
│   ├── train_IF.py
│   ├── models/
│   │   ├── predicing_flag_invoice.pkl
│   │   └── scalar.pkl
│   ├── __pycache__/
│   └── .ipynb_checkpoints/
│
├── inference/
│   ├── Predict_freight.py
│   ├── Predict_invoice_flag.py
│   └── .ipynb_checkpoints/
│
├── app.py (Streamlit web application)
│
├── README.md (project documentation)
│
├── .gitignore (git exclusions)
│
└── .git/ (version control)

---

## ⚙️ How to Run This Project

```bash
# Clone repository
git clone <your-repo-url>
cd vendor_invoice_intelligence

# Install dependencies
pip install -r requirements.txt

# Add database
Place inventory.db inside /data folder

# Train models
cd freight_cost_prediction
python train.py

cd ../invoice_flagging
python train.py

# Run application
streamlit run app.py
```

---

## 🧪 Usage Instructions

1. Open the Streamlit app
2. Select model from sidebar:

   * Freight Cost Prediction
   * Invoice Risk Flagging
3. Enter input values
4. Click submit
5. View prediction results instantly

---

## 📸 Screenshots

<img src="C:\Users\VBdri\OneDrive\Pictures\Screenshots\Screenshot 2026-04-03 023138.png" class='fit-picture'></img>

---

## 🔮 Future Improvements

* Add logging & monitoring pipeline
* Deploy using FastAPI + cloud infrastructure
* Improve regression model tuning
* Add vendor-level feature engineering
* Implement authentication & role-based access
* Enable batch invoice processing

---

## 👤 Author

* GitHub: [https://github.com/medrishti]
* LinkedIn: [https://www.linkedin.com/in/drishti-kumari-ba7188293/]

---


