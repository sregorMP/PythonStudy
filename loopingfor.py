print('======looping for1======')
for x in range(10):
    print(x)

print('======looping for2 impressão até o 10======')
for x in range(1, 11):
    print(x)

print('======looping for3 pulando por intervalos======')
for x in range(0, 10, 3):
    print(x)

print('======looping for4 para cada elemento apresentara o valor======')
carros = ['Camaro', 'Ranger', 'Pajero', 'Hilux']
for a in carros:
    print(a)
print('Mesmo Resultado')
for a in range(len(carros)):
    print(carros[a])
    
print('Contem ' + str(len(carros)) + ' carros')