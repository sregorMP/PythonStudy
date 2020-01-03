import random

print('#################################################')
print('Bem vindo ao jogo de advinha')
print('Você terá sete chances para adivinhar o número')
print('#################################################')

numeroSecreto = random.randint(1, 100)
advinhador = input('Informe o nome do advinhador? ')
palpite = int(input('Qual o 1º palpite 0 - 100? '))
#print(numeroSecreto)

for x in range(1, 8):
    if (palpite > numeroSecreto):
        x += 1
        print('NUMERO MAIOR')
        print(x, 'tentativa')
        print('#################################################')
        palpite = int(input('Informe Nova Tentativa: '))
        continue
    elif (palpite < numeroSecreto):
        x += 1
        print('NUMERO MENOR')
        print(x, 'tentativa')
        print('#################################################')
        palpite = int(input('Informe Nova Tentativa: '))
        continue
    else:
        print('#################################################')
        print('PARABÉNS VOCÊ ACERTOU NA %d , VOCẼ TEM MUITA SORTE!' % x)
        print('#################################################')
        break
else:
    print('Acabaram as Tentativas')
