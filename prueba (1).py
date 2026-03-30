from main import save_clients
print("MENUUUUUUU")
print("1. registrar usuario")
print("2. listar usuario")
print("3. buscar usuario")
print("4. actualizar usuario")
print("5. eliminar usuario")
print("6. salir")



def registrar_usuario():

  try:
    
    id=input("digite id")
    nombre=input("digite nombre")
    edad=input("digite edad")
    membresia=input("digite membresia semanal/mensual/anual")
    estado=input("digite estado activo/inactivo")
    

    estadoBoo=True
    if(estado=="activo"):
     estadoBoo=True
    else:
     estadoBoo=False


    diccionario={
        "id":id,
        "nombre":nombre,
        "edad":edad,
        "membresia":membresia,
        "estado":estadoBoo
    }

    save_clients(diccionario)


  except ValueError:
    print("ocurrio un error")  
    
    print(f"se registro el usuario {diccionario}")

    return diccionario    

def listar_usuario():
   diccionario={
        "id":"id",
        "nombre":"nombre",
        "edad":"edad",
        "membresia":"membresia",
        "estado":"estadoBoo"
    }
   print("los usuarios son",diccionario)

def buscar_usuario():
  
  diccionario={"id":"123",
        "nombre":"juan",
        "edad":"23",
        "membresia":"mensual",
        "estado":True}

  idbuscar=input("digite el id del usuario a buscar") 
  usuario={}

  for clave , valor in diccionario.items():
     if(idbuscar==valor["id"]):
      usuario=valor 


  print(f"los datos del usuario son {usuario}")     

       



   

opcion=int(input("digita una opcion"))


if(opcion==1):
    registrar_usuario()
elif(opcion==2):
   listar_usuario()    
elif(opcion==3):
  buscar_usuario()

    










