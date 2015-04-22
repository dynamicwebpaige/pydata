#! /usr/bin/python

import time
import datetime

HPD_police_beats = ["1A10", "1A20", "1A30", "1A40", "1A50", "3B10", "3B20", "3B30", "3B40", "3B50", "7C10", "7C20", "7C30", "7C40", "7C50", "11H10", "11H20", "11H30", "11H40", "11H50", "10H10", "10H20", "10H30", "10H40", "10H50", "10H60", "10H70", "10H80", "12D10", "12D20", "12D30", "12D40", "12D50", "12D60", "12D70", "13D10", "13D20", "13D30", "13D40", "14D10", "14D20", "14D30", "14D40", "14D50", "17E10", "17E20", "17E30", "17E40", "18F10", "18F20", "18F30", "18F40", "18F50", "18F60", "15E10", "15E20", "15E30", "15E40", "16E10", "16E20", "16E30", "16E40", "19G10", "19G20", "19G30", "19G40", "19G50", "20G10", "20G20", "20G30", "20G40", "20G50", "20G60", "20G70", "20G80", "4F10", "4F20", "4F30", "5F10", "5F20", "5F30", "5F40", "21I10", "21I20", "21I30", "21I40", "21I50", "21I60", "21I70", "23J10", "23J40", "23J50"]

full_years = []
months_to_check = []
URLS = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
now = datetime.datetime.now()

for i in range(2010, now.year, 1):
	full_years.append(str(i))

for i in range(12):
	if now.strftime("%b") != months[i]:
		months_to_check.append(months[i])
	else:
		break

months_to_check.pop()

def URL_populator():
	for i in  months[5:]:
		for j in HPD_police_beats:
			URLS.append("http://www.houstontx.gov/police/cs/stats2009/" + i + "09/" + i + j + ".htm")

	for i in months:
		for j in full_years:
			for k in HPD_police_beats:
				URLS.append("http://www.houstontx.gov/police/cs/stats" + j + "/" + i + j[-2:] + "/" + i + k + ".htm")

	for i in months_to_check:
		for j in HPD_police_beats:
			URLS.append("http://www.houstontx.gov/police/cs/stats2015/" + i + "15/" + i + j + ".htm")

	return URLS

