#!/bin/python

############################################################
# This application is being made in order for me
#     to learn 'requests' and 'BeautifulSoup'
# It is intended to be functional for limited purposes.
# Objective: quickly find a restaurant in Yelp and
#     display their most popular items.
############################################################

import requests
from bs4 import BeautifulSoup

desc = input('Food/Restaurant: ')
loc = input('Geo: ')

payload = {'find_desc': desc, 'find_loc': loc}

r = requests.get('http://www.yelp.com/search?', params = payload)

data = r.text

print(r.url)
print(r.status_code)
soup = BeautifulSoup(data,'html.parser')

bizlinks = []

for link in soup.findAll('a',{'class': 'biz-name'}):
        bizlinks.append('http://wwww.yelp.com' + link.get('href'))

bizlinks = bizlinks[1:]
bizlinks = bizlinks[:1]

for i in bizlinks:
        print(i)
        r = requests.get(i)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')
        
        # Grab restaurant name
        for title in soup.findAll('h1',{'class': 'biz-page-title'}):
            print('Restaurant: ' + title.get_text())
            
        # Grab top mentioned phrases
        for ngram in soup.findAll('p',{'class': 'quote'}):
            print('Most talked about features: ' + ngram.get_text() + '\n')
