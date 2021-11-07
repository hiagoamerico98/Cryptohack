def divisores(a):
  lista = []
  for i in range(1,a+1):
    if a % i == 0:
      lista.append(i) 
  return lista

def gcd(a,b):
  a1 = a
  b1 = b
  a_divisores = divisores(a)
  b_divisores = divisores(b)
  max = []

  if len(a_divisores) >= len(b_divisores):
    for i in range(len(a_divisores)):
      if a_divisores[i] in b_divisores:
        max.append(a_divisores[i])

  else:
    for j in range(len(b_divisores)):
      if b_divisores[j] in a_divisores:
        max.append(b_divisores[j])
  
  #print(max)
  return max[-1]

gcd(66528,52920)
