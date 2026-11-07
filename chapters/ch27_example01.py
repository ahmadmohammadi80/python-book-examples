# Python book chapter 27, example 1
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE tx (id INTEGER PRIMARY KEY, kind TEXT CHECK(kind IN ('income','expense')), amount INTEGER CHECK(amount > 0))")
con.execute("INSERT INTO tx(kind,amount) VALUES (?,?)", ("expense", 25000))
con.execute("INSERT INTO tx(kind,amount) VALUES (?,?)", ("income", 90000))
print(con.execute("SELECT kind,SUM(amount) FROM tx GROUP BY kind").fetchall())
con.close()
