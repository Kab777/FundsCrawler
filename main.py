from Crawling_Engine import Engine
from insert import Database
from analyser import Analyser


if __name__ == "__main__":
	crawler = Engine()
	crawler.fetch()

	conn = Database(host="localhost", user="root", password="1234", database="Traning")

	anal=Analyser(conn)
	anal.process()

	crawler.close()


