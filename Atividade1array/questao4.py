'''
4- Faça um programa em Py que alimente um vetor, com um número de posições definidas pelo usuário. 
Este vetor deverá armazenar um conjunto de nomes em diferentes posições. Crie um mecanismo para alimentar 
elementos no vetor e pesquisar por um valor existente.
 ======== MENU ======== 
1) Cadastrar nome 
2) Pesquisar nome 
3) Listar todos os nome 
0) Sair do programa 
——————– 
Digite sua escolha:
'''

nomes = []

quantidade = int(input("Quantos nomes deseja cadastrar?: "))

opcao = -1

while opcao != 0:
    print("======== MENU ========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")

    opcao = int(input("Digite sua escolha: "))
    if opcao == 1:
        for i in range(quantidade):
            nome = input (f"Digite o {i+1}° nome: ")
            nomes.append(nome)
        
    elif opcao == 2:
        pesquisa = input("Qual nome você deseja pesquisar?: ")
        if pesquisa in nomes:
            print("Nome encontrado!")
        else:
            print("Nome não encontrado!")
    
    elif opcao == 3:
        for i in range(len(nomes)):
            print(nomes[i])
    
    elif opcao == 0:
        print("Você saiu do programa!")
    
    else:
        print("Número inválido!")