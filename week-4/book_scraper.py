## code for getting the word count from a project gutenberg book
from bs4 import BeautifulSoup
from collections import Counter 
import requests

url = "https://www.gutenberg.org/files/345/345-h/345-h.htm" 
result = requests.get(url) #change this to whatever site you want
c = result.content
soup = BeautifulSoup(c, "html.parser")

def get_text(url, text_file):
	text_on_site = (soup.get_text().encode('utf-8'))
	with open(text_file, "w") as file:
		file.write(text_on_site)
	print "Check directory for file"

def get_word_count(text_file, wordcount_file):
	with open(text_file) as f:
		wordcount = str(Counter(f.read().split()))
	with open(wordcount_file, "wb") as file:
		file.write(str(wordcount))
	print "Check directory for file"


# get_text(url, "story_text.txt")
get_word_count("story_text.txt", "word_count.txt")