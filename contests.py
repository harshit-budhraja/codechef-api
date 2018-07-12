import os
import urllib2
from bs4 import BeautifulSoup
import json

PRESENT_CONTESTS = 'present'
FUTURE_CONTESTS = 'future'
PAST_CONTESTS = 'past'
URL = 'https://codechef.com'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
present_contests = list()
all_contests = list()
past_contests = list()
future_contests = list() 

class Contest:
	code = ''
	name = ''
	start = ''
	end = ''
	def serialize(self):
		return {'code': self.code, 'name': self.name, 'start': self.start, 'end': self.end }

def parseContests(type):
	req = urllib2.Request(URL + '/contests', headers={'User-Agent': user_agent})
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')
	tables = soup.find_all('tbody')
	
	# CONDITIONAL CODE SNIPPET
	if type == PRESENT_CONTESTS:
		output = tables[0].text.strip()
	elif type == PAST_CONTESTS:
		output = tables[2].text.strip()
	elif type == FUTURE_CONTESTS:
		output = tables[1].text.strip()

	# GENERAL CODE SNIPPET
	lines = output.splitlines()
	for i in range(0,len(lines)-4,4):
		contest = Contest()
		contest.code = lines[i]
		contest.name = lines[i+1]
		contest.start = lines[i+2]
		contest.end = lines[i+3]
		# CONDITIONAL CODE SNIPPET
		if type == PRESENT_CONTESTS:
			present_contests.append(contest.serialize())
		elif type == PAST_CONTESTS:
			past_contests.append(contest.serialize())
		elif type == FUTURE_CONTESTS:
			future_contests.append(contest.serialize())

	# CONDITIONAL CODE SNIPPET
	if type == PRESENT_CONTESTS:
		return json.dumps(present_contests)
	elif type == PAST_CONTESTS:
		return json.dumps(past_contests)
	elif type == FUTURE_CONTESTS:
		return json.dumps(future_contests)
