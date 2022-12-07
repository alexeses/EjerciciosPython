if __name__ == "__main__":
    # Genera y muestra los números del 1 al 100 y calcula la suma de todos los números pares, por un
    # lado, y la suma de los números impares, por otro. Muestra los resultados.
    lista = [i for i in range(1, 101)]

    print(lista)

    suma_par = 0
    suma_impar = 0

    for i in lista:
        if i % 2 == 0:
            suma_par += i
        else:
            suma_impar += i
    print('La suma de los números pares es: ', suma_par)
    print('La suma de los números impares es: ', suma_impar)