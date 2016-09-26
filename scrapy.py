
#####
# YourName .~= ruichao zhang  =~.
###

import urllib
import re
import requests
from pattern import web
import pandas as pd
from bs4 import BeautifulSoup 
import networkx as nx
import timeit
import sys
import multiprocessing
import threading
import math
import os
import Queue
import time
import logging

NumErr = 0
DEBEG = 0
# read the website
defaultUrl = "http://www.whosdatedwho.com/dating/"
sampleUrl = ["http://www.whosdatedwho.com/dating/gregg-sulkin","http://www.whosdatedwho.com/dating/bella-thorne"]
# htmlfile = urllib.urlopen('http://www.whosdatedwho.com/')
# htmltext = htmlfile.read()
# i = 0
# get inside title tag 

testname = "Jake T. Austin"
p = re.split(r'[;,.\s]\s*',testname)
# print type("-".join(p))
regex = '<a href="/dating/gregg-sulkin">Gregg Sulkin</a>'
pattern = re.compile(regex)



# scrapy the first 100 popular start on the list  http://www.whosdatedwho.com/popular

def parse_name_inside_link(link):
	return link.split("/")[-1]
# print parse_name_inside_link("http://www.whosdatedwho.com/dating/taylor-swift")

def get_popular_celerbities(html):
	link = html
	r = requests.get(link)
	soup = BeautifulSoup(r.text,"html.parser")
	singlePerson = soup.body.find("div",class_="ff-box-grid ff-medium-square")
	# print singlePerson.prettify()
	returnList = []
	for a in singlePerson.find_all('a', href=True):
		returnList.append(parse_name_inside_link(a["href"]).encode("utf-8"))
	return returnList	

# returnlink = ["hello"]
# returnlink+=get_100_popular_celerbities("http://www.whosdatedwho.com/popular?page=1")
# print returnlink
def get_100_popular_celebrities(html):
	returnList = []
	for i in range(1,10):
		subfix = "?page="+str(i)
		returnList+=get_popular_celerbities(html+subfix)
	return returnList

#input name of the person 

#output object of the person' relationship

# return list of relationship

def get_relationship(name):
	global NumErr
	link = defaultUrl+name
	# try:
	if DEBEG ==1 :
		start_time = timeit.default_timer()
		print "computation time is ",(timeit.default_timer() - start_time) ,"seconds process time"

	r = requests.get(link)
	# r.raise_for_status() 
	if r.status_code == requests.codes.ok:
		pass
	else :
	# except requests.exceptions.RequestException as e:    # This is the correct syntax
	# 	NumErr+=1
	# 	print "return none"
		return None

	if DEBEG ==1 :
		start_time = timeit.default_timer()

	soup = BeautifulSoup(r.text,"html.parser")
	relations = soup.body.find("p",class_="ff-auto-relationships")
	if relations is None :
		NumErr+=1
		return None
	resultSet = {}
	if DEBEG ==1 :
		print relations.prettify()
	######version2
	for item in relations.find_all("a"):


		relationName = parse_name_inside_link(item["href"]).encode("utf-8")
		try :
			year = re.findall('\d+', (item.next_sibling.get_text()).encode('utf-8'))
		except AttributeError:
			resultSet[relationName] = None
			continue
		ValueYear = tuple(map(lambda x : int(x),year))
		resultSet[relationName] =  ValueYear
	if DEBEG ==1 :
		print "computation time is ",(timeit.default_timer() - start_time) ,"seconds process time"

	######version1 
	# item = relations.find("a")
	# try:
	# 	relationName = parse_name_inside_link(item["href"]).encode("utf-8")
	# 	year = re.findall('\d+', (item.next_sibling.get_text()).encode('utf-8'))
	# 	ValueYear = tuple(map(lambda x : int(x),year))
	# 	resultSet[name] =  ValueYear
	# except AttributeError :
	# 	# print name
	# 	# return
	# 	resultSet[relationName] = None
	
	# while item.find_next_sibling("a") is not None :
	# 	item = item.find_next_sibling("a")
	# 	try:
	# 		relationName = parse_name_inside_link(item["href"]).encode("utf-8")
	# 		year = re.findall('\d+', (item.next_sibling.get_text()).encode('utf-8'))
	# 	except AttributeError :
	# 		resultSet[relationName] = None
	# 		continue
		
	# 	ValueYear = tuple(map(lambda x : int(x),year))
	# 	resultSet[relationName] = ValueYear
	if DEBEG ==1 :
		print resultSet
	return resultSet

	# resultSet = []
	# for e in relations:a[1].next_sibling.get_text()
	# 	resultSet[e.a.get_text()] = {}
	# for k in relations[0].find_all("a")[1:]:
	# 	name = k.get_text().split()
		# print "http://www.whosdatedwho.com/dating/"+name[0]+"-"+name[1]
	# parse name to format xxx-x-xxx
	# for k in relations.a[:]:
	# 	p = re.split(r'[;,.\s]\s*',k.get_text())
	# 	name = "-".join(p)
	# 	resultSet.append({"name": name})



	# print resultSet
	

cacheName = get_100_popular_celebrities("http://www.whosdatedwho.com/popular")

def get_100_popular_celebrities_relationship(html):
	start_time = timeit.default_timer()
	# returnList = get_100_popular_celebrities(html)

	# stopTime = time.clock()
	returnList = cacheName
	# print "computation for getting 100 name",(stopTime-startTime) ,"seconds process time"
	result = {}
	for name in returnList[0:10]:
		result[name] = get_relationship(name)
	# result[returnList[1]] = get_relationship(returnList[0])
	print "computation time is ",(timeit.default_timer()-start_time) ,"seconds process time"
	return result

def work(num):
		"""worker function"""
		start_time = timeit.default_timer()
		print 'worker',num
		returnList = cacheName
		# print "computation for getting 100 name",(stopTime-startTime) ,"seconds process time"
		result = {}
		for name in returnList[num*10:(num*10+10)]:
			result[name] = get_relationship(name)
		print "computation time for worker ",num,"  ",(timeit.default_timer()-start_time) ,"seconds process time"
		# print result
		return result


def thread_on_worker(nums,nthreads):

	def worker(num,outdict):
	# http://eli.thegreenplace.net/2012/01/16/python-parallelizing-cpu-bound-tasks-with-multiprocessing/
		outdict[num] = work(num)

		print 'Worker: %s' % num
    	# return

	threads = []
	outs = [{} for i in range(nthreads)]

	for i in range(nums):
	    t = threading.Thread(target=worker, args=(i,outs))
	    threads.append(t)
	    t.start()
	for t in threads:
		t.join()
	# print "dict len",len(outs)
	return outs

if __name__ == '__main__':

	# test()

	# jobs = []
	# for i in range(10):
	# 	p = multiprocessing.Process(target=worker,args=(i,))
	# 	jobs.append(p)
	# 	p.start()	
	out = thread_on_worker(10,10)
	print out[5]
	# main(cacheName)
	# threads = []
	# for i in range(5):
	# 	t = threading.Thread(target=worker, args=(i,))
	# 	threads.append(t)
	# 	t.start()
	# print "threadlist",threads

	# 
# output the dictionary of the person's relationship
# print get_relationship("justin-bieber")
# print get_100_popular_celebrities_relationship("http://www.whosdatedwho.com/popular")
# print NumErr
# try:
# 	r = requests.get("http://www.whosdatedwho.com/popular")
# 	r.raise_for_status()
# 	print "sucess"
# 	# if r.status_code == 404 :

# except requests.exceptions.RequestException as e:    # This is the correct syntax
# 	NumErr+=1
# 	print e
# 	sys.exit(1)




if DEBEG is 1:
	result = {}
	result["bella-thorne"] = get_relationship("bella-thorne")
	print "hello"
# result["Britt-Robertson"] = temp
# for i in temp:
# 	print i 
# 	result["Britt-Robertson"][str(i)] = get_relationship(i)
	print result
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
	# for e in relations:
	# 	resultSet[e.a.get_text()] = {}
	for k in relations[0].find_all("a")[1:]:
		name = k.get_text().split()
		print "http://www.whosdatedwho.com/dating/"+name[0]+"-"+name[1]
	resultSet[relations[0].a.get_text()]= [k.get_text()for k in relations[0].find_all("a")[1:]]

	print resultSet
	return resultSet
	### output to json format
		

	# relation = []
	# return relation

if DEBEG is 1:
	print get_relavant_relation("http://www.whosdatedwho.com/dating/Britt-Robertson")


#https://github.com/cs109/content/blob/master/HW5_solutions.ipynb

# parse the relavent content
# for i in range(0,2):
# 	htmlfile = urllib.urlopen(sampleUrl[i])
# 	htmltext = htmlfile.read()
# 	# titles = re.findall(pattern,htmltext)
# 	print htmltext
# structure data in dictionary format


# print htmltext