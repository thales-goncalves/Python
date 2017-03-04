def somar_imposto(taxa_imposto, custo):
    valor = custo * (1+(taxa_imposto/100))
    return valor


if __name__=='__main__':
    taxa_imposto = int(input ('Forneca a taxa em %: '))
    custo = int(input ('Forneca o valor a ser taxado: '))
    print(somar_imposto(taxa_imposto,custo))