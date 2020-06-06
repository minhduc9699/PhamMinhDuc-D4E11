import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_db = mongo_client.get_database('d4e12')
movie_collection = mongo_db.get_collection('movies')

for movie in movie_collection.find({}):
  print(movie)

mysql_client = pymysql.connect(
  host='localhost',
  user='root',
  password='@gmail.com',
  cursorclass=pymysql.cursors.DictCursor
)
cursor = mysql_client.cursor()
cursor.execute('''
  CREATE TABLE IF NOT EXISTS movie.movie(
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255),
    writer VARCHAR(255),
    year VARCHAR(255)
  )
''')
cursor.execute('''
  CREATE TABLE IF NOT EXISTS movie.actor(
    name VARCHAR(255) PRIMARY KEY
  )
''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS movie.movie_actor(
    movie_id VARCHAR(255),
    actor_name VARCHAR(255),
    PRIMARY KEY(movie_id, actor_name)
  )
''')
mysql_client.commit()
