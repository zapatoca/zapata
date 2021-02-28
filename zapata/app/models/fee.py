from database import db


class Fee(db.Model):
    __tablename__ = "fees"
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    Apartment = db.Column(db.Integer, nullable=False)
    Fee_type = db.Column(db.String, nullable=False)
    Amount = db.Column(db.Integer, nullable=False)
    project = db.Column(
        db.Integer, db.ForeignKey("projects.id"), nullable=False
    )
    Jan = db.Column(db.Integer, nullable=False)
    Feb = db.Column(db.Integer, nullable=False)
    Mar = db.Column(db.Integer, nullable=False)
    Balance = db.Column(db.Integer, nullable=False)
    Alert = db.Column(db.Boolean, nullable=False)

    def __init__(self, Apartment, Fee_type, Amount, project):
        self.Apartment = Apartment
        self.Fee_type = Fee_type
        self.Amount = Amount
        self.project = project
        self.Jan = 0
        self.Feb = 0
        self.Mar = 0
        self.Balance = 0
        self.Alert = True
