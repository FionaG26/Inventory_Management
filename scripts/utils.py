import os

def get_env_variable(var_name):
    """Retrieve environment variable or return default value"""
    return os.getenv(var_name, None)
