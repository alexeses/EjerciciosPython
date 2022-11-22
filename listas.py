mares01 = ["Mediterraneo", "Cantabrico", "Báltico", "Ártico", "Índico", "Pacífico", "Atlántico", "Antártico"]
mares02 = ["Rojo", "Muerto", "Caspio", "Negro", "Aral", "Morto", "Sargasso", "Mariano"]
mares00 = mares01 + mares02

print('La logintud total de la lista es: ', len(mares01))
print(mares01)
print('La logintud total de la lista es: ', len(mares02))
print(mares02)
print('La logintud total de la lista es: ', len(mares00))
print(mares00)

print('Los elementos  1, 2 y 3 de la lista son: ', mares01[0:3])
print('El elemento egeo está en la posición: ', mares01.index('Ártico'))

print('Los elementos 5, 6 y 7 de la lista son: ', mares02[4:7])
print('El elemento Caspßio está en la posición: ', mares02.index('Caspio'))
print('El ßelemento Caspio está la posición: ', mares00.index('Caspio'))