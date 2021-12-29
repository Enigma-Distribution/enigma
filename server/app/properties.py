import os
import psycopg2
import traceback
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()
    print("Environment Loaded from .env file")
else:
    print("Environment Variables will be used directly from environment.")

postgres_url = os.getenv("POSTGRESURL")
secret_key = os.getenv("SECRET")
bucket_name = os.getenv("BUCKET_NAME")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
aws_session_token = os.getenv("aws_session_token")


__PG_CONNECTION__ = None
try:
    __PG_CONNECTION__ = psycopg2.connect(postgres_url)
    print("Connected to Database Successfully")
except Exception as e:
    traceback.print_exc()
    print("Error Connecting Database")

# Getter Methods
def get_pg_connection():
    return __PG_CONNECTION__

def get_site_secret_key():
    return secret_key

def get_s3_bucket_name():
    return bucket_name

def get_aws_access_key_id():
    return aws_access_key_id

def get_aws_secret_access_key():
    return aws_secret_access_key

def get_aws_session_token():
    return aws_session_token