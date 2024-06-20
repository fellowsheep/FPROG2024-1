import csv

arquivoCSV = open('playlist.csv',encoding='utf-8')
leitor = csv.reader(arquivoCSV,delimiter=',')
dados = list(leitor)

print(dados)

playlist = [] #variavel que vai armazenar nossos dados "tratados"

#percorrer, linha a linha, nossa matriz (tabela) de dados
for i in range(1,len(dados)): #percorrendo as linhas, ignorando o cabecalho
    linha = []
    for j in range(len(dados[0])): #percorrendo as colunas
        if j == 3: #quarta coluna
            linha.append(int(dados[i][j]))
        else:
            linha.append(dados[i][j])
        print(dados[i][j], end='\t')
    playlist.append(linha)
    print() #quebra de linha

print(playlist)

# Imprimir nomes das músicas apenas
for i in range(len(playlist)):
    print(playlist[i][0])

print('-------------------------------')

# Imprimir nomes das músicas lançadas na década de 90
for i in range(len(playlist)):
    ano = playlist[i][3]
    if ano >= 1990 and ano < 2000:
        print(playlist[i][0])