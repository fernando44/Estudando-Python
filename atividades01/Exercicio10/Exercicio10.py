from random import randint

for cont in range(0, 10):
    rnd = randint(0, 10)
    var = int(input('Informe um valor para comparação: '))
    if rnd > var:
        print('valor {} é menor que {} '.format(var, rnd))

    elif rnd < var:
        print('valor {} é maior que {} '.format(var, rnd))

    else:
        print('valor {} igual ao valor {}'.format(var, rnd))

