import json  # Importa el módulo para trabajar con archivos JSON
import os    # Importa el módulo para interactuar con el sistema operativo

# ==========================================================
# CONFIGURACIÓN DEL ARCHIVO
# ==========================================================

FILE_PATH = "datos/usuarios.json"  # Ruta del archivo donde se almacenan los clientes


# ==========================================================
# FUNCIONES DE PERSISTENCIA
# ==========================================================

def load_clients():  # Carga la lista de clientes desde el archivo JSON
    """
    Load clients from the JSON file.

    If the file does not exist, return an empty list.
    """
    if not os.path.exists(FILE_PATH):  # Si el archivo no existe, retorna una lista vacía
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:  # Abre el archivo en modo lectura
        return json.load(file)  # Carga y retorna la lista de clientes


def save_clients(clients):
    """
    Save the full client list into the JSON file.
    """
    with open(FILE_PATH, "w", encoding="utf-8") as file:  # Abre el archivo en modo escritura
        json.dump(clients, file, ensure_ascii=False, indent=4)  # Guarda la lista de clientes en formato JSON


# ==========================================================
# FUNCIONES DE NEGOCIO
# ==========================================================

def show_menu():
    """
    Display the main menu.
    """
    print("\n===== GYM CLIENT MANAGEMENT SYSTEM =====")  # Título del menú
    print("1. Register client")   # Opción para registrar cliente
    print("2. List clients")      # Opción para listar clientes
    print("3. Search client")     # Opción para buscar cliente
    print("4. Update client")     # Opción para actualizar cliente
    print("5. Delete client")     # Opción para eliminar cliente
    print("6. Exit")              # Opción para salir


def find_client_by_id(clients, client_id):
    """
    Search for a client by ID.

    Returns:
        dict: client if found
        None: if not found
    """
    for client in clients:  # Recorre la lista de clientes
        if client["id"] == client_id:  # Si el ID coincide
            return client  # Retorna el cliente encontrado
    return None  # Si no encuentra, retorna None


def register_client(clients):
    """
    Register a new client.

    Validates that:
    - ID is unique
    - age is numeric
    - status is active or inactive
    """
    print("\n--- Register Client ---")  # Encabezado

    client_id = input("Enter client ID: ").strip()  # Pide el ID
    if client_id == "":  # Valida que no esté vacío
        print("ID cannot be empty.")
        return

    existing_client = find_client_by_id(clients, client_id)  # Busca si ya existe ese ID
    if existing_client is not None:
        print("A client with that ID already exists.")
        return

    name = input("Enter client name: ").strip()  # Pide el nombre
    if name == "":  # Valida que no esté vacío
        print("Name cannot be empty.")
        return

    age_text = input("Enter client age: ").strip()  # Pide la edad
    if not age_text.isdigit():  # Valida que sea número
        print("Age must be a number.")
        return
    age = int(age_text)  # Convierte a entero

    plan = input("Enter plan (monthly / quarterly / yearly): ").strip().lower()  # Pide el plan
    if plan not in ("monthly", "quarterly", "yearly"):  # Valida el plan
        print("Invalid plan.")
        return

    status = input("Enter status (active / inactive): ").strip().lower()  # Pide el estado
    if status not in ("active", "inactive"):  # Valida el estado
        print("Invalid status.")
        return

    new_client = {  # Crea el diccionario del nuevo cliente
        "id": client_id,
        "name": name,
        "age": age,
        "plan": plan,
        "status": status
    }

    clients.append(new_client)  # Agrega el cliente a la lista
    save_clients(clients)       # Guarda la lista actualizada

    print("Client registered successfully.")  # Mensaje de éxito


def list_clients(clients):
    """
    Print all registered clients.
    """
    print("\n--- Client List ---")  # Encabezado

    if len(clients) == 0:  # Si no hay clientes
        print("No clients registered.")
        return

    for client in clients:  # Recorre y muestra cada cliente
        print(f"ID: {client['id']}")
        print(f"Name: {client['name']}")
        print(f"Age: {client['age']}")
        print(f"Plan: {client['plan']}")
        print(f"Status: {client['status']}")
        print("-" * 30)


def search_client(clients):
    """
    Search client by ID or by name.
    """
    print("\n--- Search Client ---")  # Encabezado
    print("1. Search by ID")      # Opción buscar por ID
    print("2. Search by name")    # Opción buscar por nombre

    option = input("Choose an option: ").strip()  # Pide opción

    if option == "1":  # Si busca por ID
        client_id = input("Enter client ID: ").strip()
        client = find_client_by_id(clients, client_id)

        if client is None:
            print("Client not found.")  # No encontrado
        else:
            print("\nClient found:")
            print(client)  # Muestra el cliente

    elif option == "2":  # Si busca por nombre
        name = input("Enter client name: ").strip().lower()
        found = False

        for client in clients:
            if client["name"].lower() == name:
                print(client)
                found = True

        if not found:
            print("Client not found.")

    else:
        print("Invalid option.")  # Opción inválida


def update_client(clients):
    """
    Update an existing client by ID.
    """
    print("\n--- Update Client ---")  # Encabezado

    client_id = input("Enter client ID to update: ").strip()  # Pide el ID
    client = find_client_by_id(clients, client_id)  # Busca el cliente

    if client is None:
        print("Client not found.")  # No encontrado
        return

    print("Leave blank if you do not want to change a field.")  # Instrucción

    new_name = input(f"New name ({client['name']}): ").strip()  # Nuevo nombre
    new_age = input(f"New age ({client['age']}): ").strip()      # Nueva edad
    new_plan = input(f"New plan ({client['plan']}): ").strip().lower()  # Nuevo plan
    new_status = input(f"New status ({client['status']}): ").strip().lower()  # Nuevo estado

    if new_name != "":  # Si se ingresó nuevo nombre
        client["name"] = new_name

    if new_age != "":  # Si se ingresó nueva edad
        if new_age.isdigit():
            client["age"] = int(new_age)
        else:
            print("Invalid age. Age was not updated.")

    if new_plan != "":  # Si se ingresó nuevo plan
        if new_plan in ("monthly", "quarterly", "yearly"):
            client["plan"] = new_plan
        else:
            print("Invalid plan. Plan was not updated.")

    if new_status != "":  # Si se ingresó nuevo estado
        if new_status in ("active", "inactive"):
            client["status"] = new_status
        else:
            print("Invalid status. Status was not updated.")

    save_clients(clients)  # Guarda los cambios
    print("Client updated successfully.")  # Mensaje de éxito


def delete_client(clients):
    """
    Delete a client by ID.
    """
    print("\n--- Delete Client ---")  # Encabezado

    client_id = input("Enter client ID to delete: ").strip()  # Pide el ID
    client = find_client_by_id(clients, client_id)  # Busca el cliente

    if client is None:
        print("Client not found.")  # No encontrado
        return

    clients.remove(client)  # Elimina el cliente de la lista
    save_clients(clients)   # Guarda la lista actualizada

    print("Client deleted successfully.")  # Mensaje de éxito


# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def main():
    """
    Main program function.
    """
    clients = load_clients()  # Carga la lista de clientes desde el archivo
    option = ""  # Variable para la opción del menú

    while option != "6":  # Bucle principal hasta que elija salir
        show_menu()  # Muestra el menú
        option = input("Choose an option: ").strip()  # Pide opción

        if option == "1":
            register_client(clients)  # Registrar cliente
        elif option == "2":
            list_clients(clients)     # Listar clientes
        elif option == "3":
            search_client(clients)    # Buscar cliente
        elif option == "4":
            update_client(clients)    # Actualizar cliente
        elif option == "5":
            delete_client(clients)    # Eliminar cliente
        elif option == "6":
            print("Goodbye.")         # Salir
        else:
            print("Invalid option. Please try again.")  # Opción inválida


if __name__ == "__main__":  # Si el archivo se ejecuta directamente
    main()  # Llama a la función principal