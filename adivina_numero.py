numero = 6

print("Debes adivinar en 5 intentos")

intento_primero = int(input("Elige numero:"))

if intento_primero == numero:
    print("¡Enhorabuena! Has ganado")
else:
    print("¡Fallaste!")

    intento_segundo = int(input("Prueba"))

    if intento_segundo == numero:
        print("Ganaste")
    else:
        print("Fallaste")

        intento_tercero = int(input("Prueba"))

        if intento_tercero == numero:
            print("Ganaste")
        else:
            print("Fallaste")

            intento_cuarto = int(input("Prueba"))

            if intento_cuarto == numero:
                print("Ganaste")
            else:
                print("Ultimo intento")

                intento_quinto = int(input("Ultimo intento:"))

                if intento_quinto == numero:
                    print("Ganaste")
                else:
                    print("Ya perdiste, era el 6")
