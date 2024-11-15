# SOMAR NUMEROS ATÉ ATINGIR UM LIMITE

limite = 100
soma = 0
numero = 1

# ENQUANTO A SOMA FOR MENOR QUE O LIMITE, CONTINUE SOMANDO
while soma < limite:
    soma += numero
    numero += 1

print(soma)

print("\n####################################################")
# ENCONTRAR O PRIMEIRO NUMERO DIVISIVEL POR 7 EM UM INTERVALO

for numero in range(1, 1000):
    if numero % 7 == 0:
        print(numero, end=", ")
        # break

print("\n\n####################################################")
# VERIFICAR SE TODOS OS ITENS DE UMA LISTA SÃO POSITIVOS

numeros = [1,2,3,4,5,6]
todos_positivos = True

for numero in numeros:
    if numero < 0:
        todos_positivos = False

if todos_positivos:
    print("\nTodos os num positivos")
else:
    print("\nExistem num negativos")
