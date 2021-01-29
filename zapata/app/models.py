from database import db


class Incident(db.Model):
    __tablename__ = "incidents"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


class Fee(db.Model):
    __tablename__ = "fees"
    id = db.Column(db.Integer, primary_key=True)
    yearly = db.Column(db.Integer)
