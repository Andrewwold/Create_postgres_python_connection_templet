import psycopg2
from config import config


def insert_game(game_name):

	sql = """INSERT INTO games(game_name)
			 VALUES(%s) RETURNING game_id;"""
	conn = None
	game_id = None

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		cur.execute(sql, (game_name,))

		game_id = cur.fetchone()[0]

		conn.commit()

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

	return game_id

def insert_list_of_games(games_list):

	sql = "INSERT INTO games(game_name) VALUES(%s)"
	conn = None
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		cur.executemany(sql, games_list)

		conn.commit()

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


games = [('Skyrim',),('Starcraft',),('RuneScape',), ('Mario',)]


insert_list_of_games(games)
