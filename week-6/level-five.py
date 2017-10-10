# There are several problems with this code. 
# Figure out what they are and fix them to get the program working.

from bs4 import BeautifulSoup
import requests
import csv

result = requests.get("http://bennington.works")
content = result.content
soup = BeautifulSoup(content, "html.parser") #might need to be "html5lib"

def get_text():
	text = (soup.get_text())
	with open("bennington_site.txt", "w") as f:
		f.write(text)
	print "Created text file!"

def get_links():
	links = soup.find_all('a')
	with open("page_links.txt", "w") as f:
		writer = csv.writer(f)
		for link in links:
			writer.writerow([link])
	print "Finished getting links!"	

 
get_text()