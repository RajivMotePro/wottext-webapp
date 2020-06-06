from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search')
def search():
	query = request.args.get('query')
	return render_template('search-results.html', query=query)

app.run(debug=True)
