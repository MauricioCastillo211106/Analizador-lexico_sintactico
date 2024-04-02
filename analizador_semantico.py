class TablaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.funciones = {}  # Nuevo diccionario para funciones

# Ajuste en la clase TablaDeSimbolos en analizador_semantico.py

    def agregar(self, nombre, tipo, valor=None):
        if nombre in self.simbolos:
            raise Exception(f"Error semántico: '{nombre}' ya declarado.")
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}


    def agregar_funcion(self, nombre, tipo_retorno=None, parametros=None):
        if nombre in self.funciones:
            raise Exception(f"Error semántico: Función '{nombre}' ya declarada.")
        self.funciones[nombre] = {'tipo_retorno': tipo_retorno, 'parametros': parametros}

    def verificar_declaracion(self, nombre):
        if nombre not in self.simbolos and nombre not in self.funciones:
            raise Exception(f"Error semántico: '{nombre}' no declarado.")

    def obtener_tipo(self, nombre):
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        elif nombre in self.funciones:
            return self.funciones[nombre]['tipo_retorno']
        else:
            return None
    
    def actualizar_valor(self, nombre, valor):
        if nombre in self.simbolos:
            self.simbolos[nombre]['valor'] = valor
            print(self.simbolos)
        else:
            raise Exception(f"Error semántico: Variable '{nombre}' no declarada.")


# Instancia global de la tabla de símbolos
tabla_simbolos = TablaDeSimbolos()

def verificar_asignacion(nombre, valor, linea):
    """
    Verifica la compatibilidad de tipos en una asignación y otros chequeos necesarios.
    """
    tipo = tabla_simbolos.obtener_tipo(nombre)
    if tipo is None:
        raise Exception(f"Error semántico en línea {linea}: Variable '{nombre}' no declarada.")
    # Aquí agregarías más lógica para verificar la asignación dependiendo del tipo y valor.
