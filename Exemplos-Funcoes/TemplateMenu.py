import os # Biblioteca de software do Python

################ FUNÇÕES ################
# Menu com as opções de escolha
def menu():
  print('\n..:: Desenvolvendo programas com menus ::..\n')
  
  # Limpa a tela - Win/Linux/MacOS 
  os.system('cls' if os.name == 'nt' else 'clear') 
  print('1 - Opção 1')
  print('2 - Opção 2')
  print('3 - Opção 3')
  print('0 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

# AÇÃO: Uma função para cada item do menu
def opcao_1():
	print('\nOpção escolhida: 1\n')
def opcao_2():
	print('\nOpção escolhida: 2\n')
def opcao_3():
	print('\nOpção escolhida: 3\n')


################ PROGRAMA PRINCIPAL ################
# LOOP: Processamento do menu e chamada das funções
escolha = ''
while(escolha != '0'):
    escolha = menu()
    if escolha == '1':
        opcao_1()
    elif escolha == '2':
        opcao_2()
    elif escolha == '3':
        opcao_3()
    elif escolha == '0':
        print('\nSaindo...\n')
    else:
        print('\nOpção desconhecida!\n')
    input('Pressione ENTER para continuar')




