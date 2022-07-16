from flask import Flask, request, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:p%40ssw0rd1@mysqldb/test_mysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def inex():
    return 'Response Data'

@app.route('/anoter')
def inex1():
    return "Anoter Response"

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<para>')
def test_request1(para):
    return f'test_request:{para}'

@app.route('/try_html')
def try_html():
    return render_template("pri.html")

@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    return request.form

@app.route('/try_css')
def try_css():
    return render_template('./css.css')

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
