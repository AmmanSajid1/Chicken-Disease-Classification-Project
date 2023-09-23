import sys
from src.Chicken_Disease_Classifaction_Project.config.configuration import ConfigurationManager
from src.Chicken_Disease_Classifaction_Project.components.data_ingestion import DataIngestion
from src.Chicken_Disease_Classifaction_Project.logger import logging
from src.Chicken_Disease_Classifaction_Project.exception import CustomException

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

    except Exception as e:
        raise CustomException(e,sys)