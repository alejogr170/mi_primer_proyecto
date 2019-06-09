

numero = 4

print("Debes adivinar un número entre 0 y 10, y tienes dos intentos")

respuesta = int(input("¿Cual crees que es?___"))

if respuesta  == numero:
    print("Enhorabuena, has ganado")

else:
    print("¡Oh valla!, has fallado ")
    respuesta_2 = int(input("Prueba de nuevo___"))

if respuesta_2 == numero:
    print("Enhorabuena, has ganado")

else:
    print("Has perdido ;) , ¡Que malo eres!")
