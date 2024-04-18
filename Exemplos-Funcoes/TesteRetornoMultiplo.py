############### FUNÇÕES ##################

def modificaValores(posicao, casado, curso):
    posicao = posicao + 1
    casado = True
    curso = "Direito"
    return posicao,casado,curso

def printValores(posicao,casado,curso):
    print(' Posicao: ', posicao)
    print(' É casado: ', casado)
    print(' Curso: ', curso)
    print('-------------')

############## PROGRAMA PRINCIPAL ################

posicaoJogador1 = 0
jogador1Casado = False
jogador1Curso = ""

printValores(posicaoJogador1,jogador1Casado,jogador1Curso)

posicaoJogador1,jogador1Casado,jogador1Curso = modificaValores(posicaoJogador1,jogador1Casado,jogador1Curso)

printValores(posicaoJogador1,jogador1Casado,jogador1Curso)



