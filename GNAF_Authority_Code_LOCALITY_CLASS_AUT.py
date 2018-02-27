# GNAF LOCALITY_CLASS_AUT Loader


# libraries installed
# pip 9.0.1
# psycopg2-2.7.3

import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect("dbname=GNAF_DB user=postgres password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# drop table
cur.execute("DROP TABLE IF EXISTS LOCALITY_CLASS_AUT;")

cur.execute("CREATE TABLE LOCALITY_CLASS_AUT (CODE varchar(1) PRIMARY KEY, NAME varchar(50), DESCRIPTION varchar(200));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Authority Code/Authority_Code_LOCALITY_CLASS_AUT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_CLASS_AUT', sep="|",null = '')
		conn.commit()
file.close()


conn.close()
