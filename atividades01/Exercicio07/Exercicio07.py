#pedra papel tesoura
# 0      1      2
from random import randint

print('Suas opções: ')
print('[0] pedra\n[1]papel\n[2]tesoura')
opcao = int(input('informe sua jogada: '))
computador = randint(0, 2)

if computador == 0:
    if opcao ==0:
        print('Empate')
    elif opcao ==1:
        print('vitoria')
    else:
        print('derrota')

elif computador ==1:
    if opcao ==0:
        print('derrota')

    elif opcao ==1:
        print('empate')

    else:
        print('vitoria')

else:
    if opcao==0:
        print('vitoria')

    elif opcao==1:
        print('derrota')

    else:
        print('empate')
