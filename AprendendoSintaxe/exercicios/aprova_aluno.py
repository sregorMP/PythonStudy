nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
n1 = int(input('digite sua nota 1: '))
n2 = int(input('digite sua nota 2: '))
nome = nome.lower().title()
print('Olá %s' % nome)
media = int((n1 + n2) / 2)

if media >= 6 and idade >= 18:
    print('Parabéns %s você foi aprovado' % nome)
else:
    print('Infelizmente você foi reprovado!')
