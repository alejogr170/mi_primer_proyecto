print()
print("El programa devuelve el menor de diez numeros")

numeros_usuario = []
numero_a_introducir = ""

while len(numeros_usuario) < 10:
    while not numero_a_introducir.isdigit():
        numero_a_introducir = input("Introduce un numero: ")
    print("Se ha introducido {}".format(numero_a_introducir))
    numeros_usuario.append(int(numero_a_introducir))
    numero_a_introducir = ""

numero_pequeño = numeros_usuario[0]

for numero in numeros_usuario:
    if numero_pequeño > numero:
        numero_pequeño = numero

print("Estos son los numeros que has introducido: {}".format(numeros_usuario))

print()

print("Y este es el numero mas pequeño: {}".format(numero_pequeño))