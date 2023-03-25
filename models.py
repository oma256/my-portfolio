from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    date_of_birth = Column(Date)
    phone_number = Column(String(20))
    address = Column(String(512))
