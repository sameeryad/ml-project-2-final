

# Network Security ML Project

An end-to-end Machine Learning project for detecting phishing/network security threats.

## 🔄 Pipeline

```text
MongoDB
   ↓
Data Ingestion
   ↓
Data Validation + Drift Detection
   ↓
Data Transformation
   ↓
Model Training + Hyperparameter Tuning
   ↓
Best Model
   ↓
FastAPI Prediction
```

## 🛠️ Technologies

* Python
* Pandas / NumPy
* Scikit-learn
* MongoDB
* MLflow / DagsHub
* FastAPI
* Docker
* AWS S3 / ECR / EC2
* GitHub Actions

## 🤖 Models

* Random Forest
* Decision Tree
* Gradient Boosting
* Logistic Regression
* AdaBoost

The best model is selected based on evaluation results.

## 📊 Evaluation

* F1 Score
* Precision
* Recall

## 🚀 Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run training:

```bash
python main.py
```

Run API:

```bash
python app.py
```

API documentation:

```text
http://localhost:8000/docs
```

## 📁 Main Components

```text
components/
├── data_ingestion.py
├── data_validation.py
├── data_transformation.py
└── model_trainer.py

pipeline/
└── training_pipeline.py

app.py
main.py
Dockerfile
```

**One-line summary:**

> A modular end-to-end ML pipeline that ingests, validates, transforms, trains, evaluates, and serves a network-security classification model.
