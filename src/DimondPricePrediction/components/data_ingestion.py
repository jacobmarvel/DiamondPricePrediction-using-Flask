
import pandas as pd
import numpy as np 
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import os
import sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_test_path:str = os.path.join("artifacts","train.csv")
    test_train_path:str = os.path.join("artifacts","test.csv")
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","cubic_zirconia.csv")))
            logging.info("I have read the dataset as a dataframe")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("I have saved the raw daset in artifact folder")
            logging.info("Here I have performed train test split")

            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("Train test split completed")

            train_data.to_csv(self.ingestion_config.train_test_path,index=False)
            test_data.to_csv(self.ingestion_config.test_train_path,index=False)

            logging.info("Data ingestion part completed")

            return (
                self.ingestion_config.train_test_path,
                self.ingestion_config.test_train_path
            )

        except Exception as e:
            logging.info("Exception during occured at data ingestion stage")
            raise customexception(e,sys)

