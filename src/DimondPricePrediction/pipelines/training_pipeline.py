
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import ModelTrainer

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
import pandas as pd


obj = DataIngestion()
train_test_path,test_train_path = obj.intiate_data_ingestion()

data_transformation = DataTransformation()

train_arr, test_arr = data_transformation.initialize_data_transformation(train_test_path,test_train_path)

model_trainer_obj = ModelTrainer()

model_trainer_obj.initate_model_training(train_arr,test_arr)


