# for i in range(3):
#   print(i)
from getpass import getpass

username = 'mindx'
password = 'password'
count = 0
while True:
  if count > 7:
    print('hết lần thử r bạn eii')
    break
  username_input = input('username=')
  password_input = getpass('password=')
  if username_input == username and password_input == password:
    print('Welcome')
    break
  else:
    count += 1