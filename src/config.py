from dotenv import load_dotenv
import os

load_dotenv()
GRPC_ANALYTICS_ADDRESS = os.environ.get("GRPC_ANALYTICS_ADDRESS")
GRPC_USER_ADDRESS = os.environ.get("GRPC_USER_ADDRESS")
DATABASE_URL = os.environ.get("DATABASE_URL")
TEST_DATABASE_URL = os.environ.get("TEST_DATABASE_URL")

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
