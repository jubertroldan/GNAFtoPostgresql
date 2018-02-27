# GNAF ADDRESS_DETAIL Loader


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
cur.execute("DROP TABLE IF EXISTS ADDRESS_DETAIL;")

cur.execute("CREATE TABLE ADDRESS_DETAIL (ADDRESS_DETAIL_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_LAST_MODIFIED Date, DATE_RETIRED Date, BUILDING_NAME varchar(45), LOT_NUMBER_PREFIX varchar(2), LOT_NUMBER varchar(5),\
	LOT_NUMBER_SUFFIX varchar(2), FLAT_TYPE_CODE varchar(7), FLAT_NUMBER_PREFIX varchar(2), FLAT_NUMBER integer,\
	FLAT_NUMBER_SUFFIX varchar(2), LEVEL_TYPE_CODE varchar(4), LEVEL_NUMBER_PREFIX varchar(4), LEVEL_NUMBER integer,\
	LEVEL_NUMBER_SUFFIX varchar(2), NUMBER_FIRST_PREFIX varchar(4), NUMBER_FIRST integer, NUMBER_FIRST_SUFFIX varchar(4),\
	NUMBER_LAST_PREFIX varchar(3), NUMBER_LAST integer, NUMBER_LAST_SUFFIX varchar(2), STREET_LOCALITY_PID varchar(15),\
	LOCATION_DESCRIPTION varchar(45), LOCALITY_PID varchar(45), ALIAS_PRINCIPAL char(1), POSTCODE varchar(4), PRIVATE_STREET varchar(75),\
	LEGAL_PARCEL_ID varchar(20), CONFIDENCE integer, ADDRESS_SITE_PID varchar(15), LEVEL_GEOCODED_CODE integer, PROPERTY_PID varchar(15),\
	GNAF_PROPERTY_PID varchar(15), PRIMARY_SECONDARY varchar(1));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_ADDRESS_DETAIL_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_DETAIL', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
