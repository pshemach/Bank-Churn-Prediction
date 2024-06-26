import os 

DATABASE_NAME = 'BankChurn'
COLLECTION_NAME = 'bank_data'

MONGODB_URL_KEY = 'MONGODB_URL'

PIPELINE_NAME: str = 'bankchurn'

ARTIFACT_DIR: str = 'artifacts'

MODEL_FILE_NAME = 'model.pkl'
TARGET_COLUMN = 'Exited'
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"


FILE_NAME: str = "bankchurn.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "bankchurn_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2