# GNAF LOCALITY_ALIAS Loader


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
cur.execute("DROP TABLE IF EXISTS LOCALITY_ALIAS;")

cur.execute("CREATE TABLE LOCALITY_ALIAS (LOCALITY_ALIAS_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, LOCALITY_PID varchar(15), NAME varchar(100), POSTCODE varchar(4), ALIAS_TYPE_CODE varchar(10), \
	STATE_PID varchar(15));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
