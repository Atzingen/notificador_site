import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, select, and_

engine = db.create_engine('sqlite:///base.db')
metadata_obj = MetaData()

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
    
def get_all_sites():
    conn = engine.connect()
    query = select(user.columns.user_telegram_id, 
                   user.columns.site_name,
                   user.columns.site_url, 
                   user.columns.site_hash)
    result = conn.execute(query).all()
    conn.close()
    return result

def check_user_exists(user_id: int):
    conn = engine.connect()
    query = db.select(user).where(user.c.user_telegram_id == user_id)
    # result = conn.execute(query).all() != []
    result = conn.execute(query).first() is not None
    conn.close()
    return result
    
def get_notifications_list(user_id: int):
    conn = engine.connect()
    query = select(user.columns.site_name, user.columns.site_url).\
                   where(user.c.user_telegram_id == user_id)
    result = conn.execute(query).all()
    conn.close()
    return result

def get_site_hash(user_id: int, site_name: str):
    conn = engine.connect()
    query = select(user).where(and_(user.c.user_telegram_id == user_id,
                                    user.c.site_name == site_name))
    result = conn.execute(query).fetchone()
    conn.close()
    return result

def insert_notification(user_id: int, site_name: str, 
                        site_url: str, site_hash: str):  
    conn = engine.connect()
    query = db.insert(user).values(user_telegram_id=user_id, site_name=site_name, 
                                   site_url=site_url, site_hash=site_hash)
    result = conn.execute(query)
    conn.commit()
    conn.close()
    return result
    
def delete_notification(user_id: int, site_name: str):
    conn = engine.connect()
    query = db.delete(user).where(user.c.user_telegram_id == user_id).where(user.c.site_name == site_name)
    result = conn.execute(query).rowcount > 0
    conn.commit()
    conn.close()
    return result

def delete_user(user_id: int):
    conn = engine.connect()
    query = db.delete(user).where(user.c.user_telegram_id == user_id)
    result = conn.execute(query).rowcount > 0
    conn.commit()
    conn.close()
    return result
