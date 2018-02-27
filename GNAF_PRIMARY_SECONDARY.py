# GNAF PRIMARY_SECONDARY Loader


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
cur.execute("DROP TABLE IF EXISTS PRIMARY_SECONDARY;")

cur.execute("CREATE TABLE PRIMARY_SECONDARY (PRIMARY_SECONDARY_PID varchar(15) PRIMARY KEY,PRIMARY_PID varchar(15), SECONDARY_PID varchar(15), DATE_CREATED Date,\
	DATE_RETIRED Date,PS_JOIN_TYPE_CODE integer, PS_JOIN_COMMENT varchar(500));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_PRIMARY_SECONDARY_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'PRIMARY_SECONDARY', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
