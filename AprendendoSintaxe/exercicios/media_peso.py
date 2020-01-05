
x = []
contador = 0
for i in range(0, 7):
    x.append(float(input('digite um peso\n')))
    if x[i] > 90:
        contador += 1
print(f'existem {contador} pessoas acima de 90kg e a media dlees é {sum(x)/len(x):2f}')
