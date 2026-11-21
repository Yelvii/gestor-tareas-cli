
# Gestor de Tareas CLI

tareas = []


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def agregar_tarea():
    descripcion = input("Ingrese la nueva tarea: ").strip()

    if descripcion:
        tareas.append({
            "descripcion": descripcion,
            "completada": False
        })
        print("Tarea agregada correctamente.")
    else:
        print("Error: la tarea no puede estar vacía.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")

    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']} - {estado}")


def completar_tarea():
    listar_tareas()

    if not tareas:
        return

    try:
        numero = int(input("Número de tarea a completar: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea completada correctamente.")
        else:
            print("Número de tarea inválido.")

    except ValueError:
        print("Debes ingresar un número válido.")


def eliminar_tarea():
    listar_tareas()

    if not tareas:
        return

    try:
        numero = int(input("Número de tarea a eliminar: "))

        if 1 <= numero <= len(tareas):
            eliminada = tareas.pop(numero - 1)
            print(f"Tarea eliminada: {eliminada['descripcion']}")
        else:
            print("Número de tarea inválido.")

    except ValueError:
        print("Debes ingresar un número válido.")


def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Gracias por utilizar el gestor de tareas.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
