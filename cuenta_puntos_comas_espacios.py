print()
print()
print()

frase_del_usuario = input("Escribe aqui tu texto o frase:  ")

numero_de_puntos = 0
numero_de_comas = 0
numero_de_espacios = 0

for caracter in frase_del_usuario:
    if caracter == " ":
        numero_de_espacios += 1
    if caracter == ",":
        numero_de_comas += 1
    if caracter == ".":
        numero_de_puntos += 1

print("El numero de espacios es {}, el numero de comas es {} y el numero de puntos es {}".format(numero_de_espacios,numero_de_comas,numero_de_puntos))