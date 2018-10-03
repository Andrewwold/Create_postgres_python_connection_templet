import psycopg2
from config import config


def create_tables():

	commands = (
		"""
		CREATE TABLE games (
			game_id SERIAL PRIMARY KEY,
			game_name VARCHAR(50) NOT NULL,
			game_price INTEGER
		)
		""",
		"""
		CREATE TABLE stuff (
			game_id SERIAL PRIMARY KEY,
			game_name VARCHAR(50) NOT NULL,
			game_price INTEGER
		)
		""")

	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		print("connected to Database")
		cur = conn.cursor()

		for command in commands:
			cur.execute(command)

		cur.close()
		
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

create_tables()		