#importing Flask class from flask Lib
from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development, Testing
from resources.net_sal_calculator import KRACalculator

#Instantiating class Flask
app = Flask(__name__)

#this is a config parameter that shows where our database lives
#identifier of db://(missing part is driver/connecter/adapter-by default it is psychopg2)(sth sth):password@host:port/dbname
app.config.from_object(Development)
#app.config.from_object(Testing)

db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

@app.before_first_request
def create_tables():
    db.create_all()


#registering a route
#TODO:read about flask-migrate
@app.route('/')
#function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    return render_template('flask.html', idara=departments)

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    this_dept = DepartmentModel.fetch_by_id(dept_id)
    return render_template('employees.html', this_dept=this_dept)

@app.route('/payroll/<int:emp_id>')
def payroll(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payroll.html', employee=employee)

@app.route('/new_department', methods=['POST'])
def new_department():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        #read more on bootstrap alerts with flash
        flash('Department' + department_name + ' already exists.')
        return redirect(url_for('home'))
    department = DepartmentModel(name=department_name)
    department.insert_to_db()
    flash('Department ' + department_name + ' has been added.')
    return redirect(url_for('home'))

@app.route('/add_employee', methods=['POST'])
def new_employee():
    full_name = request.form['full_name']
    gender = request.form['gender']
    KRA_pin = request.form['KRA_pin']
    national_ID = request.form['national_ID']
    email = request.form['email']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    department_ID = int(request.form['department'])
    if EmployeesModel.fetch_by_mail(email):
        flash('Employee' + full_name + ' already exists.')
        return redirect(url_for('home'))
    emp = EmployeesModel(full_name = full_name, gender = gender, KRA_pin = KRA_pin,
                              email = email, national_ID = national_ID, basic_salary = basic_salary,
                              benefits = benefits, department_ID = department_ID)
    emp.insert_to_db()
    flash('Employee ' + full_name + ' has been added.')
    return redirect(url_for('home'))

@app.route('/generate_payroll/<int:id>', methods=['POST'])
def generate_payroll(id):
    this_employee = EmployeesModel.fetch_by_id(id)
    payroll = KRACalculator(this_employee.full_name, this_employee.basic_salary,this_employee.benefits)
    NHIF = payroll.NHIF
    NSSF = payroll.NSSF
    PAYE = payroll.PAYE
    gross_salary = payroll.gross_salary
    personal_relief = payroll.personal_relief
    taxable_income = payroll.taxable_income
    net_salary = payroll.net_salary
    
    return redirect(url_for('home'))


@app.route('/name')
def name():
    return 'Name: Jane Doe!'

# run Flask
# if __name__ == '__main__':
#     app.run()
