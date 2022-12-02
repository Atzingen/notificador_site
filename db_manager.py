import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String


engine = db.create_engine('sqlite:///base.db')

metadata_obj = MetaData()

