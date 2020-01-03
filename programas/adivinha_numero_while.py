import random

print('#################################################')
print('Bem vindo ao jogo de advinha')
print('Você terá sete chances para adivinhar o número')
print('#################################################')

numeroSecreto = random.randint(1, 100)
advinhador = input('Informe o nome do advinhador? ')
print(numeroSecreto)
tentativas = 1
while tentativas <= 7:
    chute = (int(input('Digite seu Chute: ')))
    if chute < numeroSecreto:
        print('Essa foi a %d' % tentativas)
        print('Você errou e seu chute foi menor')
    elif chute > numeroSecreto:
        print('Essa foi a %d' % tentativas)
        print('Você errou e seu chute foi maior')
    else:
        print('Você acertou na %d. Você tem muita sorte!' % tentativas)
        break
    tentativas += 1
if tentativas == 8:
    print('Acabaram as tentativas! Fim de jogo!')
