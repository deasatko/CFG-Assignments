import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database configuration
USER = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD_DB")
HOST = os.getenv("HOST_DB")
DATABASE = os.getenv("DATABASE_NAME")

