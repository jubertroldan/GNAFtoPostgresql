# GNAF LOCALITY_POINT Loader


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
cur.execute("DROP TABLE IF EXISTS LOCALITY_POINT;")

cur.execute("CREATE TABLE LOCALITY_POINT (LOCALITY_POINT_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, LOCALITY_PID varchar(15), PLANIMETRIC_ACCURACY integer, LONGITUDE numeric(11,8), LATITUDE numeric(10,8));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_LOCALITY_POINT_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_POINT', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
