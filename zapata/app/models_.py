from database import db


class Incident(db.Model):
    __tablename__ = "incidents"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


class Building(db.Model):
    __tablename__ = "buildings"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    flats = db.Column(db.Integer)


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(80))
    budget = db.Column(db.Integer)
    fees = db.relationship("Fee", backref="project_fees")
