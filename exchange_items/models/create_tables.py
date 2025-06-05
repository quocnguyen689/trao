from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from exchange_items.config.db_config import db_config
from exchange_items import db, create_app

def init_db():
    """Initialize database and create all tables"""
    # Create database URL
    db_url = f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['hostPort']}/{db_config['database']}"
    
    # Create engine
    engine = create_engine(db_url)
    
    # Create database if it doesn't exist
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Created database: {db_config['database']}")
    
    # Create Flask app and push context
    app = create_app()
    with app.app_context():
        # Import models here to avoid circular imports
        from exchange_items.models import Collection, Ad, User, UserActivity, Offer
        
        # Create all tables
        db.create_all()
        print("Created all tables successfully!")

if __name__ == "__main__":
    init_db() 