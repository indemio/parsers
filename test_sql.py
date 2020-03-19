import sys
import sqlite3

conn = sqlite3.connect('C:/Users/Sedykhgi/Documents/GitHub/parsers/pythonsqlite.db')
#conn.text_factory = lambda x: str(x, 'cp1251')
c = conn.cursor()
c.execute('''SELECT *  FROM tempTab,tempTab2,tempTab3,tempTab4,tempTab5''')
rows = c.fetchall()
for row in rows:
    print(row)
