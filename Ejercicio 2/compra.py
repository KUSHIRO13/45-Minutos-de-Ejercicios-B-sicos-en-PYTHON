"""
Debe hacer un programa que verifique el costo del producto a vender, y lo que te dio
"""

producto = int(input("Cuanto cuesta ese producto?: "))
dinero = int(input("Cuanto te dio?: "))

if producto == dinero:
    print(f"""
    Puedes venderlo quedandote con: {dinero}""")
elif producto > dinero:
    print(f"Lastimosamente no puedes venderlo porque al cliente le faltan {producto - dinero} pesos")
else:
    print(f"Puedes venderlo quedandote con {dinero} pesos y al cliente le quedan {dinero - producto} pesos")