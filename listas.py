#lista
mi_lista = ["María", "Pepe", "Marta", "Antonio"]

#imprimir la lista 
print(mi_lista[:])

#imprimir un elemento en concreto
print(mi_lista[2])

#imprimir dentro de un rango 
print(mi_lista[0:2])
print(mi_lista[:2])
print(mi_lista[2:])

#para agregar un elemento a la lista 
mi_lista.append("José")
print(mi_lista[:])

#para agregar un elemento en cierta posición
mi_lista.insert(2,"Alex")
print(mi_lista[:])

#para agregar varios elementos a la lista 
mi_lista.extend(["Gabriela","Mariela"])
print(mi_lista[:])

#para el índice de un elemento en una lista 
print(mi_lista.index("Alex"))

#para comprobar si un elemento se encuentra en la lista 
print("José" in mi_lista)

#para eliminar un elemento en una lista 
mi_lista.remove("José")
print(mi_lista[:])

#para eliminar un  ultimo elemento
mi_lista.pop()
print(mi_lista[:])

#para concatenar dos  listas 
mi_lista2=["Sonia","Pepe"]
mi_lista3= mi_lista + mi_lista2
print(mi_lista3)

#para repetir un cierto número de veces una lista
mi_lista = ["María", "Pepe", "Marta", "Antonio"]*3
print(mi_lista[:])