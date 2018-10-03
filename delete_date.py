import psycopg2
from config import config


def delete_games(game_id):

	conn = None
	
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute("DELETE FROM games WHERE game_id = %s", (game_id,))
		

		conn.commit()
		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


delete_games(2)