"""حسابداری شخصی ساده با SQLite و مبالغ صحیح."""
import argparse
import sqlite3
from pathlib import Path

DB_PATH = Path('expenses.sqlite3')


def connect(path=DB_PATH):
    con = sqlite3.connect(path)
    con.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        day TEXT NOT NULL,
        kind TEXT NOT NULL CHECK(kind IN ('income', 'expense')),
        category TEXT NOT NULL,
        amount INTEGER NOT NULL CHECK(amount > 0)
    )''')
    con.commit()
    return con


def add(con, day, kind, category, amount):
    if len(day) != 10 or day[4] != '-' or day[7] != '-':
        raise ValueError('تاریخ باید YYYY-MM-DD باشد')
    if kind not in {'income', 'expense'} or not category.strip() or amount <= 0:
        raise ValueError('مقدار نامعتبر است')
    from datetime import date
    date.fromisoformat(day)
    with con:
        con.execute('INSERT INTO transactions (day, kind, category, amount) VALUES (?, ?, ?, ?)',
                    (day, kind, category.strip(), amount))


def summary(con):
    rows = con.execute('SELECT kind, SUM(amount) FROM transactions GROUP BY kind').fetchall()
    totals = dict(rows)
    income = totals.get('income', 0)
    expense = totals.get('expense', 0)
    return income, expense, income - expense


def main(argv=None):
    parser = argparse.ArgumentParser(description='ثبت تراکنش‌های مالی آموزشی')
    sub = parser.add_subparsers(dest='action', required=True)
    p = sub.add_parser('add')
    p.add_argument('day')
    p.add_argument('kind', choices=['income', 'expense'])
    p.add_argument('category')
    p.add_argument('amount', type=int)
    sub.add_parser('report')
    args = parser.parse_args(argv)
    con = connect()
    try:
        if args.action == 'add':
            add(con, args.day, args.kind, args.category, args.amount)
            print('تراکنش ثبت شد')
        else:
            print('درآمد، هزینه، مانده:', *summary(con))
    finally:
        con.close()


if __name__ == '__main__':
    try:
        main()
    except (ValueError, sqlite3.DatabaseError) as exc:
        raise SystemExit(f'خطا: {exc}')
