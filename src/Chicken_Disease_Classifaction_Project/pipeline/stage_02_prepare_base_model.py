from Chicken_Disease_Classifaction_Project.config.configuration import ConfigurationManager
from Chicken_Disease_Classifaction_Project.components.prepare_base_model import PrepareBaseModel
from Chicken_Disease_Classifaction_Project.logger import logging
from Chicken_Disease_Classifaction_Project.exception import CustomException
import sys

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
        

    except Exception as e:
        raise CustomException(e,sys)