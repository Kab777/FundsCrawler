from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from datetime import datetime
import os


class Engine:
	"Crawling Engine to fetch source code"
	__filename = None

	def __init__(self):
		self.__filename = "MF_Source.html"

	def fetch(self):
		ff = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
		ff.get("https://www.tdassetmanagement.com/fundProfile.form?productGroupName=TD%20Mutual%20Funds&site=TDCT&lang=en")
		#ff.get("https://www.tdcanadatrust.com/products-services/investing/mutual-funds/fund_prices.jsp")
		try:
			element = WebDriverWait(ff, 20).until(EC.presence_of_element_located((By.ID, "td-container")))
			file = open(self.__filename,"w")
			file.write(ff.page_source)
			file.close()
		except Exception as e:
			print (e)
			now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
			ff.get_screenshot_as_file('screenshot-%s.png' % now)
		finally:
			ff.quit()

	def close(self):
		os.remove(self.__filename)
		self.__filename= None
