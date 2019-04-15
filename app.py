from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    return f"<h1> Hello, {name}</h1>"

@app.route('/')
def index():
    return f"<h1>Hello world.</h1>"