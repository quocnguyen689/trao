import requests
import time
from sqlalchemy import create_engine, Column, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Database setup
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/trao')
engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# sk-3t1Q8UHt37NKgVyrEmtCsQ


class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    ad_id = Column(Integer, unique=True)
    list_id = Column(Integer)
    subject = Column(String)
    price = Column(Float)
    category_name = Column(String)
    area_name = Column(String)
    region_name = Column(String)
    body = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    location = Column(String)  # e.g., "Hanoi, Vietnam"

    raw_data = Column(JSON)

Base.metadata.create_all(engine)

def fetch_ad(ad_id):
    url = f"https://gateway.chotot.com/v2/public/ad-listing/{ad_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error fetching ad {ad_id}: {e}")
        return None

def save_ad(ad_data):
    session = Session()
    try:
        if not ad_data or 'ad' not in ad_data:
            return False
            
        ad_info = ad_data['ad']
        ad = Ad(
            ad_id=ad_info.get('ad_id'),
            list_id=ad_info.get('list_id'),
            subject=ad_info.get('subject'),
            price=ad_info.get('price'),
            category_name=ad_info.get('category_name'),
            area_name=ad_info.get('area_name'),
            region_name=ad_info.get('region_name'),
            body=ad_info.get('body'),
            longitude=ad_info.get('longitude'),
            latitude=ad_info.get('latitude'),
            location=ad_info.get('location'),
            raw_data=ad_data
        )
        
        session.merge(ad)
        session.commit()
        return True
    except Exception as e:
        print(f"Error saving ad: {e}")
        session.rollback()
        return False
    finally:
        session.close()

def crawl_ads(start_id, count=100):
    success = 0
    current_id = start_id
    
    while success < count:
        print(f"Fetching ad {current_id}...")
        ad_data = fetch_ad(current_id)
        
        if ad_data:
            if save_ad(ad_data):
                success += 1
                print(f"Saved ad {current_id} ({success}/{count})")
            
        current_id += 1
        time.sleep(1)  # Rate limiting
        
    print(f"Completed! Saved {success} ads")

if __name__ == "__main__":
    start_id = 125459659  # Example starting ID
    crawl_ads(start_id, 100) 