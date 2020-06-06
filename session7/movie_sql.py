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
client.commit()
