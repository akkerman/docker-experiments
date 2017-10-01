from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'p1: Hello, World!'

@app.route('/hi')
def hi_world():
    return 'p1: Hi, World!'
