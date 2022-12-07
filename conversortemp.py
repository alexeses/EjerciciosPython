if __name__ == "__main__":
    # Escribe un programa en Python que convierta la temperatura dada en grados Fahrenheit, si se
    # indica que son grados Celsius, o en grados Celsius, si se indica que son grados Fahrenheit.

    tipo = input('Introduce la unidad de medida de la temperatura (F o C): ')
    temperatura = float(input('Introduce la temperatura: '))
    if tipo == 'F':
        celsius = (temperatura - 32) * 5 / 9
        print('La temperatura en grados Celsius es: ', celsius)
    else:
        fahrenheit = (temperatura * 9 / 5) + 32
        print('La temperatura en grados Fahrenheit es: ', fahrenheit)
