dato=1
#sale del bucle para cualquier fecha "99xxxx"
while (dato != 99):

    dato = int(input("Ingrese fecha en formato ISO (AAAAMMDD)"))

    #Extraigo los dos digitos correspondientes al dia
    dia = dato %10
    dato = dato //10
    dia = dia + (dato%10)*10 
    dato = dato //10

    #Extraigo los dos digitos correspondientes al mes
    mes = dato %10
    dato = dato //10
    mes = mes + (dato %10)*10
    dato = dato //10

    #Defino una tupla para los nombres de meses
    meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    
    if (0<mes<13 and 0<dia<31) and not(mes==2 and dia>28) or (0<dia==31 and mes==(1 or 3 or 5 or 7 or 8 or 10 or 12)):
        print(f"Es {dia} de {meses[mes-1]} de {dato}")
    else:
        print("La fecha ingresada es invalida")