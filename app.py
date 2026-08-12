import os
import sys
import pandas as pd
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response, RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.pipeline.batch_prediction import start_batch_prediction
from networksecurity.utils.main_utils.utils import load_object

app = FastAPI(
    title="Network Security ML Project",
    description="Machine Learning Pipeline & Prediction API for Network Phishing Security"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train", tags=["Pipeline"])
async def train_route():
    try:
        pipeline = TrainingPipeline()
        artifact = pipeline.run_pipeline()
        return Response(f"Training completed successfully! Artifact: {artifact}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

@app.post("/predict", tags=["Prediction"])
async def predict_route(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        
        # Save temp input file
        input_dir = "prediction_input"
        os.makedirs(input_dir, exist_ok=True)
        input_path = os.path.join(input_dir, file.filename)
        df.to_csv(input_path, index=False)

        # Run batch prediction
        output_path = start_batch_prediction(input_file_path=input_path)
        
        # Read output dataframe
        df_predicted = pd.read_csv(output_path)
        table_html = df_predicted.to_html(classes="table table-striped", index=False)

        return HTMLResponse(content=f"""
            <html>
                <head>
                    <title>Prediction Results</title>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
                </head>
                <body class="container py-5">
                    <h2>Network Security Prediction Results</h2>
                    <p>File processed: <code>{file.filename}</code></p>
                    <div class="table-responsive">{table_html}</div>
                    <a href="/docs" class="btn btn-primary mt-3">Back to API Docs</a>
                </body>
            </html>
        """)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
