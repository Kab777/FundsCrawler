import urllib
import re

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



class Analyser:
	__filename= None

	def __init__(self):
		self.__filename="MF_Source.html"

	def modify(self, new_str):
		return new_str.replace(" ", "_")

	def process(self):
		url = "fox.html"

		data = open(url, "r").read()


		soup = BeautifulSoup(data)

		Types = soup.find_all("h3",class_="td-margin-top-medium")


		#print (Type.string)
		links = soup.find_all("table", class_="td-table td-table-border-row td-table-border-column td-table-stripe-row td-table-hover-row")
		j=0
		i = 0

		for link in links:
			print (self.modify(Types[i].string.strip()))
			i+=1;
			Funds = link.find_all("tr")
			for Fund in Funds:
				name_tag = Fund.find("a",class_="td-link-standalone td-link-standalone-secondary")
		#		price_tag = Fund.find("td",class_="td-copy-sub")
				change = Fund.find_all("td",class_="td-copy-sub")#Alternative way here is to use css seletor (separate price, red/green growth rate)
				if not name_tag:
					continue
				else:
					pattern = re.compile(r"(.+?)\s\((.+?)\)")
					m = pattern.match(change[1].string)
					print (self.modify(name_tag.string.strip())+": " +change[0].string + " " + m.group(1) + " " + m.group(2))# + m.group(2))#Trim leading spaces
					#print (change)
					j+=1

		print (j)



a = Analyser()
a.process()
