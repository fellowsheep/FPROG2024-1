sexo = 'F'
idade = 65

if sexo == 'F': #testa se a var sexo é feminino
    #aqui estarão as ações que devem executar se a avaliação do if for verdadeiro
    print('É do sexo feminino')
    if idade >= 65:
        print('Possui 65 anos ou mais de idade')
    else:
        print('Possui menos de 65 anos de idade')
else:
    #aqui estarão as ações que devem executar se a avaliação do if for falsa
    print('Não é do sexo feminino')

if sexo == 'F' and idade >= 65:
    print('É do sexo feminino e possui 65 anos ou mais de idade')

#####################
mediaFinal = 6.0
frequencia = 0.75

#Testar a reprovação
if mediaFinal < 6.0:
    print('Reprovado por media inferior a 6.0!')
elif frequencia < 0.75:
    print('Reprovado por faltas!')
else:
    print('Aprovado!')

if (mediaFinal < 6.0 or frequencia < 0.75):
    print('Reprovado!')