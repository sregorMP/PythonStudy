# Programa Aprovação
print('####Bem vindo ao sistema calculo de média####')
nome = input('Qual o seu nome: ')
materia = input('Qual a materia que quer média? ')
n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
n3 = float(input('Digite a Terceira nota: '))
n4 = float(input('Digite a Quarta nota: '))
media = (n1 + n2 + n3 + n4)/4

if media < 7:
    print('Aluno %s você foi REPROVADO. Sua média em %s foi %.1f' %(nome, materia, media))
else:
    print('Aluno %s, você foi APROVADO. Sua média em %s foi %.1f' %(nome, materia, media))