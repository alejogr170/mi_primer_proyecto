print()
print("Este programa cuenta los elementos de una lista")

lista = []
elementos_lista = 0
cantidad_elementos = 0

while elementos_lista != "FIN":
    elementos_lista = str(input("Escribe lo q sea (FIN para terminar): "))
    if elementos_lista != "FIN":
        lista.append(elementos_lista)

for item in lista:
    cantidad_elementos += 1

print("Esta es tu lista: {}".format(lista))

print()

print("Y tiene {} elementos".format(cantidad_elementos))