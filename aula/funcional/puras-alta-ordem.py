def soma(a,b):
    return a+b

# print(soma(2,3))
# print(soma(2,3))

def aplicar_duas_vezes(func, valor):
    return func(func(valor))

def incrementar(x):
    return x + 1

def elevar_ao_quadrado(x):
    return x ** 2

# print(incrementar(7))

print(aplicar_duas_vezes(incrementar, 1))

numeros = list(range(1,7))

def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista] #list compreension
    # lista_transformada = []
    # for item in lista:
    #     item_transformado.append(funcao(x))
    # return lista_transformadas

numeros_quadradao = aplicar_transformacao(elevar_ao_quadrado, numeros)

print(numeros_quadradao)
