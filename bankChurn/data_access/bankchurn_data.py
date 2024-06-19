from bankChurn.configuration.mongodb_connection import MongoDBClient
from bankChurn.constants import DATABASE_NAME
from bankChurn.exception import BankChurnException
from bankChurn.logger import logging
import sys
import pandas as pd
import numpy as np
from typing import Optional


class BankChurnData:
    """
    Bank Churn Data class exports entire mongodb records as panda dataframe 
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise BankChurnException(e, sys)
            
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns.to_list():
                df.drop('_id', axis=1, inplace=True)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise BankChurnException(e, sys)
