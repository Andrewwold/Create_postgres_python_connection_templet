import psycopg2
from config import config


def update_game(game_id, game_name):

	sql = """UPDATE games
				SET game_name = %s
				WHERE game_id = %s"""
	conn = None
	update_rows = 0

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		cur.execute(sql, (game_name, game_id))

		update_rows = cur.rowcount

		conn.commit()

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

	return update_rows

update_game(2, "Minecraft2")