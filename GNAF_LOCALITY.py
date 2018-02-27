# GNAF LOCALITY Loader


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
cur.execute("DROP TABLE IF EXISTS LOCALITY;")

cur.execute("CREATE TABLE LOCALITY (LOCALITY_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, LOCALITY_NAME varchar(100), PRIMARY_POSTCODE varchar(4), LOCALITY_CLASS_CODE char(1), STATE_PID varchar(15), \
	GNAF_LOCALITY_PID varchar(15), GNAF_RELIABILITY_CODE integer);")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
