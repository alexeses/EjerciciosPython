mares01 = ["Mediterraneo", "Cantabrico", "Báltico", "Ártico", "Índico", "Pacífico", "Atlántico", "Antártico"]
mares02 = ["Rojo", "Muerto", "Caspio", "Negro", "Aral", "Morto", "Sargasso", "Mariano"]
mares00 = mares01 + mares02

mares00[11] = "del Norte"
mares00[12] = "alboran"

print(mares00)

# 2. En la lista mares, inserta un elemento más con el valor 'báltico'. Muestra la lista mares

mares00.append("báltico")
print(mares00)

# 3. Borra el quinto elemento de la lista mares. Muestra la lista mares
mares00.pop(4)
print(mares00)

# 4. Muestra la longitud de la lista mares
print(len(mares00))

# 5. Muestra los valores repetidos en la lista mares usando el método correspondiente
#create set and see if it is shorter than the original list
mares00_set = set(mares00)
if len(mares00_set) < len(mares00):
    print("There are duplicates in the list")
else:
    print("There are no duplicates in the list")