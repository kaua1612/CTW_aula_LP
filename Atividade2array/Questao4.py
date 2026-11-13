'''
4-Em uma classe há n alunos, cada um dos quais realizou k provas com pesos distintos. 
Dados n , k, os pesos das k provas e 
as notas de cada aluno, 
calcular a média ponderada das provas para cada aluno e 
a média aritmética da classe em cada uma das provas
'''


n = int(input("Quantos alunos existem na turma? "))
k = int(input("Quantas provas foram realizadas? "))

pesos = []
notas = []

for i in range(k):
    peso = float(input(f"Digite o peso da prova {i+1}: "))
    pesos.append(peso)


for i in range(n):
    notasAluno = []

    print(f"\n===== ALUNO {i+1} =====")

    for j in range(k):
        nota = float(input(f"Digite a nota da prova {j+1}: "))
        notasAluno.append(nota)

    notas.append(notasAluno)



print("\n===== MÉDIA DOS ALUNOS =====")

for i in range(n):
    somaNotas = 0
    somaPesos = 0

    for j in range(k):
        somaNotas += notas[i][j] * pesos[j]
        somaPesos += pesos[j]

    mediaPonderada = somaNotas / somaPesos

    print(f"Aluno {i+1}: {mediaPonderada:.2f}")



print("\n===== MÉDIA DE CADA PROVA =====")

for j in range(k):
    soma = 0

    for i in range(n):
        soma += notas[i][j]

    media = soma / n

    print(f"Prova {j+1}: {media:.2f}")
