class MenuPrincipal:
    def __init__(self):
        self.personas = []
        self.universidades = []
        self.notas = []
        self.asignaturas = []

    def mostrar_menu_principal(self):
        print("MENU PRINCIPAL")
        print("1. PERSONAS")
        print("2. UNIVERSIDADES")
        print("3. NOTAS")
        print("4. ASIGNATURAS")
        print("5. SALIR")

    def mostrar_submenu_personas(self):
        print("\nSUBMENU PERSONAS")
        print("1. CREAR PERSONA")
        print("2. LISTAR PERSONAS")
        print("3. ELIMINAR PERSONA")
        print("4. ATRAS")

    def mostrar_submenu_universidades(self):
        print("\nSUBMENU UNIVERSIDADES")
        print("1. CREAR UNIVERSIDAD")
        print("2. LISTAR UNIVERSIDADES")
        print("3. ELIMINAR UNIVERSIDAD")
        print("4. ATRAS")

    def mostrar_submenu_notas(self):
        print("\nSUBMENU NOTAS")
        print("1. REGISTRAR NOTA")
        print("2. LISTAR NOTAS")
        print("3. ELIMINAR NOTA")
        print("4. ATRAS")

    def mostrar_submenu_asignaturas(self):
        print("\nSUBMENU ASIGNATURAS")
        print("1. AGREGAR ASIGNATURA")
        print("2. LISTAR ASIGNATURAS")
        print("3. ELIMINAR ASIGNATURA")
        print("4. ATRAS")

    # Métodos para operaciones con personas (crear, listar, eliminar)
    def crear_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        self.personas.append({"nombre": nombre, "edad": edad})
        print("Persona creada exitosamente.")

    def listar_personas(self):
        print("\nLISTADO DE PERSONAS")
        for persona in self.personas:
            print("Nombre:", persona["nombre"], "| Edad:", persona["edad"])

    def eliminar_persona(self):
        nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
        for persona in self.personas:
            if persona["nombre"] == nombre:
                self.personas.remove(persona)
                print("Persona eliminada exitosamente.")
                return
        print("No se encontró ninguna persona con ese nombre.")

    # Métodos para operaciones con universidades (crear, listar, eliminar)
    def crear_universidad(self):
        nombre = input("Ingrese el nombre de la universidad: ")
        ubicacion = input("Ingrese la ubicación de la universidad: ")
        self.universidades.append({"nombre": nombre, "ubicacion": ubicacion})
        print("Universidad creada exitosamente.")

    def listar_universidades(self):
        print("\nLISTADO DE UNIVERSIDADES")
        for universidad in self.universidades:
            print("Nombre:", universidad["nombre"], "| Ubicación:", universidad["ubicacion"])

    def eliminar_universidad(self):
        nombre = input("Ingrese el nombre de la universidad que desea eliminar: ")
        for universidad in self.universidades:
            if universidad["nombre"] == nombre:
                self.universidades.remove(universidad)
                print("Universidad eliminada exitosamente.")
                return
        print("No se encontró ninguna universidad con ese nombre.")

    # Métodos para operaciones con notas (registrar, listar, eliminar)
    def registrar_nota(self):
        estudiante = input("Ingrese el nombre del estudiante: ")
        asignatura = input("Ingrese el nombre de la asignatura: ")
        nota = float(input("Ingrese la nota del estudiante: "))
        self.notas.append({"estudiante": estudiante, "asignatura": asignatura, "nota": nota})
        print("Nota registrada exitosamente.")


    def listar_notas(self):
        print("\nLISTADO DE NOTAS")
        if self.notas:
            for i, nota in enumerate(self.notas, start=1):
                print(f"{i}. Estudiante: {nota['estudiante']} | Asignatura: {nota['asignatura']} | Nota: {nota['nota']}")
        else:
            print("No hay notas registradas.")

    def eliminar_nota(self):
        if self.notas:
            estudiante = input("Ingrese el nombre del estudiante cuya nota desea eliminar: ")
            asignatura = input("Ingrese el nombre de la asignatura: ")
            for nota in self.notas:
                if nota["estudiante"] == estudiante and nota["asignatura"] == asignatura:
                    self.notas.remove(nota)
                    print("Nota eliminada exitosamente.")
                    return
            print("No se encontró ninguna nota para ese estudiante y asignatura.")
        else:
            print("No hay notas registradas.")
        
    #Asignatura
            
    def agregar_asignatura(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        self.asignaturas.append(nombre)
        print("Asignatura agregada exitosamente.")

    def listar_asignaturas(self):
        print("\nLISTADO DE ASIGNATURAS")
        if self.asignaturas:
            for i, asignatura in enumerate(self.asignaturas, start=1):
                print(f"{i}. {asignatura}")
        else:
            print("No hay asignaturas registradas.")

    def eliminar_asignatura(self):
        if self.asignaturas:
            asignatura = input("Ingrese el nombre de la asignatura que desea eliminar: ")
            if asignatura in self.asignaturas:
                self.asignaturas.remove(asignatura)
                print("Asignatura eliminada exitosamente.")
            else:
                print("La asignatura especificada no está registrada.")
        else:
            print("No hay asignaturas registradas.")
            

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                while True:
                    self.mostrar_submenu_personas()
                    opcion_sub = input("Seleccione una opción: ")
                    if opcion_sub == "1":
                        self.crear_persona()
                    elif opcion_sub == "2":
                        self.listar_personas()
                    elif opcion_sub == "3":
                        self.eliminar_persona()
                    elif opcion_sub == "4":
                        break
                    else:
                        print("Opción inválida.")
            elif opcion == "2":
                while True:
                    self.mostrar_submenu_universidades()
                    opcion_sub = input("Seleccione una opción: ")
                    if opcion_sub == "1":
                        self.crear_universidad()
                    elif opcion_sub == "2":
                        self.listar_universidades()
                    elif opcion_sub == "3":
                        self.eliminar_universidad()
                    elif opcion_sub == "4":
                        break
                    else:
                        print("Opción inválida.")
            elif opcion == "3":
                while True:
                    self.mostrar_submenu_notas()
                    opcion_sub = input("Seleccione una opción: ")
                    if opcion_sub == "1":
                        self.registrar_nota()
                    elif opcion_sub == "2":
                        self.listar_notas()
                    elif opcion_sub == "3":
                        self.eliminar_nota()
                    elif opcion_sub == "4":
                        break
                    else:
                        print("Opción inválida.")
            elif opcion == "4":
                while True:
                    self.mostrar_submenu_asignaturas()
                    opcion_sub = input("Seleccione una opción: ")
                    if opcion_sub == "1":
                        self.agregar_asignatura()
                    elif opcion_sub == "2":
                        self.listar_asignaturas()
                    elif opcion_sub == "3":
                        self.eliminar_asignatura()
                    elif opcion_sub == "4":
                        break
                    else:
                        print("Opción inválida.")
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

# Ejecutar el programa
menu = MenuPrincipal()
menu.ejecutar()
