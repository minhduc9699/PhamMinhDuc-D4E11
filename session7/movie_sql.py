import pymysql
client = pymysql.connect(
  host='localhost',
  user='root',
  password='@gmail.com',
  cursorclass=pymysql.cursors.DictCursor
)
cursor = client.cursor()
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
client.commit()
