
numero = int(input('digite o numero fatorial: \n'))
fatorial = 1 
for i in range(numero, 0, -1):
    fatorial = fatorial * i
print(fatorial)