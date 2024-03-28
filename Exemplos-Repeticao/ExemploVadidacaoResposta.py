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
    