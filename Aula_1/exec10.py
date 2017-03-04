def add(valor1, valor2):
    print('Resultado:')
    print( valor1 + valor2)

def sub(valor1, valor2):
    print('Resultado:')
    print( valor1 - valor2)

def mul(valor1, valor2):
    print('Resultado:')
    print( valor1 * valor2)

def div(valor1, valor2):
    print('Resultado:')
    print( valor1 / valor2)

op = 0

while op != 5:


    print('\nEscolha a operaçao')
    print('1 - Soma ')
    print('2 - Subtraçao ')
    print('3 - Multiplicacao ')
    print('4 - Divisao ')
    print('Other - Sair ')

    op = eval(input())

    if op == 1:
        print('Insira dois valores: ')
        valor1 = eval(input('Valor 1 = '))
        valor2 = eval(input('Valor 2 = '))
        add(valor1,valor2)

    elif op == 2:
        print('Insira dois valores: ')
        valor1 = eval(input('Valor 1 = '))
        valor2 = eval(input('Valor 2 = '))
        sub(valor1,valor2)

    elif op == 3:    
        print('Insira dois valores: ')
        valor1 = eval(input('Valor 1 = '))
        valor2 = eval(input('Valor 2 = '))
        mul(valor1,valor2)

    elif op == 4:
        print('Insira dois valores: ')
        valor1 = eval(input('Valor 1 = '))
        valor2 = eval(input('Valor 2 = '))
        div(valor1,valor2)

    else:
        break

    

   



