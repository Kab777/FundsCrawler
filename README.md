<h1>Funds Crawler</h1>

A Python 3 based Web-Crawler/Scraper for TD Mutual Funds Website (a JS rendered website). (https://www.tdcanadatrust.com/products-services/investing/mutual-funds/fund_prices.jsp)

Including Crawling, Parsing, Inserting into database process.

Sample data is avaliable.


Crawling:

Using [**Selenium webdriver**](https://pypi.python.org/pypi/selenium) and [**PhantomJS**](http://phantomjs.org/) to create headless browser, making javascript rendered source code avaliable for crawling.

Parsing:

Combining **Regex** and [**Beautifulsoup4**](https://pypi.python.org/pypi/beautifulsoup4) to parse html file.

Inserting:

**MySQL connector/API**

