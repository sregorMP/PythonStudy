# Função print()

dia = 19
mes = 4
ano = 2018
nome = 'José'
sobrenome = 'Silva'
altura = 1.9


# O aluno José da Silva tem altura igual a 1.9
# %s para strings
# %d inteiros
# %f decimais

# 1ª forma
print('O aluno ' + nome + ' ' + sobrenome)
# 2ª forma
print('O aluno', nome, sobrenome)
# separado por /
print(dia, mes, ano, sep='/')
# outros metodos de impressão
print('Aluno %s foi aprovado ' % nome)
print('Bem vindo %s' % nome)
print('O aluno %s %s, tem altura igual a %f ' % (nome, sobrenome, altura))
# #
# #
# # #Funções de conversão
# # int('3')
# # float('3.14')
# # str(2.3)
# conversão valores em string
print('Aluno ' + nome + ' Tem altura igual a ' + str(altura))

# concatenar
quantidade = 10
estoque = 20
print("a quantidade %d e o estoque = %d " % (quantidade, estoque))

# inteiro
# float
# bool
# string
# qual o tipo?
print(type(estoque))

# manipulando strings
# contando
str = 'ccc bbb eee '
print(str.count('c'))
print(str)
# quant caracteres
print(len(str))
# maiuscula
str = str.upper()
print(str)

# iniciais maiusculas
str = str.title()
print(str)
