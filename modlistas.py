mares01 = ["Egeo", "Mediterraneo", "Cantabrico", "Báltico", "Ártico", "Índico", "Pacífico", "Atlántico", "Antártico"]
mares02 = ["Rojo", "Muerto", "Caspio", "Negro", "Aral", "Morto", "Sargasso", "Mariano"]
mares00 = mares01 + mares02

if __name__ == "__main__":
    # 1. Cambia a la vez los valores de los elementos undécimo y duodécimo de la lista mares por los valores 'del norte' y 'alborán'. Muestra la lista mares
    print('Los valores de las posiciones 11 y 12 de mares son: ', mares00[10:12])
    mares00[10:12] = ['del norte', 'alborán']
    print('Los valores de las posiciones 11 y 12 de mares son: ', mares00[10:12])
    # 2. En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    mares00.insert(4, 'Báltico')
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    # 3. Borra el quinto elemento de la lista mares. Muestra la lista mares
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    del mares00[4]
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    # 4. Muestra la longitud de la lista mares
    print('La longitud de la lista mares es: ', len(mares00))
    # 5. Muestra los valores repetidos en la lista mares usando el método correspondiente
    print('Los valores repetidos en la lista mares son: ', mares00.count('Báltico'))
    # 6. Elimina el tercer elemento de la lista mares y guárdalo en la variable mar1
    mar1 = mares00.pop(2)
    print('El tercer elemento de la lista mares es: ', mar1)
    # 7. Elimina el último elemento de la lista mares y guárdalo en la variable mar2
    mar2 = mares00.pop()
    print('El último elemento de la lista mares es: ', mar2)
    # 8. Guarda el valor del noveno elemento en la variable mar3
    mar3 = mares00[8]
    print('El noveno elemento de la lista mares es: ', mar3)
    # 9. Muestra los valores de las variables mar1, mar2 y mar3
    print('Los valores de las variables mar1, mar2 y mar3 son: ', mar1, mar2, mar3)
    # 10.  Elimina el primer elemento de la lista mares con valor 'báltico'. Muestra la lista mares
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    mares00.remove('Báltico')
    print('Los valores de todas las posiciones de la lista mares son: ', mares00)
    # 11.  Elimina todos los elementos de la lista mares
    mares00.clear()
    # 12.  Ordena por orden alfabético de 'a' a 'z' los elementos de la lista mares1
    mares01.sort()
    print('Los valores de todas las posiciones de la lista mares1 son: ', mares01)
    # 13.  Ordena por orden alfabético de 'z' a 'a' los elementos de la lista mares2\
    mares02.sort(reverse=True)
    print('Los valores de todas las posiciones de la lista mares2 son: ', mares02)