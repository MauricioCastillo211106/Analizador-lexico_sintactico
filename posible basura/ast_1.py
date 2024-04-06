class NodoAST(object):
    pass

class DeclaracionVariable(NodoAST):
    def __init__(self, tipo, identificador):
        self.tipo = tipo
        self.identificador = identificador

class AsignacionVariable(NodoAST):
    def __init__(self, identificador, valor):
        self.identificador = identificador
        self.valor = valor
