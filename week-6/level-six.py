'''
Take Matt and Asad's code form last week and do the following things:
  1. Turn it into a function.
  2. Once you've done that, get the function to run only if it's coming from standard input.
	(See here for help: https://docs.python.org/3/library/__main__.html)

P.S. Here's the photo url we used last week (thanks Lulu!): 'https://www.instagram.com/p/BY_fNlSnxTF/?taken-by=luluwiley'
'''
from bs4 import BeautifulSoup
import requests

print('Want to convert your Instagram photo into ASCII art?')

def instagram():
	url = raw_input('Enter your photo URL: ')
	result = requests.get(str(url))
	content = result.content
	soup = BeautifulSoup(content, "html.parser")
	url= soup.find("meta", property="og:image")
	result1 = requests.get(url["content"]+".html")
	content1 = result1.content
	soup1 = BeautifulSoup(content1, "html.parser")

	with open ("ASCII.html", "w") as f: 
		f.write(str(soup1))
		print 'DONE! Check your directory!' 

if __name__ == "__main__":
    # execute only if run as a script
    instagram() 

