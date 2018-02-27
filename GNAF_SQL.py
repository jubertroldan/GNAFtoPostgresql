# GNAF SQL COMBINE

# creates GNAF table with Meshblock mapping


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
cur.execute("DROP TABLE IF EXISTS public.GNAF_address;")

cur.execute("SELECT address_detail.address_detail_pid, longitude, latitude \
	into public.GNAF_address \
	FROM public.address_detail left outer join public.address_default_geocode ON public.address_detail.address_detail_pid = public.address_default_geocode.address_detail_pid\
	where (public.address_detail.confidence >= 0) AND (public.address_detail.alias_principal = 'P');")

conn.commit()

cur.execute("DROP TABLE IF EXISTS public.GNAF_address_mb_2016_pid;")

cur.execute("SELECT GNAF_address.address_detail_pid, longitude, latitude, mb_2016_pid \
	into public.GNAF_address_mb_2016_pid \
	FROM public.GNAF_address left outer join public.address_mesh_block_2016 ON public.GNAF_address.address_detail_pid = public.address_mesh_block_2016.address_detail_pid\
	;")

conn.commit()


cur.execute("DROP TABLE IF EXISTS public.GNAF_address_mb_2016;")

cur.execute("SELECT address_detail_pid, longitude, latitude, mb_2016_code  \
	into public.GNAF_address_mb_2016 \
	FROM public.GNAF_address_mb_2016_pid left outer join public.mb_2016 ON public.GNAF_address_mb_2016_pid.mb_2016_pid = public.mb_2016.mb_2016_pid\
	;")

conn.commit()


cur.execute("DROP TABLE IF EXISTS public.GNAF_address_mb_2011_pid;")

cur.execute("SELECT GNAF_address.address_detail_pid, longitude, latitude, mb_2011_pid \
	into public.GNAF_address_mb_2011_pid \
	FROM public.GNAF_address left outer join public.address_mesh_block_2011 ON public.GNAF_address.address_detail_pid = public.address_mesh_block_2011.address_detail_pid\
	;")

conn.commit()


cur.execute("DROP TABLE IF EXISTS public.GNAF_address_mb_2011;")

cur.execute("SELECT address_detail_pid, longitude, latitude, mb_2011_code  \
	into public.GNAF_address_mb_2011 \
	FROM public.GNAF_address_mb_2011_pid left outer join public.mb_2011 ON public.GNAF_address_mb_2011_pid.mb_2011_pid = public.mb_2011.mb_2011_pid\
	;")

conn.commit()



# delete uneeded table
cur.execute("DROP TABLE IF EXISTS public.gnaf_address;")
cur.execute("DROP TABLE IF EXISTS public.gnaf_address_mb_2011_pid;")
cur.execute("DROP TABLE IF EXISTS public.gnaf_address_mb_2016_pid;")

conn.commit()


conn.close()
