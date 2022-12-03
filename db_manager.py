import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String


engine = db.create_engine('sqlite:///base.db')
metadata_obj = MetaData()
conn = engine.connect()

user = Table(
    "notification",
    metadata_obj,
    Column("user_telegram_id", Integer, nullable=False),
    Column("site_name", String(100), nullable=False),
    Column("site_url", String(200), nullable=False),
    Column("site_hash", String(300), nullable=False),
)

def create_table():
    metadata_obj.create_all(engine)

def insert_notification(user_id: int, site_name: str, 
                        site_url: str, site_hash: str):  
    query = db.insert(user).values(user_telegram_id=user_id, site_name=site_name, site_url=site_url, site_hash=site_hash)
    conn.execute(query)