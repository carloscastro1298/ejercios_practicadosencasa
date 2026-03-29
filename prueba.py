#Creacion de diccionario
#Creacion de diccionario
#diccionario es una estructura de datos que almacena pares de clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
#que mas saber de los diccionarios?
#Los diccionarios se pueden crear utilizando llaves {} y separando las claves y valores con dos puntos (:). Por ejemplo:
#mi_diccionario = {"clave1": valor1, "clave2": valor2, ...}
#Los valores en un diccionario pueden ser de cualquier tipo de datos, incluyendo números, cadenas, listas, otros diccionarios, etc. Por ejemplo:
#mi_diccionario = {"nombre": "Juan", "edad": 30, "hobbies": ["futbol", "lectura"], "direccion": {"calle": "123 Main St", "ciudad": "Ciudad"}}
#Para acceder a los valores en un diccionario, se utiliza la clave correspondiente. Por ejemplo:
#nombre = mi_diccionario["nombre"]  # Esto devolverá "Juan"

estudiantes={
    "nombre": "Pedro",
    "edad": 16,
    "grado": "9no",
    "materias": ["Matematicas", "Ciencias", "Historia"]

}

#Mostrar diccionario
print("diccionario completo: ")
print(estudiantes)

#Mostrar solo el nombre
print("Nombre del estudiante: ")
print(estudiantes["nombre"])

#Agregar nueva informacion
estudiantes["ciudad"] = "Medellin"

#Cambiar edad
estudiantes["edad"]= 17

#Eliminar una materia
estudiantes["materias"].remove("Matematicas")

#Final
print("diccionario actualizado:")
print(estudiantes)
