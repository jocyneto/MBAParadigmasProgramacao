dobro = lambda x: x * 2

print(dobro(4))

valores = [1,2,3,4]

valores_dobrados = list(map(lambda x: x*2, valores))

print(valores_dobrados)

numeros_impares = list(filter(lambda x: x % 2 != 0, valores))

print(numeros_impares)
