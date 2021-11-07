def calcula(a,y,m):
  i = 1 
  b = 0
  while b != y:
    c = a * i
    b = mod(c,m)
    i = i + 1
  return i - 1

calcula(3,1,13)
