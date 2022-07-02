from flask import Flask, request, render_template
from flask import request


app = Flask(__name__)
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