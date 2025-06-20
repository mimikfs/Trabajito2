import os

Archivo = "estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []
    if os.path.exists(Archivo):  # corregido: was 'exits'
        with open(Archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes

def guardar_estudiantes(estudiantes):
    with open(Archivo, "w", encoding='utf-8') as archivo:
        for est in estudiantes:
            linea = f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)

def crear_estudiantes(estudiantes):
    codigo = input("Código del estudiante: ")
    if any(est["codigo"] == codigo for est in estudiantes):
        print("El código ya existe.\n")
        return
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiantes(estudiantes)
    print("Estudiante agregado correctamente.\n")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
        
    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(f"{est['codigo']} - {est['nombre']} {est['apellido']} - {est['carrera']}")
    print()

def actualizar_estudiantes(estudiantes):
    codigo = input("Ingresa el código del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            est["nombre"] = input(f"Nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
            est["apellido"] = input(f"Nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
            est["carrera"] = input(f"Nueva carrera (actual: {est['carrera']}): ") or est["carrera"]
            guardar_estudiantes(estudiantes)
            print("Estudiante actualizado.\n")
            return
    print("No se encontró estudiante con ese código.\n")

def eliminar_estudiante(estudiantes):
    codigo = input("Ingresa el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado.\n")
            return
    print("No se encontró un estudiante con ese código.\n")

def menu():
    estudiantes = cargar_estudiantes()  # corregido: se estaba pasando como función sin ()
    while True:
        print("====== MENÚ CRUD ESTUDIANTES ======")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            crear_estudiantes(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiantes(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.\n")

menu()
