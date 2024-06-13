def cifrarMensagem(msg):
    msgCifrada = ''
    for i in range (len(msg)):
        code = ord(msg[i]) - 1
        msgCifrada = msgCifrada + chr(code)
    return msgCifrada

def decifrarMensagem(msgCifrada):
    msgDecifrada = ''
    for i in range(len(msgCifrada)):
        code = ord(msgCifrada[i]) + 1
        msgDecifrada += chr(code)  # msgDecifrada = mgsDecifrada + chr(code)
    return msgDecifrada

###########################################

msg = input('Digite uma mensagem: ')

msgCifrada = cifrarMensagem(msg)

print(msgCifrada)

#Salvar a mensagem cifrada em um arquivo

nomeArquivo = input('Digite o nome do arquivo que deseja salvar: ')

arqSaida = open(nomeArquivo,'w')

arqSaida.write(msgCifrada)

arqSaida.close()

#Ler o arquivo com a mensagem cifrada e decifrar a mensagem
nomeArquivo = input('Digite o nome do arquivo que deseja abrir: ')

arqEntrada = open(nomeArquivo,'r')

mensagemCifrada = arqEntrada.read() #armazena todo o conteúdo do arquivo em uma string

arqEntrada.close()

mensagemDecifrada = decifrarMensagem(mensagemCifrada)

print(mensagemDecifrada)

    

