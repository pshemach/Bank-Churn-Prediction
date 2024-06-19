import sys

from bankChurn.exception import BankChurnException
from bankChurn.logger import logging

import os
import pymongo
import certifi
from bankChurn.constants import DATABASE_NAME, MONGODB_URL_KEY


ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if mongodb_url is None:
                    raise BankChurnException(
                        f"Environment variable {MONGODB_URL_KEY} is not set"
                    )
                MongoDBClient.client = pymongo.MongoClient(
                    mongodb_url, tlsCAFile=ca
                )
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise BankChurnException(e, sys)

