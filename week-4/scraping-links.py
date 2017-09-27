# Some code for scraping the links from a website
# you will need to run in terminal: pip install bs4 and pip install requests
from bs4 import BeautifulSoup
import requests, csv

result = requests.get("http://www.gawker.com/") #change this to whatever site you
c = result.content
soup = BeautifulSoup(c, "html5lib")

links = []
for link in soup.find_all("a"):
	links.append(link.get('href'))

print len(links)
print links.content

with open ("all_links.csv", "w") as f:
	writer = csv.writer(f)
	for link in links:
		writer.writerow([link])