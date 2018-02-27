# GNAF ADDRESS_SITE_GEOCODE Loader


# libraries installed
# pip 9.0.1
# psycopg2-2.7.3

import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# drop table
cur.execute("DROP TABLE IF EXISTS ADDRESS_SITE_GEOCODE;")

cur.execute("CREATE TABLE ADDRESS_SITE_GEOCODE (ADDRESS_SITE_GEOCODE_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, ADDRESS_SITE_PID varchar(15), GEOCODE_SITE_NAME varchar(46), GEOCODE_SITE_DESCRIPTION varchar(45), GEOCODE_TYPE_CODE varchar(4), \
	RELIABILITY_CODE integer, BOUNDARY_EXTENT integer, PLANIMETRIC_ACCURACY integer, ELEVATION integer, LONGITUDE numeric(11,8), LATITUDE numeric(10,8));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_ADDRESS_SITE_GEOCODE_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_SITE_GEOCODE', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
