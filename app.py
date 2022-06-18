from flask import Flask
app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'

@app.route('/anoter')
def inex1():
    return "Anoter Response"