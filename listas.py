mares01 = ["Egeo", "Mediterraneo", "Cantabrico", "Báltico", "Ártico", "Índico", "Pacífico", "Atlántico", "Antártico"]
mares02 = ["Rojo", "Muerto", "Caspio", "Negro", "Aral", "Morto", "Sargasso", "Mariano"]
mares00 = mares01 + mares02

if __name__ == "__main__":
    # 1. La longitud de la lista mares1
    print('La longitud de la lista mares1 es: ', len(mares01))
    # 2. Los valores de todas las posiciones de la lista mares1
    print('Los valores de todas las posiciones de la lista mares1 son: ', mares01)
    # 3. La longitud de la lista mares2
    print('La longitud de la lista mares2 es: ', len(mares02))
    # 4. Los valores de todas las posiciones de la lista mares2
    print('Los valores de todas las posiciones de la lista mares2 son: ', mares02)
    # 5. La longitud de la lista mares
    print('La longitud de la lista mares es: ', len(mares00))
    # 6. Los valores de todas las posiciones de mares
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    # 7. Los valores de las posiciones 1, 2 y 3 de mares1
    print('Los valores de las posiciones 1, 2 y 3 de mares1 son: ', mares01[0:3])
    # 8. El índice o posición del mar ‘egeo’ en mares1
    print('El índice o posición del mar “egeo” en mares1 es: ', mares01.index('Egeo'))
    # 9. Los valores de las posiciones 4, 5 y 6 de mares2
    print('Los valores de las posiciones 4, 5 y 6 de mares2 son: ', mares02[3:6])
    # 10.  El índice o posición del mar caspio en mares2
    print('El índice o posición del mar “caspio” en mares2 es: ', mares02.index('Caspio'))
    # 11.  El índice o posición del mar caspio en mares
    print('El índice o posición del mar “caspio” en mares es: ', mares00.index('Caspio'))
