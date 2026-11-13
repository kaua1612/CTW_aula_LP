'''
2- Faça um programa em Py que leia um vetor de seis elementos numéricos inteiros, calcule e mostre: 
a) A quantidade de números pares 
b) Quais os números pares 
c) A quantidade de números ímpares 
d) Quais os números ímpares
'''

numP = []
numI = []
num = []

qtdP = 0
qtdI = 0

for i in range(6):
    numero = int(input(f"Digite o seu {i+1}° número: "))
    num.append(numero)

for i in range(6):
    if num[i] % 2 == 0:
        print(num[i], "é par")
        numP.append(num[i])
        qtdP += 1 
    else:
        print(num[i], "é ímpar")
        numI.append(num[i])
        qtdI += 1 
        
print("Quantidade de números pares: ",qtdP)
print("Números pares: ",numP)
print("Quantidade de números ímpares: ",qtdI)
print("Números ímpares: ",numI)
        
        