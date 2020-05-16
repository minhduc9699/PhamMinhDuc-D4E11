a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

delta = b**2 - 4*a*c
print(delta)
if delta < 0:
  print('no x')
elif delta == 0:
  result = (-b) / (2*a)
  print(result)
else:
  x1 = (-b + delta**(1/2)) / 2*a
  x2 = (-b - delta**(1/2)) / 2*a
  print('x1=', x1, 'x2=', x2)