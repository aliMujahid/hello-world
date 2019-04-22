import feedparser
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

BBC_feed = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route('/<name>')
def user(name):
    user_agent = request.headers.get('user_agent')
    return render_template('user.html', name=name, user_agent=user_agent)

@app.route('/headline')
def get_news_feed():
    first_article =[]
    feed = feedparser.parse(BBC_feed)
    articles = feed['entries']
    return render_template('news_feed.html', articles=articles)

@app.route('/')
def index():

    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_servee_error(e):
    return render_template('500.html'), 500