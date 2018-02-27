# GNAF STREET_LOCALITY Loader


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
cur.execute("DROP TABLE IF EXISTS STREET_LOCALITY;")

cur.execute("CREATE TABLE STREET_LOCALITY (STREET_LOCALITY_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, STREET_CLASS_CODE char(1), STREET_NAME varchar(100), STREET_TYPE_CODE varchar(15), STREET_SUFFIX_CODE varchar(15),LOCALITY_PID varchar(15),\
	GNAF_STREET_PID varchar(15), GNAF_STREET_CONFIDENCE integer, GNAF_RELIABILITY_CODE integer);")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_STREET_LOCALITY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
