import pymysql


client = pymysql.connect(
    host='localhost',
    user='root',
    password='@gmail.com',
    cursorclass=pymysql.cursors.DictCursor
  )

cursor = client.cursor()

# cursor.execute('CREATE DATABASE d4e11')

cursor.execute('''
  CREATE TABLE d4e11.centre(
    id VARCHAR(255) UNIQUE PRIMARY KEY,
    name VARCHAR(255) UNIQUE
  )
''')

cursor.execute('''
  CREATE TABLE d4e11.salesman(
    username VARCHAR(255) PRIMARY KEY,
    centre_id VARCHAR(255) REFERENCES d4e11.centre(id),
    email VARCHAR(255),
    name VARCHAR(255)
  )
''')

# cursor.execute('''
#   CREATE TABLE d4e11.user (
#     id INT(11) AUTO_INCREMENT PRIMARY KEY,
#     usename VARCHAR(255),
#     age INT(11)
#   ) 
# ''')

# cursor.execute(''' 
#   INSERT INTO `d4e11`.centre (`id`, `name`)
#   VALUES ('1', 'Sao Hỏa'), ('2', 'Sao Kim');
# ''')

centre_name = 'Sao Hỏa'

cursor.execute(f''' SELECT * FROM d4e11.centre WHERE name = '{centre_name}' ''')
centre_found = cursor.fetchone()
print(centre_found)
cursor.execute(
  f'''
  INSERT INTO d4e11.salesman(username, centre_id, email, name)
  VALUES ('best salesman', '{centre_found['id']}', 'email@gamil.com', 'người bán hàng');
  '''
)

# cursor.execute('''SELECT MAX(age) AS max FROM d4e11.user''')
# data = cursor.fetchone()
# print(data)
# # print(data['max'])
# # cursor.execute('''
# #   UPDATE d4e11.user SET age = 1 WHERE age = 96
# # ''')

# cursor.execute('''
#   DELETE FROM d4e11.user WHERE age = 1
# ''')
client.commit()