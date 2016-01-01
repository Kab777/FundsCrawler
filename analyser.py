import urllib
import re
from insert import Database
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



class Analyser:
	__filename= None
	__dbObject = None

	def __init__(self, database):
		self.__filename="MF_Source.html"
		self.__dbObject =database

	def modify(self, new_str):
		if new_str == "Money Market¹":
			return "Money_Market"
		else:
			return new_str.replace(" ", "_")

	def process(self):

		data = open(self.__filename, "r").read()

		soup = BeautifulSoup(data)

		Types = soup.find_all("h3",class_="td-margin-top-medium")


		links = soup.find_all("table", class_="td-table td-table-border-row td-table-border-column td-table-stripe-row td-table-hover-row")
		j=0
		i = 0

		for link in links:
			
			table_n= self.modify(Types[i].string.strip())
			i+=1;
			Funds = link.find_all("tr")
			change = None
			name_tag = None
			for Fund in Funds:
				name = Fund.find("a",class_="td-link-standalone td-link-standalone-secondary")
				if not name:
					code_name=Fund.find("td",class_="td-copy-sub td-profile-fund-code")
					if code_name:
						fund_code = code_name.string.strip()[10:]
						pattern = re.compile(r"(.+?)\s\((.+?)\)")
						m = pattern.match(change[1].string)
						fund_n = self.modify(name_tag.string.strip())
						temp_price = str(change[0].string)
						self.__dbObject.insert(table_n,fund_name=fund_n,code=fund_code,price=temp_price,price_change=m.group(1),percent_change=m.group(2))
						j+=1
				else:
					change = Fund.find_all("td",class_="td-copy-sub")#Alternative way here is to use css seletor (separate price, red/green growth rate)
					name_tag = name
		
		print (str(j) + " rows are affected.")
				

