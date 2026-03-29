#Creacion de diccionario
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