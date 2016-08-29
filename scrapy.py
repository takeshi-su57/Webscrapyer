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
	soup = BeautifulSoup(r.text,"html.parser")

	# bs.find_all("div",class= "ff-current-relationship.ff-has-readmore")
	# print bsText.findall
	# cssSoup = bs("<div class = ff-current-relationship.ff-has-readmore>")
	# print soup.find_all("div")
	### get the css soup
	relations = soup.body.find_all("p",class_="ff-auto-relationships")
	print type(relations)
	print "####\n"

	### get the name of the relations
	resultSet = {}
	for e in relations:
		resultSet[e.a.get_text()] = {}
	for k in relations[0].find_all("a")[1:]:
		print k.get_text().split()
		print "http://www.whosdatedwho.com/dating/"+k.get_text().split()[0]+"-"+k.get_text().split()[1]
	resultSet[e.a.get_text()]= [k.get_text()for k in relations[0].find_all("a")[1:]]

	print resultSet

	### output to json format
		

	# relation = []
	# return relation
get_relavant_relation("http://www.whosdatedwho.com/dating/Britt-Robertson")

# parse the relavent content
# for i in range(0,2):
# 	htmlfile = urllib.urlopen(sampleUrl[i])
# 	htmltext = htmlfile.read()
# 	# titles = re.findall(pattern,htmltext)
# 	print htmltext
# structure data in dictionary format


# print htmltext