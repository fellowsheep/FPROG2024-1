import random

numeroSorteado = random.randint(1,3)

numeroLido = int(input('Digite um nro de 1 a 3: '))

if numeroLido == numeroSorteado:
    print('Voce acertou!!!')
else:
    print('ERRRROUUUU! O numero sorteado era ', numeroSorteado)

