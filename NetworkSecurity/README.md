# Network Security ML Project

This repository contains a Machine Learning pipeline for Network Security, including data ingestion, validation, transformation, model training, and MLflow experiment tracking.

## Overview
- **Data Ingestion**: Fetches network data from MongoDB or local CSV fallback.
- **Data Validation**: Checks data schema, column types, and data drift using Evidently AI.
- **Data Transformation**: Preprocesses numeric data and handles missing values.
- **Model Trainer**: Trains classification models (Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost) and tracks metrics using MLflow / DagsHub.

## Setup Instructions

1. **Environment Setup**
   Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Pipeline**
   ```bash
   python main.py
   ```
