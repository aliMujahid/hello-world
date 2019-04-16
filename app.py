from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<name>')
def user(name):
    user_agent = request.headers.get('user_agent')
    return render_template('user.html', name=name, user_agent=user_agent)

@app.route('/')
def index():
    return render_template('index.html')

