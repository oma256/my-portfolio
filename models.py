from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    date_of_birth = Column(Date)
    phone_number = Column(String(20))
    address = Column(String(512))
    about = Column(String(512))
    email = Column(String(128))


class Position(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    name = Column(String(128))
    description = Column(String(512))
    freelance = Column(Boolean, default=False)


class Skill(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    level = Column(Integer)
    position_id = Column(Integer, ForeignKey(Position.id))


class Resume(db.Model):
    id = Column(Integer, primary_key=True)
    description = Column(String(512))
    position_id = Column(Integer, ForeignKey(Position.id))


class Summary(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    intro = Column(String(512))
    city = Column(String(128))
    email = Column(String(128))
    phone = Column(String(128))
    resume_id = Column(Integer, ForeignKey(Resume.id))


class Education(db.Model):
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey(Resume.id))
    name = Column(String(128))
    major = Column(String(128))
    description = Column(String(512))
    date_begin = Column(Date)
    date_end = Column(Date)
    city = Column(String(128))


class Experience(db.Model):
    id = Column(Integer, primary_key=True)
    position_name = Column(String(128))
    is_present = Column(Boolean, default=False)
    date_begin = Column(Date)
    date_end = Column(Date)
    location = Column(String(128))


class ExperienceDescription(db.Model):
    id = Column(Integer, primary_key=True)
    experience_id = Column(Integer, ForeignKey(Experience.id))
    description = Column(String(512))
