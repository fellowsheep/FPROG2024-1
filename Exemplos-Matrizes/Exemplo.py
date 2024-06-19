import random

# Função que imprime os elementos de uma matriz, percorrendo os índices de linha e coluna
def imprimirMatriz(M):
    # Armazenando o nro de linhas e colunas
    nLinhas = len(M)
    nColunas = len(M[0])

    # Percorrendo (fazendo a varredura) a matriz utilizando os índices de linha e coluna
    for l in range(nLinhas):  
        for c in range(nColunas):
            # Dentro do contexto do segundo for, podemos acessar o elemento com índice de linha e coluna
            print(M[l][c], end='\t')
            # .. pode ter mais comandos aqui!
        # Dentro do contexto do primeiro for, podemos fazer operações utilizando a linha inteira
        print() #print para quebra de linha

#---------------------------------------------------------------------------------

# Criação de uma matriz com 3 linhas e 4 colunas - matriz 3 x 4

      #0  1   2   3
M = [ [1, 2,  3,  4],     # 0 
      [5, 6,  7,  8],     # 1
      [9, 10, 11, 12]]    # 2

print(M)

# Imprime o nro de linhas da matriz
print(len(M))


# Imprime o nro de colunas da matriz
print(len(M[0]))

print()

imprimirMatriz(M)

print()

# Criando uma matriz vazia
mat = []

# Ler do usuário o nro de linhas e colunas que a matriz terá
nLinhas = random.randint(1, 10)  #int(input('Digite o nro de linhas: '))
nColunas = random.randint(1, 10) #int(input('Digite o nro de colunas: '))

for l in range(nLinhas):
    novaLinha = []
    for c in range(nColunas):
        novoValor = random.randint(0, 100)
        novaLinha.append(novoValor) #adicionando o novo valor na linha auxiliar (nova linha)
    mat.append(novaLinha)

imprimirMatriz(mat)
print()

# Ler do usuário o nro de linhas e colunas que a matriz terá
nLinhas = random.randint(1, 10)  
nColunas = random.randint(1, 10)

print(nLinhas, 'x',nColunas)

# Inicializa a matriz nLinhas x nColunas com zeros
mat2 = []
for i in range(nLinhas):
    # Cria uma nova lista de zeros para cada linha
    linha = [0] * nColunas
    mat2.append(linha)


# Sorteia valores para cada posição, sobrescrevendo os zeros
for l in range(nLinhas):
    for c in range(nColunas):
        #Agora como a matriz mat2 não é vazia, já temos os elementos de indice l e c
        mat2[l][c] = random.randint(0,100)

imprimirMatriz(mat2)


