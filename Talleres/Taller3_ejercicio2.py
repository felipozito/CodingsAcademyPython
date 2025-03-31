"""Cecilia decide ir de compras al supermercado, se ubica la sesión de frutas y desea ir añadiendo una fruta diferente en su carrito, pero cada vez que añade una fruta el carrito no identifica si esa fruta esta añadida o no, por lo que le tocará a Cecilia identificar que la fruta no este repetida y le tomará mucho tiempo finalizar sus compras.

Ayuda a Cecilia a optimizar su tiempo de compras, crea un carrito de compras inteligente que permita identificar si la fruta ya se encuentra añadida y sino se encuentra añadida debe añadirla.

El carrito iniciará con las siguientes frutas: carritoFrutas = ["manzana", "sandia", "melon"]

Utilizar (input, for, if, break, entre otras sintaxis de python para añadir elementos, se permite creatividad).
"""
frutas= ["manzana", "sandia", "melon"]
fruta=input("Ingrese una fruta: ")
for i in frutas:
    if fruta==i:
        print("La fruta ya se encuentra en el carrito")
        break
    else:
        frutas.append(fruta)
        print("La fruta se ha añadido al carrito")
        break   
print(frutas)
    