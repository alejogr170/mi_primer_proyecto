print()
print("El programa devuelve el menor de diez numeros")

numeros_usuario = []
numero_a_introducir = ""

while len(numeros_usuario) < 10:
    while not numero_a_introducir.isdigit():
        numero_a_introducir = input("Introduce un numero: ")
    print("Se ha introducido {}".format(numero_a_introducir))
    numero_a_introducir = ""
