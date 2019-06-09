

te_apetece_un_helado_input = input("Te apetece un helado? (Si/No)").upper()
tienes_dinero_input = input("Tienes dinero? (Si/No)").upper()
alguien_te_invita_input = input("Tienes a alguien que te invite? (Si/No)").upper()
esta_el_carrito_input = input("Esta el carrito de los helados? (Si/No)").upper()

te_apetece_un_helado = te_apetece_un_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
alguien_te_invita = alguien_te_invita_input == "SI"
esta_el_carrito = esta_el_carrito_input == "SI"

if te_apetece_un_helado and (tienes_dinero or alguien_te_invita) and esta_el_carrito:
    print("Entonces... Ya estas tardando!")
else:
    print("Tranquilo, otra vez sera :[")