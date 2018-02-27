# GNAF MB_2016 Loader


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
cur.execute("DROP TABLE IF EXISTS MB_2016;")

cur.execute("CREATE TABLE MB_2016 (MB_2016_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, MB_2016_CODE varchar(15));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_MB_2016_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'MB_2016', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
