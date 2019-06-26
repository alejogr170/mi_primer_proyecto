print()
print()

print('Está es la lista de la compra:')
lista_de_la_compra = ['Lechugas', 'Aceitunas', 'Pimientos', 'Tomates', 'Azucar']

cantidad_de_elementos = len(lista_de_la_compra)
indice = 0

while indice < cantidad_de_elementos:
    print('Tengo que comprar {}'.format(lista_de_la_compra[indice]))
    indice += 1
