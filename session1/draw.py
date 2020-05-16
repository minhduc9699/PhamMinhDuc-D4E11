from turtle import *

shape("turtle")
speed(-1)
color('green')

n = int(input('enter number of edge'))

for i in range(n):
  forward(100)
  left(360/n)

mainloop()