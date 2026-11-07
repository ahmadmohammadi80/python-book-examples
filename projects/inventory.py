"""پروژه فروشگاهی با ثبت تراکنشی سفارش و موجودی."""
import sqlite3
from pathlib import Path

DB_PATH = Path('shop.sqlite3')


def connect(path=DB_PATH):
    con = sqlite3.connect(path)
    con.execute('PRAGMA foreign_keys=ON')
    con.executescript('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL CHECK(price >= 0),
            stock INTEGER NOT NULL CHECK(stock >= 0)
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL REFERENCES products(id),
            qty INTEGER NOT NULL CHECK(qty > 0),
            total INTEGER NOT NULL CHECK(total >= 0)
        );
    ''')
    con.commit()
    return con


def add_product(con, name, price, stock):
    if not name.strip() or price < 0 or stock < 0:
        raise ValueError('محصول نامعتبر')
    with con:
        cur = con.execute('INSERT INTO products(name, price, stock) VALUES (?, ?, ?)',
                          (name.strip(), price, stock))
    return cur.lastrowid


def sell(con, product_id, qty):
    if qty <= 0:
        raise ValueError('تعداد باید مثبت باشد')
    with con:
        row = con.execute('SELECT price,stock FROM products WHERE id=?', (product_id,)).fetchone()
        if row is None:
            raise ValueError('محصول پیدا نشد')
        price, stock = row
        if qty > stock:
            raise ValueError('موجودی کافی نیست')
        cur = con.execute('UPDATE products SET stock=stock-? WHERE id=? AND stock>=?',
                          (qty, product_id, qty))
        if cur.rowcount != 1:
            raise ValueError('تغییر موجودی ناموفق')
        total = price * qty
        con.execute('INSERT INTO orders(product_id, qty, total) VALUES (?, ?, ?)',
                    (product_id, qty, total))
    return total


def report(con):
    for row in con.execute('SELECT id,name,price,stock FROM products ORDER BY id'):
        print(row)
    total = con.execute('SELECT COALESCE(SUM(total), 0) FROM orders').fetchone()[0]
    print('کل فروش:', total)


def main():
    con = connect()
    try:
        pid = add_product(con, 'دفتر', 120000, 10)
        print('مبلغ سفارش:', sell(con, pid, 2))
        report(con)
    finally:
        con.close()


if __name__ == '__main__':
    main()
