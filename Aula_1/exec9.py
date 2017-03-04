notas = []
aux1 = int(input('Numero de notas: '))

for aux2 in range(aux1): 

    valor = int((input('Insira a nota do aluno: ')))

    if valor < 0 or valor > 100:
        print('Nota desprezada!')

    elif valor < 70:
        print('Turma de baixa performace')
        notas.append(valor)   
        break

    else:
        notas.append(valor)

else:
    print('Turma de alta performace!')


print(notas)