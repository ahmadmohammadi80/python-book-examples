# Python book chapter 21, example 2
import sqlite3

with sqlite3.connect(":memory:") as con:
    con.execute("CREATE TABLE stock (id INTEGER PRIMARY KEY, qty INTEGER NOT NULL)")
    con.execute("INSERT INTO stock VALUES (?, ?)", (1, 7))
    con.execute("UPDATE stock SET qty = qty - ? WHERE id = ? AND qty >= ?", (2, 1, 2))
    print(con.execute("SELECT qty FROM stock WHERE id = ?", (1,)).fetchone())
