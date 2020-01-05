arq = open('arquivoaula.txt', 'r')

texto = '''
oi tudo bem 
meu nome é rogers
'''

texto = arq.readlines()

for i in texto:
    print(i)

arq.close

arq = open('arquivoaula.txt', 'a')

texto = '''
oi tudo bem 
meu nome é rogers dinovo
'''

arq.write(texto)


arq.close