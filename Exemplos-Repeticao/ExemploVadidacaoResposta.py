#.....
resposta = 'X'
while resposta != 'S' and resposta != 'N':
    resposta = input('Responda Sim (S) ou Não (N):')
    if resposta == 'S':
        print('Como vc respondeu sim.........')
    elif resposta == 'N':
        print('Como vc respondeu não.........')
    else:
        print('Resposta inválida!')

#.....
invalida = True
while invalida == True:
    resposta = input('Responda Sim (S) ou Não (N):')
    if resposta == 'S':
        print('Como vc respondeu sim.........')
        invalida = False
    elif resposta == 'N':
        print('Como vc respondeu não.........')
        invalida = False
    else:
        print('Resposta inválida!')




    