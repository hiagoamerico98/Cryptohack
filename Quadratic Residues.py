p = 29
ints = [14, 6, 11]

lista = [] 

for a in range(p):
  if pow(a,2,p) in ints:
    lista.append(a)

print(min(lista))
