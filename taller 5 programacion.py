class SistemaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, descripcion):
        self.tareas.append({"descripcion": descripcion, "completada": False})
        print(f"Tarea '{descripcion}' agregada correctamente.")
    
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        
        print("\nLista de tareas:")
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{i}. [{estado}] {tarea['descripcion']}")
    
    def completar_tarea(self, numero_tarea):
        try:
            tarea = self.tareas[numero_tarea - 1]
            tarea["completada"] = True
            print(f"Tarea '{tarea['descripcion']}' marcada como completada.")
        except IndexError:
            print("Número de tarea inválido.")
    
    def eliminar_tarea(self, numero_tarea):
        try:
            tarea = self.tareas.pop(numero_tarea - 1)
            print(f"Tarea '{tarea['descripcion']}' eliminada correctamente.")
        except IndexError:
            print("Número de tarea inválido.")

def main():
    sistema = SistemaTareas()
    
    print("\nBienvenido al Sistema de Gestión de Tareas")
    print("----------------------------------------")
    
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            sistema.agregar_tarea(descripcion)
        elif opcion == "2":
            sistema.mostrar_tareas()
        elif opcion == "3":
            numero = int(input("Ingrese el número de la tarea a completar: "))
            sistema.completar_tarea(numero)
        elif opcion == "4":
            numero = int(input("Ingrese el número de la tarea a eliminar: "))
            sistema.eliminar_tarea(numero)
        elif opcion == "5":
            print("Gracias por usar el Sistema de Gestión de Tareas. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()



    
