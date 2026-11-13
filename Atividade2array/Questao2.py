'''
2- Utilizando vetores, crie um programa que organize uma quantidade qualquer de números inteiros fornecidos pelo usuário da seguinte forma: 
primeiro os números pares em ordem crescente e depois os números ímpares em ordem decrescente. 
'''


nI = []
nP = []

while True:
    n = int(input("Digite um número: "))

    if n % 2 ==0:
        nP.append(n)
    else:
        nI.append(n)
        
    
    print(f"Os números pares são: {nP}")
    print(f"Os números ímpares são: {nI}")
    nP.sort()
    nI.sort(reverse=True)
    print(f"A ordem dos númeors pares fica: {nP.sort()}")
    print(f"A ordem dos númeors ímpares fica: {nI.sort(reverse=True)}") 
    print(nP)
    print(nI)