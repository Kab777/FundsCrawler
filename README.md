<h1>Funds Bot</h1>

![](https://github.com/Kab777/FundsCrawler/blob/master/Logo/fundsC.png)


| Param  | Type | Description |
| --- | --- | --- |
| code | text (255)  | The id of the fund you wish to search for. (ex: TDB970)|
| type | text (255)  | The type of the afund you wish to search for. (ex: Balanced)|


[**Run example**](http://junyuzhou.com/api/public/fundPrice?code=TDB970&type=Balanced)

online version available at here: http://junyuzhou.com/funds.html

As of Sep 23, there are **673** unique users registered for daily investment notification.

A Python 3 based Web-Crawler/Scraper for TD Mutual Funds Website (a JS rendered website). https://www.tdcanadatrust.com/products-services/investing/mutual-funds/fund_prices.jsp

Including Crawling, Parsing, Inserting into database process.

Sample data is avaliable.


Crawling:

Using [**Selenium webdriver**](https://pypi.python.org/pypi/selenium) and [**PhantomJS**](http://phantomjs.org/) to create headless browser, making javascript rendered source code avaliable for crawling.

Parsing:

Combining **Regex** and [**Beautifulsoup4**](https://pypi.python.org/pypi/beautifulsoup4) to parse html file.

Inserting:

**MySQL connector/API**

