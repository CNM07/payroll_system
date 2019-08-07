#import flask sqlalchemy object from main file
from app import db

class EmployeesModel(db.Model):
    __tablename__ = 'Employees'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(35), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    KRA_pin = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    national_ID = db.Column(db.String(15), unique=True, nullable=False)
    department_ID = db.Column(db.Integer,db.ForeignKey('Departments.id'))
    basic_salary = db.Column(db.Float(10))
    benefits = db.Column(db.Float(10))

    # create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_mail(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id = id).first()










    # @classmethod
    # def fetch_all(cls):
    #     return cls.query.all()
    #
    # @classmethod
    # def fetch_by_department(cls, dept_id):
    #     return cls.query.filter_by(department_ID=dept_id)