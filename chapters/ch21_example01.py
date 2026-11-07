# Python book chapter 21, example 1
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL)")
con.execute("INSERT INTO products(name, price) VALUES (?, ?)", ("کتاب", 180000))
con.commit()
rows = con.execute("SELECT name, price FROM products").fetchall()
print(rows)
con.close()
