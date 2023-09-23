from src.Chicken_Disease_Classifaction_Project.logger import logging
from src.Chicken_Disease_Classifaction_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Chicken_Disease_Classifaction_Project.exception import CustomException
from src.Chicken_Disease_Classifaction_Project.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Chicken_Disease_Classifaction_Project.pipeline.stage_03_training import ModelTrainingPipeline
import sys

STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

except Exception as e:
    raise CustomException(e,sys)


STAGE_NAME = "Prepare Base Model"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

except Exception as e:
    raise CustomException(e,sys)


STAGE_NAME = "Training"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

except Exception as e:
    raise CustomException(e,sys)