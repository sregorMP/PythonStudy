
um_array = []  # Lista
print(type(um_array))

um_array = []

dicionarios = {}  # Lista do tipo Dict
print(type(dicionarios))

# Entendendo sobre tuplas

# Declaração de Listas do tipo Tuplas
dias_da_semana = ('Domingo', 'Segunda', 'Terça',
                  'Quarta', 'Quinta', 'Sexta', 'Sábado')
dias_da_semana_2 = 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'

print(type(dias_da_semana))
print(type(dias_da_semana))

# Tuplas de um único elemento colocar uma "," apos o elemento

tupla1 = 'a',
tupla2 = ('b',)


print(type(tupla1))
print(type(tupla2))

idade = [20, 30, 40]

idade.append(50)
idade.insert(3, 'rogers')

print(idade)
idade.pop(3)
print(idade)

idade = [310, 22, 40, 50]

idade.sort(reverse=True)
print(min(idade))

print('minha lista')
x = [1, 2, 3, 4, 5]

print(x)

y = int(input('digite um numero para apagar da lista: '))

if y in x:
    x.remove(y)
    print('o valor foi removido')
else:
    print('valor não existe na lista')
print(x)

print('meu dicionario')
z = {'nome': 'rogers', 'teste': 30}
print(len(z))
