import os
import sys
import numpy as np
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import load_object

def start_batch_prediction(input_file_path: str, output_file_dir: str = "prediction_output") -> str:
    try:
        os.makedirs(output_file_dir, exist_ok=True)
        logging.info(f"Starting batch prediction for file: {input_file_path}")

        df = pd.read_csv(input_file_path)
        
        model_path = os.path.join("final_model", "model.pkl")
        if not os.path.exists(model_path):
            raise Exception(f"Trained model not found at {model_path}. Please run training pipeline first.")

        network_model = load_object(file_path=model_path)
        
        if "Result" in df.columns:
            df_input = df.drop(columns=["Result"], axis=1)
        else:
            df_input = df

        y_pred = network_model.predict(df_input)
        df["prediction"] = y_pred

        output_file_name = os.path.basename(input_file_path).replace(".csv", "_prediction.csv")
        output_file_path = os.path.join(output_file_dir, output_file_name)
        df.to_csv(output_file_path, index=False)

        logging.info(f"Batch prediction completed. Saved to: {output_file_path}")
        return output_file_path

    except Exception as e:
        raise NetworkSecurityException(e, sys)
