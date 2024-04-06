from ast import NodoAST, DeclaracionVariable, AsignacionVariable

entorno = {}  # Diccionario global para almacenar variables y sus valores

def ejecutar_ast(nodo):
    if isinstance(nodo, DeclaracionVariable):
        # Asumiendo que las declaraciones solo registran la variable sin asignar un valor inicial
        entorno[nodo.identificador] = None
    elif isinstance(nodo, AsignacionVariable):
        if nodo.identificador in entorno:
            entorno[nodo.identificador] = nodo.valor
        else:
            raise Exception(f"Variable '{nodo.identificador}' no declarada.")
    # Continuar aquí con otros tipos de nodos