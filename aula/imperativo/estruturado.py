import random

notas_alunos = [random.randint(1, 11), 
                random.randint(1, 11), 
                random.randint(1, 11), 
                random.randint(1, 11),
                random.randint(1, 11),
                random.randint(1, 11)]

total_de_provas = len(notas_alunos)

def calcular_media(notas):
    soma = 0
    for nota in notas_alunos:
        soma += nota
    media = soma/total_de_provas
    classificar_aluno(media)
    return

def classificar_aluno(nota):
    if(nota >= 7):
        print(f"passou! {nota:.2f}")
    elif(nota >= 5):
        print(f"Recuperacao! {nota:.2f}")
    else:
        print(f"Reprovado! {nota:.2f}")

calcular_media(notas_alunos)
