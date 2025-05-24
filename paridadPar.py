bandera=True
while (bandera):
    n=int(input("Ingrese un numero entero: "))
    if(n==99):
        bandera=False
    contador=0
    while (n!=0):
        digito=n%10
        if(digito % 2==0):
            contador+=1
        n=n//10
       
    if (contador%2==0):
        print("La cantidad de digitos pares es par")
    else:
        print("La cantidad de digitos pares es impar")
