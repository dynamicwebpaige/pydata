#! /usr/bin/python

import urllib2
import pprint
import csv
import URL_generator as populator
from bs4 import BeautifulSoup

police_districts = ['populate w/ police districts #s, there should be 90']
years_abbr = ['09','10','11','12','13','14','15']
years_stats = ['stats2009','stats2010','stats2011','stats2012','stats2013','stats2014','stats2015']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

# URL's 
url = 'http://www.houstontx.gov/police/cs/stats2015/jan15/jan1510h40.htm'
# looping through list of URL's 
# urls = populator.URL_populator()

html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

def chunks(l,n):
	for i in xrange(0, len(l), n):
		yield l[i:i+n]

for row in soup('table', {'class':'MsoNormalTable'}):
	holder = []
	values = row.find_all('span')
	for i in values:
		try:
			holder.append(str(i.get_text()))
		except:
			UnicodeDecodeError
			holder.append("Unknown")

# pprint.pprint(list(chunks(holder,10)))
holder2 = list(chunks(holder,10))
csvfile = '/home/paige/list_of_crimes.csv'

with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerows(holder2[1:])
