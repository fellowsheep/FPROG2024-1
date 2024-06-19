#Lendo o arquivo de perguntas e armazenando numa matriz em que cada linha trata de uma questão, e cada coluna armazena uma opção

arqQuestoes = open('questoes.txt', 'r', encoding='utf-8')
questoesProva = []
pergunta = arqQuestoes.readline()
while pergunta: #enquanto retornar uma string não vazia 
    questao = []
    questao.append(pergunta.strip()) # Remove \n e espaços em branco
    for i in range(5):
        alternativa = arqQuestoes.readline()
        questao.append(alternativa.strip())
    #já tenta iniciar a leitura da próxima linha
    questoesProva.append(questao)
    pergunta = '\n'
    while pergunta == '\n':
        pergunta = arqQuestoes.readline()

print(questoesProva)

respostas = []

for i in range(len(questoesProva)):
    print(i+1,' - ', end='')
    print(questoesProva[i][0])
    for j in range (1, 6):
        print(chr(96+j),') ', end='')
        print(questoesProva[i][j])
    resposta = input('Qual é a alternativa correta? ')
    respostas.append(resposta)
    print()

