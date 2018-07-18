import os
import urllib2
from bs4 import BeautifulSoup
import json

URL = 'https://codechef.com/users/'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

class User:
	handle = ''
	name = ''
	country = ''
	state = ''
	city = ''
	motto = ''
	link = ''
	group = ''
	institution = ''
	profile_img = ''
	rating = ''
	global_rank = ''
	country_rank = ''
	fully_solved = ''
	partially_solved = ''
	def serialize(self):
		return {'handle':self.handle, 'name':self.name, 'link':self.link, 'country':self.country, 'state':self.state, 'city':self.city, 'motto':self.motto, 'group':self.group, 'institution':self.institution, 'profile_img':self.profile_img, 'rating':self.rating, 'global_rank':self.global_rank, 'country_rank':self.country_rank, 'fully_solved':self.fully_solved, 'partially_solved':self.partially_solved}

def getUser(handle):
	user = User()
	req = urllib2.Request(URL + handle, headers={'User-Agent': user_agent})
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')

	is_motto = False
	is_link = False

	if soup.find_all('span')[6].string == handle:
		user.handle = handle
		# Retrieving profile image
		for link in soup.find_all('img'):
			if '/sites/default' in link.get('src'):
				user.profile_img = 'https://codechef.com' + link.get('src')
				break
		# Retrieving user's full name
		user.name = soup.find_all('h2')[1].string

		if 'Motto' in soup.text:
			is_motto = True
		if 'Link' in soup.text:
			is_link = True

		print(str(is_link) + " " + str(is_motto))
		val = 8
		user.country = soup.find_all('span')[val].string
		val+=1
		user.state = soup.find_all('span')[val].string
		val+=1
		user.city = soup.find_all('span')[val].string
		if(is_motto):
			val+=1
			user.motto = soup.find_all('span')[val].string
			if(is_link):
				val+=1
				user.link = soup.find_all('span')[val].string
		val+=1
		user.group = soup.find_all('span')[val].string
		val+=1
		user.institution = soup.find_all('span')[val].string

		user.rating = soup.find('div', class_="rating-number").string

		ranks = []
		for rank in soup.find_all('strong'):
			if rank.string == None:
				continue
			if rank.string.isdigit():
				print(rank.string)
				ranks.append(rank.string)

		user.global_rank = ranks[8]
		user.country_rank = ranks[9]

		user.fully_solved = soup.find_all('h5')[0].string.split('(')[1].split(')')[0]
		user.partially_solved = soup.find_all('h5')[1].string.split('(')[1].split(')')[0]

	return user.serialize()