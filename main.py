import sys
import os
sys.path.append(os.path.abspath("."))

from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__ == '__main__':
    try:
        pipeline = TrainingPipeline()
        logging.info("Initiating Training Pipeline...")
        model_trainer_artifact = pipeline.run_pipeline()
        print("Training Pipeline Executed Successfully!")
        print("Model Trainer Artifact:", model_trainer_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
