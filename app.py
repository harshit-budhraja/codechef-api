# Author:- Harshit Budhraja
# Unofficial Codechef API
import os
import requests as re
from flask import Flask, jsonify
from flask_cors import CORS
from contests import parseContests

app = Flask(__name__)
CORS(app)
ALL_CONTESTS = 'all'
PRESENT_CONTESTS = 'present'
FUTURE_CONTESTS = 'future'
PAST_CONTESTS = 'past'

@app.route('/rankings/<contest>/<customFilter>')
def filtered_rankings(contest, customFilter):
	x = re.get('https://www.codechef.com/api/rankings/'+contest+'?sortBy=rank&order=asc&page=1&itemsPerPage=100&filterBy='+customFilter).json()
	return jsonify(result=x)

@app.route('/rankings/<contest>')
def all_rankings(contest):
	x = re.get('https://www.codechef.com/api/rankings/'+contest+'?sortBy=rank&order=asc&page=1&itemsPerPage=100').json()
	return jsonify(result=x)

@app.route('/contests/present')
def present_contests():
	x = parseContests(PRESENT_CONTESTS)
	return jsonify(result=x)

@app.route('/contests/past')
def past_contests():
	x = parseContests(PAST_CONTESTS)
	return jsonify(result=x)

@app.route('/contests/future')
def future_contests():
	x = parseContests(FUTURE_CONTESTS)
	return jsonify(result=x)

@app.route('/')
def root():
	x = re.get('https://harshitbudhraja.github.io/codechef-api/')
	return x.text

if __name__ == '__main__':
	app.run()