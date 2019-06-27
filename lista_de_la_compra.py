print()
print()

print('Está es la lista de la compra:')

lista_de_la_compra = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("Escribe lo que necesites (para salir escribe FIN) :")
    if input_usuario != "FIN":
        lista_de_la_compra.append(input_usuario)

cantidad_de_elementos = len(lista_de_la_compra)
indice = 0

while indice < cantidad_de_elementos:
    print('Tengo que comprar {}'.format(lista_de_la_compra[indice]))
    indice += 1
