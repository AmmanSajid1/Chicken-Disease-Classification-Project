from src.Chicken_Disease_Classifaction_Project.logger import logging
from src.Chicken_Disease_Classifaction_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Chicken_Disease_Classifaction_Project.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

except Exception as e:
    raise CustomException(e,sys)
