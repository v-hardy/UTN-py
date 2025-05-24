ingresado = int(input("ingrese entero mayor a 1: "))
numeros_primos = []

for num in range(2,ingresado+1):
    esPrimo = True  #Suponemos que el número es primo
    acumulador = 2
    while acumulador < num:
        if num % acumulador == 0:
            #Si entra al if significa que encontro un divisor entonces no es primo
            esPrimo = False
            break
        acumulador=acumulador+1
    #agrego el numero porque es primo a la lista de primos
    if esPrimo:
        numeros_primos.append(num)

print("Lista de numeros primos")
print(numeros_primos)