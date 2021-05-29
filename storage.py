import sqlite3
import time

def insert(name, link):
    t = time.strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect('test.db') as conn:
        conn.execute(
            'INSERT INTO signatures (name, link, date) VALUES (?, ?, ?)',
            (name, link, t)
        )
        conn.commit()

def get_all_after(after):
    try:
        after = int(after)
        after = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(after))
    except ValueError:
        pass
    with sqlite3.connect('test.db') as conn:
        return list(conn.execute(
            'SELECT name, link FROM signatures WHERE date >= ?',
            (after,)
        ))
