import os # Biblioteca de sofware do Python

# 1: Menu com as opções de escolha
def menuMaquinaCafe():    
    # Limpa a tela - Win/Linux/MacOS 
    os.system('cls' if os.name == 'nt' else 'clear') 

    print('\n..:: O que você deseja fazer? ::..\n')

    print('1 - Trocar o refil dos ingredientes')
    print('2 - Consultar a quantidade de ingredientes')
    print('3 - Fazer um café')
    print('0 - Desligar a máquina (SAIR)\n')
    item = input('Escolha uma opção: ')
    return item


# 3: AÇÃO: Uma função para cada item do menu
def trocarRefil():
    print('\nOpção escolhida: Trocar Refil\n')

def consultar():
    print('\nOpção escolhida: Consultar Ingredientes\n')

def prepararCafe():
    print('\nOpção escolhida: Preparar café\n')

# 2: LOOP: Processamento do menu e chamada das funções
escolha = ''
while(escolha != '0'):
    escolha = menuMaquinaCafe()
    if escolha == '1':
        trocarRefil()
    elif escolha == '2':
        consultar()
    elif escolha == '3':
        prepararCafe()
    elif escolha == '0':
        print('\nSaindo...\n')
    else:
        print('\nOpção desconhecida!\n')

    input('Pressione ENTER para continuar')