from app import db

class PayrollsModel(db.Model):
    __tablename__ = 'Payrolls'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20),nullable=False)
    gross_salary = db.Column(db.Float())
    overtime = db.Column(db.Float)
    loan_deducted = db.Column(db.Float)
    advance = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    taxable_income= db.Column(db.Float)
    PAYE = db.Column(db.Float)
    NHIF = db.Column(db.Float)
    NSSF = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    employee_id = db.Column(db.Integer,db.ForeignKey('Employees.id'))

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()