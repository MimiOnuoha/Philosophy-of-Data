'''
Python functions are intended to be short and have a single purpose. 

Take your code from the level-six example and change it so that it is split 
into two different functions. Make at least one of the functions take in 
something as a parameter.  

For help with parameters, see here: http://pythoncentral.io/fun-with-python-function-parameters/
'''

from bs4 import BeautifulSoup
import requests

print('Want to convert your Instagram photo into ASCII art?')

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

