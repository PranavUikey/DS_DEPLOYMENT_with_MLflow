from end_2_end_ds_project.config.configuration import ConfigurationManager
from end_2_end_ds_project.components.model_trainer import ModelTrainer
from end_2_end_ds_project import logger

STAGE_NAME = 'Data Transformation stage'
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()



if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>> stage {STAGE_NAME} started  <<<<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx========x')
    except Exception as e:
        logger.exception(e)
        raise e