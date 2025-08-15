import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    user = quote_plus(os.getenv('MYSQL_USER'))
    password = quote_plus(os.getenv('MYSQL_PASSWORD'))
    host = os.getenv('MYSQL_HOST', 'localhost')
    port = os.getenv('MYSQL_PORT', '3306')
    db = os.getenv('MYSQL_DB')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False