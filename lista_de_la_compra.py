print()
print()

lista_de_la_compra = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("Escribe lo que necesites (para salir escribe FIN) :")
    if input_usuario != "FIN":
        lista_de_la_compra.append(input_usuario)

print('Está es la lista de la compra:')

for item in lista_de_la_compra:
    print("Tengo que comprar {}".format(item))
