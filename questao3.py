"""
    3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 (121 dias) não ocorreu 
    temperatura inferior a 15° C e nem superior a 40° C.
    Fazer um programa py que determine: 
    a) A menor temperatura ocorrida 
    b) A maior temperatura ocorrida 
    c) A temperatura média do período  
    """

somaTemp = 0 
temperaturas = []
menorTemp = 40
maiorTemp = 15

for i in range(4):
    Nmes = int(input(f"Digite a temp do {i+1}° mês: "))
    temperaturas.append(Nmes)
    somaTemp += Nmes
    
    if Nmes < menorTemp:
        menorTemp = Nmes

    if Nmes > maiorTemp:
        maiorTemp = Nmes
    
    media = somaTemp/4
    
    

print("Maior temperatura:", maiorTemp)
print("Menor temperatura:", menorTemp)
print("A temperatura média é de: ",media)