ano = int(input("Entre com o ano: "))
print(ano)

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano %s é bissexto" % ano)
        else:
             print("O ano %s não é bissexto" % ano)
    else:
         print("O ano %s é bissexto" % ano)
else:
     print("O ano %s não é bissexto" % ano)