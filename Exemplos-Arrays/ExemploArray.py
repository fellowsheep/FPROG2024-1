# Função que percorre os elementos do array (vetor) por índice e imprime os seus valores
def imprimirVetor(v):
    n  = len(v)
    for i in range(n):
        print(v[i], end= ' ')

#------------------------------------------------------------------------------------- 

# Criacao de um array já inicializado com 10 inteiros
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Armazenando o tamanho do array em uma variável
tamanho = len(A)

print(A)
print('Este array possui ', tamanho, 'elementos.')
print('Este array possui ', len(A), 'elementos.')

# Imprimir (acessar) o primeiro elemento do array
print('Primeiro elemento do array: ', A[0]) #os arrays sempre iniciam com o índice zero 

# Imprimir (acessar) o último elemento do array
print('Último elemento do array: ', A[tamanho - 1]) #utilizando a variável que armazena o tamanho
print('Último elemento do array: ', A[len(A) - 1]) #chamando diretamente a função que retorna o tamanho

# Imprimir (acessar) um elemento a partir de uma posição (variável que armazene a posição e não o índice)
pos = 5  # esta variável é pra indicar (no exemplo) que gostaríamos da 5a posição do vetor (índice 4)
print('Elemento que está na posição', pos, ' do array: ', A[pos - 1] )

# Inicializações alternativas
B = ['a', 'a','a','a','a']
B = ['a'] * 200
print(B)

C = list(range(5, 20, 3)) # Typecast de uma sequência
print(C)

D = [ x**2 for x in range(1, 20) if x % 3 == 0 ] # List Comprehension
print(D)

# Percorrer/varrer uma array

# Por elemento (percorrendo os elementos do array A)
for e in A:
    print('Valor: ', e)

# Por índice (percorrer o array A acessando os elementos a partir do índice)
for i in range(tamanho): #o range com 1 parâmetro retorna de 0 até o valor do par - 1
    print('Valor de A[',i,']: ', A[i])

# Criação de um array vazio
vet = []

# Ler do usuário o nro de elementos do array
n = int(input('Digite o nro de elementos do array:'))

# Preencher o vetor com números lidos do usuário
for i in range(n):
    #Ler o valor e armazenar no elemento em uma variável
    valor = int(input('Digite o valor do elemento: '))
    vet.append(valor)

imprimirVetor(vet)

