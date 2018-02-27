# GNAF ADDRESS_MESH_BLOCK_2011 Loader


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
cur.execute("DROP TABLE IF EXISTS ADDRESS_MESH_BLOCK_2011;")

cur.execute("CREATE TABLE ADDRESS_MESH_BLOCK_2011 (ADDRESS_MESH_BLOCK_2011_PID varchar(15) PRIMARY KEY, DATE_CREATED Date,\
	DATE_RETIRED Date, ADDRESS_DETAIL_PID varchar(15), MB_MATCH_CODE varchar(15), MB_2011_PID varchar(15));")

conn.commit()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/ACT_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NSW_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/NT_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/OT_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/QLD_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/SA_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/TAS_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/VIC_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

file = open("C:/Workfiles/Tools/gnaf_loader/data/Standard/WA_ADDRESS_MESH_BLOCK_2011_psv.psv","r")

with file as f:
	for line in f:
		cur.copy_from(f, 'ADDRESS_MESH_BLOCK_2011', sep="|",null = '')
		conn.commit()
file.close()

conn.close()
