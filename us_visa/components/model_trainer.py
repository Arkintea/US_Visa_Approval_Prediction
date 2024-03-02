import json
import sys

import pandas as pd
import numpy as np
from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.utils.main_utils import read_yaml_file, write_yaml_file
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
from us_visa.entity.config_entity import DataValidationConfig, DataIngestionConfig, DataTransformationConfig
from sklearn.linear_model import LogisticRegression



class ModelTrainer:

    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            pass
  
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise USvisaException(e,sys)

        
    