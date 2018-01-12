# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:47:25 2018

@author: Jimit
"""

# Counting Organizations

import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
            CREATE TABLE Counts(org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if(len(fname) < 1): fname = 'mbox.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    email_parts = email.split('@')
    org = email_parts[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    # (email,) is a one-element tuple
    # (email) won't turn 'email' into a tuple
    # so we need to add a comma after 'email'
    
    
    row = cur.fetchone()
    
    if row is None:
        cur.execute('''INSERT INTO Counts(org, count)
        VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
        
conn.commit()
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()