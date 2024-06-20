import csv

arquivoCSV = open('Gatos.csv',encoding='utf-8')
leitor = csv.reader(arquivoCSV,delimiter=';')
dados = list(leitor) #aqui já temos uma tabela, mas apenas com strings

print(dados)

dadosONG = [] # dadosONG é a matriz que vai mesmo armazenar nossos dados para as consultas

# Preenchendo dadosONG, fazendo as conversões de tipo necessárias
#percorrer, linha a linha, nossa matriz (tabela) de dados
for i in range(len(dados)): #percorrendo as linhas (esse csv não tem cabeçalho)
    linha = [] #linha auxiliar
    for j in range(len(dados[0])): #percorrendo as colunas
        if j == 2: #terceira coluna é a idade
            linha.append(int(dados[i][j]))
        else:
            linha.append(dados[i][j])
    dadosONG.append(linha)