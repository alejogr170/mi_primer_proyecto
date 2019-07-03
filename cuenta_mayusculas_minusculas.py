print()
print()

frase_del_usuario = input("Escribe aquuí tu texto: ")

numero_mayusculas = 0
numero_minusculas = 0

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for letter in frase_del_usuario:
    for item in mayusculas:
        if item == letter:
            numero_mayusculas += 1
    for item_2 in minusculas:
        if item_2 == letter:
            numero_minusculas += 1

print("El numero total de MAYUSCULAS es de {} y el numero de minusculas es de {}".format(numero_mayusculas, numero_minusculas))
