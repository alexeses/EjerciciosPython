if __name__ == "__main__":
    # Escribe un programa en Python que pida al usuario dos números.
    # • Si la suma de ambos números es mayor que 100 se mostrará el resultado de la suma y el
    # mensaje: 'La suma supera la centena'. De lo contrario se mostrará el resultado de la suma y el
    # mensaje ‘el resultado de la suma no supera la centena’.99

    num1 = float(input('Introduce el primer número: '))
    num2 = float(input('Introduce el segundo número: '))
    suma = num1 + num2
    if suma > 100:
        print('La suma supera la centena')
        print('El resultado de la suma es: ', suma)
    else:
        print('El resultado de la suma no supera la centena')
        print('El resultado de la suma es: ', suma)
