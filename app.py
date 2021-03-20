from bottle import route, run
import feedparser
import random

@route('/random')
def get_random():
    response = feedparser.parse("https://news.ycombinator.com/rss")
    entries = response["entries"]
    number_of_articles = len(entries)
    article_selected = random.randrange(number_of_articles)
    return entries[article_selected]

@route('/')
def get_ping():
    return("pong")

run(host='0.0.0.0', port=8072, debug=True)
