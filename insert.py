from mysql import connector
#from mysql.connector import errorcode




class Database:
	"Database base class for Mutual Funds"
	__host = None
	__user = None
	__password = None
	__database = None

	__connection = None
	__session = None

	def __init__(self, host="localhost", user="root", password="", database=""):
		self.__host = host
		self.__user = user
		self.__password = password
		self.__database = database


	def connect(self):
		conn = connector.connect(host=self.__host, user=self.__user, password=self.__password,database=self.__database)
		self.__connection = conn
		self.__session = conn.cursor()


	def close(self):
		self.__session.close()
		self.__connection.close()

	def insert(self, table_name, **kwargs):
		placeholders = ', '.join(['%s'] * len(kwargs))
		columns = ', '.join(kwargs.keys())
		sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, placeholders)
		self.connect()
		try:
			self.__session.execute(sql,tuple(kwargs.values()))
		except:
			print("fail")
			self.__connection.rollback()
			self.close()
		self.__connection.commit()
		self.close()
		return self.__session.lastrowid




#conn = Database(host="localhost", user="root", password="1234", database="Traning")
#conn.connect()
#conn.insert("Balanced",fund_name="INcome",code="TDB777",price=24.00,price_change=0.02,percent_change=0.08)
#conn.close()
#   .execute("SELECT * FROM Balanced")
#   x.execute("INSERT INTO Balanced( code,price) VALUES( %s, %s)",('TDB888', 9999))
 #  x.execute("INSERT INTO Balanced(id, code,price) VALUES(2, 'TDB777', 17.98)")
# INSERT INTO Balanced (`price_change`,`price`,`fund_name`,`percent_change`,`code`) VALUES(%s,%s,%s,%s,%s) dict_values([0.08, 0.02, 'INcome', 'TDB777', 24.0])
#INSERT INTO Balanced (fund_name,percent_change,price,price_change,code) VALUES(%s,%s,%s,%s,%s)
 #  result = x.fetchall()
  # for row in result:
 #    print (row[0])
#   x.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
