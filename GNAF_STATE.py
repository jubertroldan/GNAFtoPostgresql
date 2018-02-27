# GNAF STATE Loader


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
cur.execute("DROP TABLE IF EXISTS STATE;")

cur.execute("CREATE TABLE STATE (STATE_PID varchar(15) PRIMARY KEY,DATE_CREATED Date, DATE_RETIRED Date,\
	STATE_NAME varchar(50),STATE_ABBREVIATION varchar(3));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_STATE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STATE', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
