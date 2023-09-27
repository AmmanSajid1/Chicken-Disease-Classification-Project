from Chicken_Disease_Classifaction_Project.exception import CustomException
from Chicken_Disease_Classifaction_Project.config.configuration import ConfigurationManager
from Chicken_Disease_Classifaction_Project.components.evaluation import Evaluation
from Chicken_Disease_Classifaction_Project.logger import logging
import sys



STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logging.info(f"*********************")
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")

    except Exception as e:
        raise CustomException(e,sys)
