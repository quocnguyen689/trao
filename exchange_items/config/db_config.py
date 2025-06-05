import os

db_config = {
    "username": os.getenv("DB_USERNAME", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "hostPort": os.getenv("DB_HOST", "localhost:5432"),
    "database": os.getenv("DB_NAME", "trao")
} 