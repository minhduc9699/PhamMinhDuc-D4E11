from random import shuffle
from getpass import getpass

quiz = getpass('enter your quiz').lower()

list_quiz = list(quiz)
shuffle(list_quiz)
for i in range(len(list_quiz)):
  print(list_quiz[i].upper(), end=' ')

ans = input('your guess? ').lower()
if ans == quiz:
  print('bingo')
else:
  print('T.T')