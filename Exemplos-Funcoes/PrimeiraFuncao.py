# Área com a implementação das funções que o código vai usar
def minhaFuncao():
    # Comandos que serão executados quando a função minhaFuncao for chamada
    print("Ola funções!")

def funcaoComParametros(p1,p2,p3):
    print("Olá função com parâmetros!")
    print("Parâmetro 1: ",p1)
    print("Parâmetro 2: ",p2)
    print("Parâmetro 3: ",p3)


################ PROGRAMA PRINCIPAL ################ 
print("Olá!!!")

minhaFuncao()

funcaoComParametros()
funcaoComParametros(1, 2.2, "C")
a = "Rossana"
b = input("Digite uma coisa:")
funcaoComParametros(a,True, b)




