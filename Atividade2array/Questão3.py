'''
3- Faça um programa que leia e monte dois vetores de números inteiros com 20 números
cada. Depois de montados, gere um terceiro vetor 
formado pela diferença dos dois vetores lidos,
um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto 
vetor formado pela multiplicação dos dois vetores lidos.
'''

vetor1 = []
vetor2 = []
diferenca = []
multiplicacao = []
soma = []


for i in range(20):
    n1 = int(input(f"Digite o {i+1}° número para o vetor 1: "))
    vetor1.append(n1)

    n2 = int(input(f"Digite o {i+1}° número para o vetor 2: "))
    vetor2.append(n2)


for i in range(20):
    diferenca.append(vetor1[i] - vetor2[i])
    soma.append(vetor1[i] + vetor2[i])
    multiplicacao.append(vetor1[i] * vetor2[i])


print("\n===== RESULTADOS =====")
print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Diferença:", diferenca)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)