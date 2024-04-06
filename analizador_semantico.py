class TablaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.funciones = {}  # Nuevo diccionario para funciones

# Ajuste en la clase TablaDeSimbolos en analizador_semantico.py

    def agregar(self, nombre, tipo, valor=None):
        if nombre in self.simbolos:
            raise Exception(f"Error semántico: '{nombre}' ya declarado.")
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}
        print(f"Variable '{nombre}' agregada correctamente. Tipo: {tipo}, Valor: {valor}")
        
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

def verificar_tipo_compatibilidad(tipo_variable, valor):
    """
    Verifica si el valor es compatible con el tipo de la variable.
    """
    if tipo_variable == "entero":
        return isinstance(valor, int)
    elif tipo_variable == "cadena":
        return isinstance(valor, str)
    # Aquí puedes agregar más tipos según sea necesario.
    else:
        return False

def verificar_asignacion(nombre, valor, linea):
    """
    Verifica la compatibilidad de tipos en una asignación y otros chequeos necesarios.
    """
    tipo_variable = tabla_simbolos.obtener_tipo(nombre)['tipo']  # Asegúrate de obtener solo el tipo de la variable.
    if tipo_variable is None:
        raise Exception(f"Error semántico en línea {linea}: Variable '{nombre}' no declarada.")
    
    # Si `valor` es un identificador de otra variable, obtén su valor real y tipo.
    if isinstance(valor, str) and valor in tabla_simbolos.simbolos:
        valor = tabla_simbolos.simbolos[valor]['valor']
        tipo_valor = tabla_simbolos.obtener_tipo(valor)['tipo']
    else:
        tipo_valor = "entero" if isinstance(valor, int) else "cadena" if isinstance(valor, str) else None
    
    # Verificar la compatibilidad de tipo.
    if not verificar_tipo_compatibilidad(tipo_variable, valor):
        raise Exception(f"Error semántico en línea {linea}: Incompatibilidad de tipos entre '{nombre}' y el valor asignado.")