from end_2_end_ds_project import logger
from end_2_end_ds_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from end_2_end_ds_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from end_2_end_ds_project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from end_2_end_ds_project.pipeline.stage_04_model_trainer import ModelTrainingPipeline



STAGE_NAME = 'Data Ingestion stage'


try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started  <<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx========x')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started  <<<<<<<')
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx========x')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started  <<<<<<<')
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx========x')
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = 'Model Training stage'



try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started  <<<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx========x')
except Exception as e:
    logger.exception(e)
    raise e