'''
1- Faça um programa em Py que receba o total das vendas de cada vendedor e armazenadas em um vetor. Receba também o percentual de comissão 
de cada vendedor e
armazene-os em outro vetor. Receba os nomes desses vendedores e armazene ­os em um terceiro vetor. Existem apenas dez vendedores. 
Calcule e mostre: 
a) Um relatório com os nomes dos vendedores e os valores a receber; 
b) O total das vendas de todos os vendedores; 
c) O maior valor a receber e quem o receberá; 
d) O menor valor a receber e quem o receberá.

'''

nomeVendedor = []
vendas = []
comissoes = []
valores_receber = []


for i in range(10):

    nome = str(input(f"Digite o nome do {i+1}º vendedor: "))
    venda = float(input("Digite o total de vendas: "))
    comissao = float(input("Digite o percentual de comissão: "))

    nomeVendedor.append(nome)
    vendas.append(venda)
    comissoes.append(comissao)



for i in range(10):

    valor = vendas[i] * (comissoes[i] / 100)
    valores_receber.append(valor)



print("\n===== RELATÓRIO DOS VENDEDORES =====")

for i in range(10):

    print(f"Vendedor: {nomeVendedor[i]}")
    print(f"Valor a receber: R$ {valores_receber[i]:.2f}")
    print("-----------------------------")



total_vendas = 0

for i in range(10):

    total_vendas += vendas[i]

print(f"\nTotal de vendas: R$ {total_vendas:.2f}")



maior = valores_receber[0]
vendedorMaior = nomeVendedor[0]

for i in range(10):

    if valores_receber[i] > maior:
        maior = valores_receber[i]
        vendedorMaior = nomeVendedor[i]

print(f"\nMaior comissão: R$ {maior:.2f}")
print(f"Vendedor: {vendedorMaior}")



menor = valores_receber[0]
vendedorMenor = nomeVendedor[0]

for i in range(10):

    if valores_receber[i] < menor:
        menor = valores_receber[i]
        vendedorMenor = nomeVendedor[i]

print(f"\nMenor comissão: R$ {menor:.2f}")
print(f"Vendedor: {vendedorMenor}")
