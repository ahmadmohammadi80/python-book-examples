# Python book chapter 21, worked practice
import sqlite3
con = sqlite3.connect(":memory:")
try:
    con.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    with con:
        con.execute("INSERT INTO items(name) VALUES (?)", ("دفتر",))
    print(con.execute("SELECT name FROM items WHERE id=?", (1,)).fetchone()[0])
finally:
    con.close()
