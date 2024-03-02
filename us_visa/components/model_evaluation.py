import json
import sys

import pandas as pd

from pandas import DataFrame

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.utils.main_utils import read_yaml_file, write_yaml_file
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelPusherArtifact
from us_visa.entity.config_entity import DataValidationConfig, DataIngestionConfig, DataTransformationConfig, ModelPusherConfig

from us_visa.constants import SCHEMA_FILE_PATH



class ModelEvaluation:

    
    def initiate_model_evaluation(self,):
        try:
            pass
  
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise USvisaException(e,sys)

        
    