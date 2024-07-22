class Nodo:
    def __init__(self, id, nombre_departamento, jefe_departamento, nodo_izquierdo=None, nodo_derecho=None):
        self.id = id
        self.nombre_departamento = nombre_departamento
        self.jefe_departamento = jefe_departamento
        self.nodo_izquierdo = nodo_izquierdo
        self.nodo_derecho = nodo_derecho

def crear_organigrama():
    raiz = Nodo(1, "CEO", "Ulises Gonzalez")

    nivel2_izquierdo = Nodo(2, "Marketing", "Erika Malave")
    nivel2_derecho = Nodo(3, "Ventas", "Raul Silva")

    raiz.nodo_izquierdo = nivel2_izquierdo
    raiz.nodo_derecho = nivel2_derecho

    nivel3_izquierdo_marketing = Nodo(4, "Redes Sociales", "Alicia Martínez")
    nivel3_derecho_marketing = Nodo(5, "Marketing de Contenidos", "Roberto López")

    nivel2_izquierdo.nodo_izquierdo = nivel3_izquierdo_marketing
    nivel2_izquierdo.nodo_derecho = nivel3_derecho_marketing

    nivel3_izquierdo_ventas = Nodo(6, "Equipo de Ventas 1", "Carlos Hernández")
    nivel3_derecho_ventas = Nodo(7, "Equipo de Ventas 2", "David Moreno")

    nivel2_derecho.nodo_izquierdo = nivel3_izquierdo_ventas
    nivel2_derecho.nodo_derecho = nivel3_derecho_ventas

    nivel4_izquierdo_ventas_1 = Nodo(8, "Ventas Corporativas", "Pablo Gómez")
    nivel4_derecho_ventas_1 = Nodo(9, "Ventas al Gobierno", "Sandra Martínez")

    nivel3_izquierdo_ventas.nodo_izquierdo = nivel4_izquierdo_ventas_1
    nivel3_izquierdo_ventas.nodo_derecho = nivel4_derecho_ventas_1

    nivel4_izquierdo_ventas_2 = Nodo(10, "Ventas Minoristas", "Carlos Jiménez")
    nivel4_derecho_ventas_2 = Nodo(11, "Ventas Online", "Patricia Rodríguez")

    nivel3_derecho_ventas.nodo_izquierdo = nivel4_izquierdo_ventas_2
    nivel3_derecho_ventas.nodo_derecho = nivel4_derecho_ventas_2

    return raiz

def mostrar_ramas(nodo):
    if nodo is None:
        return

    print(f"ID del nodo: {nodo.id}")
    print(f"Departamento: {nodo.nombre_departamento}")
    print(f"Jefe: {nodo.jefe_departamento}")

    mostrar_ramas(nodo.nodo_izquierdo)
    mostrar_ramas(nodo.nodo_derecho)

def mostrar_raiz(nodo):
    if nodo is None:
        return

    print(f"Nodo raíz:")
    print(f"ID del nodo: {nodo.id}")
    print(f"Departamento: {nodo.nombre_departamento}")
    print(f"Jefe: {nodo.jefe_departamento}")

def mostrar_ultimos_nodos(nodo):
    if nodo is None:
        return

    if nodo.nodo_izquierdo is None and nodo.nodo_derecho is None:
        print(f"Nodo final:")
        print(f"ID del nodo: {nodo.id}")
        print(f"Departamento: {nodo.nombre_departamento}")
        print(f"Jefe: {nodo.jefe_departamento}")

    mostrar_ultimos_nodos(nodo.nodo_izquierdo)
    mostrar_ultimos_nodos(nodo.nodo_derecho)

raiz_organigrama = crear_organigrama()

mostrar_ramas(raiz_organigrama)

mostrar_raiz(raiz_organigrama)

mostrar_ultimos_nodos(raiz_organigrama)