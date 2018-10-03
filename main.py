import psycopg2
from config import config

def connect():

	conn = None
	try:
		params = config()
		print('Connecting to the database...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		print('This is the database version')

		cur.execute('SELECT vesion()')

		db_version = cur.fetchone()
		print(db_version)

		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		
	finally:
		if conn is not None:
			conn.close()

connect()			