# GNAF STREET_LOCALITY_ALIAS Loader


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
cur.execute("DROP TABLE IF EXISTS STREET_LOCALITY_ALIAS;")

cur.execute("CREATE TABLE STREET_LOCALITY_ALIAS (STREET_LOCALITY_ALIAS_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, STREET_LOCALITY_PID varchar(15), STREET_NAME varchar(100), STREET_TYPE_CODE varchar(15), STREET_SUFFIX_CODE varchar(15),ALIAS_TYPE_CODE varchar(10));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_STREET_LOCALITY_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'STREET_LOCALITY_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
