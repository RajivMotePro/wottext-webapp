from flask import Flask
from flask import render_template
from flask import request
import boto3

app = Flask(__name__)
kendra = boto3.client('kendra')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    kendraIndex = '2829b6aa-2333-450f-9bf2-584afba7a37c'
    response = kendra.query(QueryText = query, IndexId = kendraIndex)
    # TODO
    # Render page
    return render_template('search-results.html', query=query)

@app.route('/book')
def book():
    bookNum = request.args.get('bkNum')
    title = "TODO Fetch title"
    return render_template('book.html', bkNum=bookNum, title=title)

@app.route('/chapter-entities')
def chapter_entities():
    bookNum = request.args.get('bkNum')
    chapterNum = request.args.get('chNum')
    return render_template('chapter-entities.html', bkNum=bookNum, chNum=chapterNum)

@app.route('/chapter-topics')
def chapter_topics():
    bookNum = request.args.get('bkNum')
    chapterNum = request.args.get('chNum')
    return render_template('chapter-topics.html', bkNum=bookNum, chNum=chapterNum)

@app.route('/chapter-sentiment')
def chapter_sentiment():
    bookNum = request.args.get('bkNum')
    chapterNum = request.args.get('chNum')
    return render_template('chapter-sentiment.html', bkNum=bookNum, chNum=chapterNum)

app.run(debug=True)
