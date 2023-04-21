def suma_5_enteros():
    #definir variables
    lista = []
    contadorwhile = 0
    tamano = 5
    suma = 0

    #ingresamos los numeros
    while contadorwhile < tamano:
        lista.append(int(input(f"ingrese numero {contadorwhile+1} ")))
        contadorwhile += 1

    #sumamos los numeros
    contadorwhile = 0
    while contadorwhile < tamano:
        suma += lista[contadorwhile]
        contadorwhile += 1

    print("los elementos de la lista son: ")

    for numero in lista:
        print(numero, end=', ')

    print("\nla suma de todos sus elementos es: ")
    print(suma)
