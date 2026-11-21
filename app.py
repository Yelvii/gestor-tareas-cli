
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
        print("Error: la tarea no puede estar vacia.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- LISTA DE TAREAS ---")

    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']} - {estado}")


if __name__ == "__main__":
    mostrar_menu()
