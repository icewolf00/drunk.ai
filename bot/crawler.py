import requests
from bs4 import BeautifulSoup

class Crawler():
	
	def get_from_web():
		url = 'https://drunk-ai.herokuapp.com/data.html'
		resp = requests.get(url)
		soup = BeautifulSoup(resp.text, 'html.parser')
		weed = soup.find_all('h1')
		return weed
		# image = weed[0].text
		# ratio = weed[1].text