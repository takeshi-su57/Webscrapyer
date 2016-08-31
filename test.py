import pandas as pd
# import matplotlib.pyplot as plt
import requests
from pattern import web
def get_population_html_tables(html):
    """Parse html and return html tables of wikipedia population data."""

    dom = web.Element(html)

    # 0. step: look at html source!
    
    # 1. step: get all tables
    
    # tbls = [t for t in dom.by_tag('table')]

    # 2. step: get all wikitable sortable tables (the ones with data)
    
    tbls = [t for t in dom.by_tag('table') if t.attributes['class'] == "sortable wikitable jquery-tablesorter"]
    print tbls
    return tbls

url = 'http://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'
website_html = requests.get(url).text
tables = get_population_html_tables(website_html)
print "table length: %d" %len(tables)
for t in tables:
    print t.attributes

#print website_html