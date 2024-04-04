import random
import os

posHamster1 = 0
posHamster2 = 0

# 0 - ninguem venceu ainda
# 1 - hamster1 venceu
# 2 - hamster2 venceu
# 3 - empate
vencedor = 0 

while vencedor == 0: #continua a corrida
    #limpando a tela do console
    # Limpa a tela - Win/Linux/MacOS ​
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    # Fazendo a movimentação do Hamster 1
    nroSorteado = random.randint(1,5) #sorteia um nro entre 1 e 5
    #Aplicar as regras da tabela na posição do hamster 1
    if nroSorteado == 1:
        posHamster1 = posHamster1 + 1
    elif nroSorteado == 2:
        posHamster1 = posHamster1 + 2
    elif nroSorteado == 3:
        # não se mexe
        pass
    elif nroSorteado == 4:
        posHamster1 = posHamster1 - 1
    else:
        posHamster1 = posHamster1 - 2
    #Garantir que não existe pos negativa nem maior que 12
    if posHamster1 < 0:
        posHamster1 = 0
    if posHamster1 > 12:
        posHamster1 = 12

    # Fazendo a movimentação do Hamster 2
    nroSorteado = random.randint(1,5) #sorteia um nro entre 1 e 5
    #Aplicar as regras da tabela na posição do hamster 1
    if nroSorteado == 1:
        posHamster2 = posHamster2 + 1
    elif nroSorteado == 2:
        posHamster2 = posHamster2 + 2
    elif nroSorteado == 3:
        # não se mexe
        pass
    elif nroSorteado == 4:
        posHamster2 = posHamster2 - 1
    else:
        posHamster2 = posHamster2 - 2
    #Garantir que não existe pos negativa nem maior que 12
    if posHamster2 < 0:
        posHamster2 = 0
    if posHamster2 > 12:
        posHamster2 = 12

    #Testa quem venceu
    if posHamster1 == 12: 
        vencedor = 1 # hamster 1 venceu
    if posHamster2 == 12: 
        if vencedor == 0:
            vencedor = 2 # hamster 2 venceu
        else:
            vencedor = 3 #houve um empate
    
    # Imprime na tela o status da corrida
    print('Hamster1: ', end = ' ')
    for n in range(posHamster1):
        print('* ', end = ' ')
    print() #quebra de linha

    print('Hamster2: ', end = ' ')
    for n in range(posHamster2):
        print('* ', end = ' ')
    print() #quebra de linha
    print ('-----------------------------------')

#imprime quem ganhou
if vencedor == 1:
    print('Hamster 1 venceu!')
elif vencedor == 2:
    print('Hamster 2 venceu!')
else:
    print('Houve um empate!')


