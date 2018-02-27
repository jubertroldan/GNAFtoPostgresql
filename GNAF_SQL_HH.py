# GNAF SQL COMBINE

# creates GNAF table with Meshblock mapping 
# include additional columns to be uploaded for Household.

#	address_detail_pid,
#	alias_principal,
#	confidence,
#	postcode,
#	suburb_name,
#	state,
#	latitude,
#	longitude,
#	mb_2011_code,
#	mb_2016_code
	
# libraries installed
# pip 9.0.1
# psycopg2-2.7.3

import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect("dbname=GNAF_DB user=postgres password=postgres")
# Open a cursor to perform database operations
cur = conn.cursor()

# CREATING TEMPORARY TABLE for HH_GNAF_ADDRESS_LATLON

cur.execute("SELECT public.address_detail.address_detail_pid, public.address_detail.alias_principal, public.address_detail.confidence, public.address_detail.postcode, public.address_detail.locality_pid, \
	public.address_default_geocode.longitude, public.address_default_geocode.latitude \
	into temporary table hh_gnaf_latlon \
	FROM public.address_detail left outer join public.address_default_geocode ON public.address_detail.address_detail_pid = public.address_default_geocode.address_detail_pid;")

conn.commit()

cur.execute("SELECT hh_gnaf_latlon.*,public.locality.locality_name, public.locality.state_pid\
	into temporary table hh_gnaf_locality_latlon \
	from hh_gnaf_latlon left outer join public.locality ON hh_gnaf_latlon.locality_pid = public.locality.locality_pid;")

conn.commit()

# CREATE hh_gnaf_abs data for uploading to TERADATA IDW

cur.execute("SELECT hh_gnaf_locality_latlon.address_detail_pid, hh_gnaf_locality_latlon.alias_principal, hh_gnaf_locality_latlon.confidence, \
	hh_gnaf_locality_latlon.postcode, hh_gnaf_locality_latlon.locality_name as suburb_name, public.state.state_abbreviation as state, \
	hh_gnaf_locality_latlon.latitude, hh_gnaf_locality_latlon.longitude \
	into temporary table hh_gnaf_abs \
	from hh_gnaf_locality_latlon left outer join public.state ON hh_gnaf_locality_latlon.state_pid = public.state.state_pid;")

conn.commit()

# ADD MB16 and MB11

cur.execute("SELECT hh_gnaf_abs.*, public.gnaf_address_mb_2011.mb_2011_code \
	into temporary table hh_gnaf_abs_mb11 \
	from hh_gnaf_abs left outer join public.gnaf_address_mb_2011 ON hh_gnaf_abs.address_detail_pid = public.gnaf_address_mb_2011.address_detail_pid;")

conn.commit()

cur.execute("DROP TABLE IF EXISTS public.hh_gnaf_abs_mb;")

cur.execute("SELECT hh_gnaf_abs_mb11.*, public.gnaf_address_mb_2016.mb_2016_code\
	into public.hh_gnaf_abs_mb \
	from hh_gnaf_abs_mb11 left outer join public.gnaf_address_mb_2016 ON hh_gnaf_abs_mb11.address_detail_pid = public.gnaf_address_mb_2016.address_detail_pid;")

conn.commit()

cur.execute("COPY public.hh_gnaf_abs_mb TO 'C:/Workfiles/Tools/gnaf_loader/output/hh_gnaf_abs_mb.csv' DELIMITER ',' CSV;")

conn.commit()

conn.close()