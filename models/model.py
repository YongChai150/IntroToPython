from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#create a new database with name course
db = SQLAlchemy()

class Location(db.Model):
    __abstract__ = True
    longtitude = db.Column(db.String(200),nullable=False)
    latitude = db.Column(db.String(200),nullable=False)
    name = db.Column(db.String(200),nullable=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

class Weather(Location):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Numeric(precision=10, scale=2),nullable=False,default=30)
    

class HistoricalPlace(Location):
    __tablename__ = 'historicalplace'
    id = db.Column(db.Integer, primary_key=True)
    tourists = db.Column(db.Integer)