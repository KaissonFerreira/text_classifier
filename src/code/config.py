import pathlib
import os


BASE_DIR = pathlib.Path(__name__).parent.resolve()
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_RAW_DIR = os.path.join(DATA_DIR, 'raw')
DATA_EXTERNAL_DIR = os.path.join(DATA_DIR, 'external')
DATA_INTERIM_DIR = os.path.join(DATA_DIR, 'interim')
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
DATA_RAW_FILE = os.path.join(DATA_RAW_DIR, 'review.csv')

