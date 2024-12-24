import os
from end_2_end_ds_project import logger
from sklearn.model_selection import train_test_split
from end_2_end_ds_project.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def split(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'),index = False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'),index = False)

        logger.info(f"Splited data into training and testing sets")
        logger.info(f"{train.shape}")
        logger.info(f"{test.shape}")

        print(train.shape)
        print(test.shape)