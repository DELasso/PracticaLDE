class Nodo:
    def __init__(self, estudiante):
        self.data = estudiante  # El dato es un diccionario con los datos del estudiante
        self.next = None  # Referencia al siguiente nodo
        self.prev = None  # Referencia al nodo anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.head = None  # La cabeza (primer nodo)
        self.tail = None  # La cola (último nodo)
        self.total_aprobados = 0
        self.total_reprobados = 0
        self.suma_notas = 0
        self.total_estudiantes = 0
        self.codigo_actual = 0  # Contador de códigos automáticos

    # Método para agregar un estudiante (aprobados al inicio, reprobados al final)
    def agregar_estudiante(self, nombre, apellidos, correo, nota):
        # Asignación automática del código
        codigo = self.codigo_actual
        self.codigo_actual += 1

        estudiante = {
            "codigo": codigo,
            "nombre": nombre,
            "apellidos": apellidos,
            "correo": correo,
            "nota": nota
        }

        nuevo_nodo = Nodo(estudiante)
        self.suma_notas += nota
        self.total_estudiantes += 1

        # Si el estudiante aprobó (nota >= 3.0), lo insertamos al inicio
        if nota >= 3.0:
            self.total_aprobados += 1
            if self.head is None:  # Si la lista está vacía
                self.head = nuevo_nodo
                self.tail = nuevo_nodo
            else:
                nuevo_nodo.next = self.head
                self.head.prev = nuevo_nodo
                self.head = nuevo_nodo
        else:
            self.total_reprobados += 1
            # Si la lista está vacía
            if self.head is None:
                self.head = nuevo_nodo
                self.tail = nuevo_nodo
            else:
                self.tail.next = nuevo_nodo
                nuevo_nodo.prev = self.tail
                self.tail = nuevo_nodo

    # Método para buscar un estudiante por código
    def buscar_estudiante(self, codigo):
        actual = self.head
        while actual:
            if actual.data["codigo"] == codigo:
                return actual.data
            else:
                actual = actual.next
        return None

    # Método para eliminar un estudiante por código
    def eliminar_estudiante(self, codigo):
        if self.head is None:  # Si la lista está vacía
            print("La lista está vacía.")
            return

        actual = self.head
        while actual is not None and actual.data["codigo"] != codigo:
            actual = actual.next

        if actual is None:  # Si no se encuentra el estudiante
            print("Estudiante no encontrado.")
            return

        # Actualizar contadores y suma de notas
        self.suma_notas -= actual.data["nota"]
        self.total_estudiantes -= 1
        if actual.data["nota"] >= 3.0:
            self.total_aprobados -= 1
        else:
            self.total_reprobados -= 1

        # Si es el único nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Si el nodo a eliminar es la cabeza
        elif actual == self.head:
            self.head = actual.next
            if self.head:
                self.head.prev = None
        # Si el nodo a eliminar es la cola
        elif actual == self.tail:
            self.tail = actual.prev
            if self.tail:
                self.tail.next = None
        # Si el nodo está en el medio
        else:
            actual.prev.next = actual.next
            if actual.next:
                actual.next.prev = actual.prev

        print(f"Estudiante con código {codigo} eliminado.")

    # Método para contar estudiantes aprobados
    def total_aprobados(self):
        return self.total_aprobados

    # Método para contar estudiantes reprobados
    def total_reprobados(self):
        return self.total_reprobados

    # Método para calcular la nota promedio
    def nota_promedio(self):
        if self.total_estudiantes == 0:
            return 0
        return self.suma_notas / self.total_estudiantes

    # Método para imprimir la lista de estudiantes desde la cabeza
    def imprimir_desde_la_cabeza(self):
        actual = self.head
        if actual is None:
            print("La lista está vacía.")
            return

        print("Lista de estudiantes desde la cabeza:")
        while actual is not None:
            estudiante = actual.data
            print(f"{estudiante['codigo']}: {estudiante['nombre']} "
                  f"{estudiante['apellidos']} - Correo: {estudiante['correo']} - Nota: {estudiante['nota']}")
            actual = actual.next
        print()

    # Método para imprimir la lista de estudiantes desde la cola
    def imprimir_desde_la_cola(self):
        actual = self.tail
        if actual is None:
            print("La lista está vacía.")
            return

        print("Lista de estudiantes desde la cola:")
        while actual is not None:
            estudiante = actual.data
            print(f"{estudiante['codigo']}: {estudiante['nombre']} "
                  f"{estudiante['apellidos']} - Correo: {estudiante['correo']} - Nota: {estudiante['nota']}")
            actual = actual.prev
        print()

# Ejemplo de menú
def menu():
    lista_estudiantes = ListaDobleEnlazada()

    while True:
        print("\n-------- MENÚ DE ESTUDIANTES --------")
        print("a) Agregar un estudiante")
        print("-------------------------------------")
        print("b) Buscar un estudiante por código")
        print("-------------------------------------")
        print("c) Eliminar un estudiante")
        print("-------------------------------------")
        print("d) Total de estudiantes aprobados")
        print("-------------------------------------")
        print("e) Total de estudiantes reprobados")
        print("-------------------------------------")
        print("f) Nota promedio")
        print("-------------------------------------")
        print("g) Imprimir desde la cabeza")
        print("-------------------------------------")
        print("h) Imprimir desde la cola")
        print("-------------------------------------")
        print("i) Salir")
        print("-------------------------------------")

        opcion = input("Selecciona una opción: ").lower()

        if opcion == 'a':
            while True:
                nombre = input("Nombre: ").strip()
                if all(letra.isalpha() or letra.isspace() for letra in nombre) and len(nombre) > 0:
                    break
                else:
                    print("Error: El nombre solo debe contener letras y no puede ser un espacio en blanco.")

            while True:
                apellidos = input("Apellidos: ").strip()
                if all(letra.isalpha() or letra.isspace() for letra in apellidos) and len(apellidos) > 0:
                    break
                else:
                    print("Error: Los apellidos solo deben contener letras y espacios, y no pueden estar vacíos.")

            while True:
                correo = input("Correo: ").lower()
                if "@" in correo and correo.endswith(".com"):
                    break
                else:
                    print("Error: El correo debe contener '@' y terminar en '.com'. Inténtalo de nuevo.")

            while True:
                nota = input("Nota (0 a 5): ")
                if nota.replace('.', '', 1).isdigit() and nota.count('.') < 2:
                    nota = float(nota)
                    if 0 <= nota <= 5:
                        break
                    else:
                        print("Error: La nota debe estar en el rango de 0 a 5. Inténtalo de nuevo.")
                else:
                    print("Error: La nota debe ser un número válido. Inténtalo de nuevo.")

            lista_estudiantes.agregar_estudiante(nombre, apellidos, correo, nota)
            print("Estudiante agregado correctamente.")

        elif opcion == 'b':
            while True:
                codigo_input = input("Código del estudiante a buscar: ")
                if codigo_input.isdigit():
                    codigo = int(codigo_input)
                    break
                else:
                    print("Error: El código debe ser un número entero. Inténtalo de nuevo.")

            estudiante = lista_estudiantes.buscar_estudiante(codigo)
            if estudiante:
                print(
                    f"Estudiante encontrado con código: {estudiante['codigo']} - {estudiante['nombre']} {estudiante['apellidos']}"
                    f" - Correo: {estudiante['correo']}, Nota: {estudiante['nota']}")
            else:
                print(f"Estudiante con código: {codigo} no encontrado.")

        elif opcion == 'c':
            while True:
                codigo_input = input("Código del estudiante a eliminar: ")
                if codigo_input.isdigit():
                    codigo = int(codigo_input)
                    break
                else:
                    print("Error: El código debe ser un número entero. Inténtalo de nuevo.")

            lista_estudiantes.eliminar_estudiante(codigo)

        elif opcion == 'd':
            print(f"Total de estudiantes aprobados: {lista_estudiantes.total_aprobados}")

        elif opcion == 'e':
            print(f"Total de estudiantes reprobados: {lista_estudiantes.total_reprobados}")

        elif opcion == 'f':
            print(f"Nota promedio de los estudiantes: {lista_estudiantes.nota_promedio()}")

        elif opcion == 'g':
            lista_estudiantes.imprimir_desde_la_cabeza()

        elif opcion == 'h':
            lista_estudiantes.imprimir_desde_la_cola()

        elif opcion == 'i':
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
