import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_db = mongo_client.get_database('d4e12')
movie_collection = mongo_db.get_collection('movies')


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

query = {
  'title': {'$ne': None},
  'writer': {'$ne': None},
  'year': {'$ne': None},
  'actors': {'$ne': None}
}
for movie in movie_collection.find(query): # EXTRACT
  # TRANSFORM
  movie_id = str(movie['_id'])
  movie_title = movie['title']
  movie_writer = movie['writer']
  movie_year = movie['year']
  # LOAD
  cursor.execute(f'''
    INSERT INTO movie.movie(id, title, writer, year)
    VALUES ('{movie_id}', '{movie_title}', '{movie_writer}', '{movie_year}')
  ''')



mysql_client.commit()
