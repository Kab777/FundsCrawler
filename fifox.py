from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from datetime import datetime
from time import sleep
ff = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
ff.get("https://www.tdassetmanagement.com/fundProfile.form?productGroupName=TD%20Mutual%20Funds&site=TDCT&lang=en")
try:
    element = WebDriverWait(ff, 20).until(EC.presence_of_element_located((By.ID, "td-container")))
    print (ff.page_source)
except Exception as e:
    print (e)
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    ff.get_screenshot_as_file('screenshot-%s.png' % now)
finally:
    ff.quit()
