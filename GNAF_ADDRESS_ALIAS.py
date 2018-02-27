# GNAF ADDRESS_ALIAS Loader


# libraries installed
# pip 9.0.1
# psycopg2-2.7.3

import psycopg2
import csv
import string

# Connect to an existing database
conn = psycopg2.connect("dbname=GNAF_DB user=postgres password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

#drop table
cur.execute("DROP TABLE IF EXISTS ADDRESS_ALIAS;")

cur.execute("CREATE TABLE ADDRESS_ALIAS (ADDRESS_ALIAS_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, PRINCIPAL_PID varchar(15), ALIAS_PID varchar(15), ALIAS_TYPE_CODE varchar(10), ALIAS_COMMENT varchar(200));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_ADDRESS_ALIAS_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_ALIAS', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
