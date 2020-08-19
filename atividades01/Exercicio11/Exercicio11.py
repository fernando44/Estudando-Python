import modulo
print('digite 1 para somar\ndigite 2 para subtrair\ndigite 3 para multiplicar\ndigite 4 para dividir')
escolha = int(input('digite: '))
var1 = int(input('informe um valor: '))
var2 = int(input('informe outro valor: '))
if escolha ==1:
    var = modulo.soma(var1, var2)
elif escolha ==2:
    var = modulo.subtracao(var1,var2)
elif escolha ==3:
    var = modulo.multiplicacao(var1, var2)
elif escolha==4:
    var = modulo.divisao(var1, var2)
else:
    print('Valor invalido')

print('Resultado {}'.format(var))
