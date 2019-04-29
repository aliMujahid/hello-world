import feedparser
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml', 'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest', 'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route('/<name>')
def user(name):
    user_agent = request.headers.get('user_agent')
    return render_template('user.html', name=name, user_agent=user_agent)


@app.route('/headline')
def get_news_feed():
    quary = request.args.get("publication")
    if not quary or quary.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = quary.lower()
    head = publication.upper()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template('news_feed.html',head=head, articles=articles)

@app.route('/')
def index():

    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_servee_error(e):
    return render_template('500.html'), 500