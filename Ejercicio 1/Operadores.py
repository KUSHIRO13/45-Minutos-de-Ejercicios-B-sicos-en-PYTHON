"""
Realizar un programa que muestre la suma, resta, multiplicacion y divicion de dos numeros enteros
"""
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese un numero: "))

print(f"""
La suma de los dos numeros es: {n1 + n2}
La resta de los dos numeros es: {n1 - n2}
La multiplicacion de los dos numeros es: {n1 * n2}
La divicion de los dos numeros es: {round(n1 / n2,2)}
""")