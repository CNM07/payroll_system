#importing Flask class from flask Lib
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development, Testing

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
@app.route('/')
#function to run when clients visit this route
def hello_world():
    return render_template('flask.html')

@app.route('/name')
def name():
    return 'Name: Jane Doe!'

# run Flask
# if __name__ == '__main__':
#     app.run()
