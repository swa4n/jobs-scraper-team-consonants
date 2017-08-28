#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="rootroot",  # your password
                     db="thinkit")        # name of the data base
db.set_character_set('utf8mb4')
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')
