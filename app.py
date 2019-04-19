from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/<name>')
def user(name):
    user_agent = request.headers.get('user_agent')
    return render_template('user.html', name=name, user_agent=user_agent)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_servee_error(e):
    return render_template('500.html'), 500
