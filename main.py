
edad = 12

altura = 1.79

nombre = "juan"

estado = True

#lista enteros
lista1 = [10, 5, 3, 9]

#lista decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]

#lista strings
lista3 = ["lunes", "martes", "miercoles"]

'''
lista de distintos tipos
'''

lista4 = ["juan", 45, 1.92, False]


if __name__ == '__main__':

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    print(lista1[3])