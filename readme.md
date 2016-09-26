This is a web scrapyer for http://www.whosdatedwho.com/

current implemented feature 
* scrapy top 100 celebrities from [who is dating who](https://facebook.github.io/relay/docs/getting-started.html)
* 10 working thread to request from the website 
* implemented timer to test scrapy speed

todo feature 
* display it as graph and edge 

getting the virtual environment
```
source test/bin/activate
```

```
python scrapy.py
```



#### current output format 
```
{'bella-thorne': [{'name': u'Gregg Sulkin', 'year': u' (2015 - 2016)'}, {'name': u'Ryan Nassif', 'year': u' (2015)'}, {'name': u'Brandon Thomas Lee', 'year': u' (2015)'}, {'name': u'Tristan Klier', 'year': u' (2012 - 2014)'}, {'name': u'Cody Simpson', 'year': u' (2011)'}, {'name': u'Garrett Backstrom', 'year': u' (2010 - 2011)'}, {'name': u'Jake T. Austin', 'year': u' (2010)'}]}
```
## MIT License