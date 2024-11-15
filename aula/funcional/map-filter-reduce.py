from functools import reduce


numeros = list(range(1,11))

# Filtrar numeros pares
numeros_pares = list(filter(lambda x:x % 2 == 0, numeros))

# Dobra
numeros_pares_dobrados = list(map(lambda x:x*2, numeros_pares))

# Soma todos
soma_numeros_pares_dobrados = reduce(lambda x,y: x+y, numeros_pares_dobrados)

print(soma_numeros_pares_dobrados)
