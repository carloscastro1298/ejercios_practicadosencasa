#.append() se utiliza para agregar un elemento al final de una lista
#.remove() se utiliza para eliminar la primera aparición de un elemento específico de una lista.
#.pop() se utiliza para eliminar un elemento de una lista o un diccionario y devolver su valor. En una lista, se puede especificar el índice del elemento a eliminar, mientras que en un diccionario, se puede especificar la clave del elemento a eliminar.
#si quiero saber la posicion de un elemento en una lista, puedo usar el metodo .index() que devuelve el indice de la primera aparicion del elemento especificado en la lista. Si el elemento no se encuentra en la lista, se genera un error ValueError.
#listas y diccionarios son estructuras de datos fundamentales en Python que permiten almacenar y organizar información de manera eficiente. Las listas son ordenadas y mutables, lo que significa que se pueden modificar después de su creación, mientras que los diccionarios almacenan pares de clave-valor y también son mutables. 
#Ambas estructuras ofrecen una variedad de métodos para manipular los datos, como agregar, eliminar o acceder a elementos específicos.
#tuplas?#Las tuplas son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de su creación. Se definen utilizando paréntesis () en lugar de corchetes []. Las tuplas son útiles para almacenar datos que no deben cambiar, como coordenadas geográficas o fechas. 
#Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos de datos y se pueden acceder a sus elementos mediante índices.
frutas=["manzana","mango","pera","naranja","uva"]
frutas=["manzana","mango","pera","naranja","uva"]

print("lista de frutas")

print(frutas)

print("primera fruta")
print(frutas[0])

frutas.append("banano")
print("listado actualizado")
print(frutas)

frutas.remove("uva")
print("listado actualizado")
print(frutas)
