""" 
Dado un número ingresado por el usuario, determinar si el número es feliz.
Un número feliz es un número entero positivo que, al reemplazarlo repetidamente
por la suma de los cuadrados de sus dígitos, eventualmente llega al número 1. Si
entra en un ciclo que no incluye al 1, entonces se lo llama infeliz =(.

1**2 + 9**2 = 1 + 81 = 82
8**2 + 2**2 = 64 + 4 = 68
6**2 + 8**2 = 36 + 64 = 100
1**2 + 0**2 + 0**2 = 1+ 0 + 0 = 1 
"""

visitados = []  # Para guardar los números ya vistos

# Función que determina si un número es feliz
def es_feliz(n):

    while n != 1:
        if n in visitados:
            print(f"El numero que se repite es: {n}")
            return False  # Se detecta un ciclo → número infeliz
        visitados.append(n)

        suma = 0
        for digito in str(n):
            suma += int(digito) ** 2  # Sumar el cuadrado de cada dígito

        n = suma  # Actualizar n con la nueva suma

    return True  # Si llegamos al 1, es feliz

# Entrada del usuario
numero = int(input("Ingresa un número entero positivo: "))

# Salida del resultado
if es_feliz(numero):
    print("El número es feliz 😊")
    print(visitados)
else:
    print("El número es infeliz 😢")
    print(visitados)