import sys
import sqlite3

conn = sqlite3.connect('xlsdb.db')
#conn.text_factory = lambda x: str(x, 'cp1251')
c = conn.cursor()
c.execute('''SELECT * test''')
rows = c.fetchall()
for row in rows:
    print(row)
