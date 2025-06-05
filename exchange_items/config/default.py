import json
import os
from loguru import logger
from exchange_items.config.db_config import db_config

try:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['hostPort']}/{db_config['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
except Exception as e:
    logger.warning(f"Failed to load config: {e}")
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "True") == "True"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://postgres:postgres@localhost:5432/trao",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
