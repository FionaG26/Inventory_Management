import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name):
    """Retrieve environment variable or return default value"""
    return os.getenv(var_name, None)
