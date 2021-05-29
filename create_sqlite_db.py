#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('test.db')

conn.execute('''
    CREATE TABLE signatures (
        name    TEXT    NOT NULL,
        link    TEXT,
        date    DATE
    );
''')

conn.close()
