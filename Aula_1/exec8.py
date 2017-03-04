par = []
impar = []

for number in range(100,200):
    if number % 2 == 0:
        par.append(number)
    else:
        impar.append(number)

print(par)
print(impar)