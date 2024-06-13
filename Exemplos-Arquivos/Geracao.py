# cria um arquivo vazio se não existir ou APAGA
# o conteúdo de um arquivo existente para escrita
nomeArquivo = 'Lalala.txt'

arqEscrita = open('Lalala.txt', 'w')

arqEscrita.write('15\n')

numero = 65

arqEscrita.write(str(numero))

arqEscrita.write('\n')

arqEscrita.write(chr(numero))

print(ord('A'))

arqEscrita.close()
