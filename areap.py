if __name__ == "__main__":
    # Escribe un programa en Python que calcule el área y el perímetro de un rectángulo pidiendo al
    # usuario que introduzca la base y la altura del mismo (con decimales).
    base = float(input('Introduce la base del rectángulo: '))
    altura = float(input('Introduce la altura del rectángulo: '))
    area = base * altura
    perimetro = 2 * (base + altura)
    print('El área del rectángulo es: ', area)
    print('El perímetro del rectángulo es: ', perimetro)


