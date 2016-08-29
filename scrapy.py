import urllib
import re
import requests
from pattern import web
import pandas as pd
from bs4 import BeautifulSoup 
# read the website


sampleUrl = ["http://www.whosdatedwho.com/dating/gregg-sulkin","http://www.whosdatedwho.com/dating/bella-thorne"]
# htmlfile = urllib.urlopen('http://www.whosdatedwho.com/')
# htmltext = htmlfile.read()
# i = 0
# get inside title tag 
regex = '<a href="/dating/gregg-sulkin">Gregg Sulkin</a>'
pattern = re.compile(regex)

def get_relavant_relation(html):
	# dom = web.Element(html)
	### 0. get the website
	### 1. get the relation
	# print dom.by_tag
	r = requests.get(html)
	soup = BeautifulSoup(r.text)
	# bs.find_all("div",class= "ff-current-relationship.ff-has-readmore")
	# print bsText.findall
	# cssSoup = bs("<div class = ff-current-relationship.ff-has-readmore>")
	# print soup.find_all("div")
	### get the css soup
	relations = soup.body.find_all("div",class_="ff-current-relationship")
	print type(relations)
	print "####\n"
	print relations


	# relation = []
	# return relation
get_relavant_relation("http://www.whosdatedwho.com/dating/gregg-sulkin")

# parse the relavent content
# for i in range(0,2):
# 	htmlfile = urllib.urlopen(sampleUrl[i])
# 	htmltext = htmlfile.read()
# 	# titles = re.findall(pattern,htmltext)
# 	print htmltext
# structure data in dictionary format




# print htmltext