from turtle import *

n = int(input('enter number of edge'))

for edge in range(3, n+1):
  for i in range(edge):
    forward(100)
    left(360 / edge)


mainloop()