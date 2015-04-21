#! /usr/bin/python

import urllib2
import pprint
import csv
from bs4 import BeautifulSoup

url = 'http://www.houstontx.gov/police/cs/stats2015/jan15/jan1510h40.htm'
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

# holder2 = pprint.pprint(list(chunks(holder,10)))
holder2 = list(chunks(holder,10))
csvfile = '/home/paige/list_of_crimes.csv'

with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerows(holder2)
