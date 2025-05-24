# # Ejercicio:
# # Definir una lista de 1 al 1000 y determinar todos los numeros primos
# # que aparecen en dicha lista. Posteriormente guardarlos en una nueva 
# # lista llamada numeros_primos.


#Defino la lista del 2 al 1000 incluido
listaNumeros = list(range(2,1001))

numeros_primos = []

for num in listaNumeros:
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