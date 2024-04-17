import random
import os

######################FUNÇÕES##############################
def movimentarHamster(posHamster):
    nroSorteado = random.randint(1,5) #sorteia um nro entre 1 e 5
    #Aplicar as regras da tabela na posição do hamster 1
    if nroSorteado == 1:
        posHamster = posHamster + 1
    elif nroSorteado == 2:
        posHamster = posHamster + 2
    elif nroSorteado == 3:
        # não se mexe
        pass
    elif nroSorteado == 4:
        posHamster = posHamster - 1
    else:
        posHamster = posHamster - 2
    #Garantir que não existe pos negativa nem maior que 12
    if posHamster < 0:
        posHamster = 0
    if posHamster > 12:
        posHamster = 12
    # Retorna o valor da posição modificada
    return posHamster

def imprimirStatusCorrida(posHamster1, posHamster2):
    print('Hamster1: ', end = ' ')
    for n in range(posHamster1):
        print('* ', end = ' ')
    print() #quebra de linha

    print('Hamster2: ', end = ' ')
    for n in range(posHamster2):
        print('* ', end = ' ')
    print() #quebra de linha
    print ('-----------------------------------')

def verificarVencedor(posHamster1, posHamster2, vencedor):
    if posHamster1 == 12: 
        vencedor = 1 # hamster 1 venceu
    if posHamster2 == 12: 
        if vencedor == 0:
            vencedor = 2 # hamster 2 venceu
        else:
            vencedor = 3 #houve um empate
    return vencedor

def imprimirResultadoCorrida(vencedor):
    if vencedor == 1:
        print('Hamster 1 venceu!')
    elif vencedor == 2:
        print('Hamster 2 venceu!')
    else:
        print('Houve um empate!')

################### PROGRAMA PRINCIPAL ########################

posHamster1 = 0
posHamster2 = 0

# 0 - ninguem venceu ainda
# 1 - hamster1 venceu
# 2 - hamster2 venceu
# 3 - empate
vencedor = 0 

while vencedor == 0: #continua a corrida
    # Limpa a tela - Win/Linux/MacOS ​
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    # Fazendo a movimentação do Hamster 1
    posHamster1 = movimentarHamster(posHamster1)

    # Fazendo a movimentação do Hamster 2
    posHamster2 = movimentarHamster(posHamster2)

    #Verifica se alguém venceu
    vencedor = verificarVencedor(posHamster1, posHamster2,vencedor)
    
    # Imprime na tela o status da corrida
    imprimirStatusCorrida(posHamster1, posHamster2)

#Imprime mensagem informando quem ganhou
imprimirResultadoCorrida(vencedor)


