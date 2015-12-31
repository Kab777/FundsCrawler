from insert import Database

conn = Database(host="localhost", user="root", password="1234", database="Traning")
conn.insert("Balanced",fund_name="INcome",code="TDB777",price=24.00,price_change=0.02,percent_change=0.08)



