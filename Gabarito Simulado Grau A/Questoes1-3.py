'''def ehPrimo(n):
    #print('Verificando o nro ', n)
    for i in range(2,n):   
        #print(i)
        if n % i == 0:
            return False
            break
    return True'''

def ehPrimo(n):
    primo = True
    cont = 2
    while cont < n:
        if (n % cont == 0): #é divisivel por cont
            primo = False
        cont = cont + 1
    return primo



contPrimos = 0
n = 2
while contPrimos < 10:
    if ehPrimo(n):
        contPrimos += 1
        print(contPrimos,": ",n)
    n += 1

totalNros = 0
totalPos = 0
totalNeg = 0
totalDiv2 = 0
totalDiv5 = 0
totalPrimos = 0

nro = -1

while nro != 0:
    nro = int(input('Digite um nro: '))
    if nro > 0:
        totalPos += 1
    if nro < 0:
        totalNeg += 1
    if nro % 2 == 0:
        totalDiv2 += 1
    if nro % 5 == 0:
        totalDiv5 += 1
    if ehPrimo(nro) == True:
        totalPrimos +=1
    totalNros += 1


print(totalNros)

print('Porcentagem de nros positivos: ', totalPos/totalNros * 100, '%')
print('Porcentagem de nros negativos: ', totalNeg/totalNros * 100, '%')
print('Porcentagem de nros divisiveis por 2: ', totalDiv2/totalNros * 100, '%')
print('Porcentagem de nros divisiveis por 5: ', totalDiv5/totalNros * 100, '%')
print('Porcentagem de nros primos: ', totalPrimos/totalNros * 100, '%')
