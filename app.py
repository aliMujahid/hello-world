from flask import Flask, request

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    user_agent = request.headers.get('user_agent')
    return f"<h1> Hello, {name}</h1><p> Your browser is {user_agent}.</p>"

@app.route('/')
def index():
    return f"<h1>Hello world.</h1>"

    