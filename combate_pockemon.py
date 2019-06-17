
pockemon_elegido = input("Contra que pockemon quieres combatir? ( Squirtle / Charmander / Bulbasaur ):").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_bulbasaur = 10
ataque_squirtle = 8
ataque_charmander = 7

if pockemon_elegido == "SQUIRTLE":
    vida_enemigo = 90

if pockemon_elegido == "CHARMANDER":
    vida_enemigo = 80

if pockemon_elegido == "BULBASAUR":
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0 :
    ataque_elegido = input("¿Que ataque deseas usar ( Bola voltio / Chispazo)?:").upper()
    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
    if ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    print("La vida de tu oponente es:  " + vida_enemigo)


