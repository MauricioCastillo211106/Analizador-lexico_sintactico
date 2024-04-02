# import tkinter as tk
# from tkinter import ttk, messagebox
import ply.lex as lex
import ply.yacc as yacc
from analizador_semantico import tabla_simbolos


tokens = [
    'ID',
    'N',
    'AS',
    'CM',
    'PA',
    'PC',
    'LA',
    'LC',
    'PT',
    'OP',   
    'IN'
]


reserved = {
    'variable':'AG',
    'entero': 'TP',
    'cadena': 'TP',
    'funcion': 'VQ',
    'para': 'PQ',
    'si': 'VS',
    'sino': 'NS',
    'principal': 'SO',
    'imprimir' : 'IM'
}

tokens += list(reserved.values())

errores = []

t_PA = r'\('
t_PC = r'\)'
t_LA = r'\{'
t_LC = r'\}'
t_CM = r'"'
t_PT = r';'
t_AS = r'='
t_OP = r'(>=|<=|==|!=|>|<)'
t_IN = r'\++'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_N(t):
    r'\d+'
    t.value = int(t.value)
    return t



t_ignore = ' \t\n'

def t_error(t):
    mensaje_error = f"Carácter desconocido'{t.value[0]}'"
    errores.append(mensaje_error)
    t.lexer.skip(1)

lexer = lex.lex()

def p_S(p):
    '''S : V
            | F
            | CL
            | IF
            | M'''

def p_V(p):
    '''V : AG TP ID VL'''
    tipo = p[2]
    identificador = p[3]
    try:
        tabla_simbolos.agregar(identificador, tipo)
    except Exception as e:
        errores.append(str(e))

# Esto maneja la asignación de valores a variables
def p_VL(p):
    '''VL : AS valor'''
    # Aquí, `valor` es una nueva regla que necesitas definir basada en lo que tu lenguaje soporta (números, cadenas, etc.)

def p_valor(p):
    '''valor : N
             | cadena
             | ID'''
    p[0] = p[1]

def p_cadena(p):
    '''cadena : CM ID CM'''
    p[0] = p[2]  # Aquí asumimos que quieres capturar el texto entre comillas como un valor de cadena

# Asume que estás declarando una variable y posiblemente asignando un valor inicial
def p_declaracion_con_asignacion(p):
    '''V : AG TP ID AS valor'''
    tipo = p[2]
    identificador = p[3]
    valor = p[5]
    try:
        tabla_simbolos.agregar(identificador, tipo, valor)  # Asegúrate de que el método agregar ahora maneje un valor
    except Exception as e:
        errores.append(str(e))

def p_asignacion(p):
    '''VL : ID AS valor'''
    identificador = p[1]
    valor = p[3]  # Asumiendo que `valor` ya ha sido evaluado a un valor concreto (número, cadena, etc.)
    print(f"Valor de '{identificador}' actualizado a: {valor}")
    if identificador in tabla_simbolos.simbolos:
        # Actualiza el valor de la variable en la tabla de símbolos
        tabla_simbolos.simbolos[identificador]['valor'] = valor
        print(f"Valor de '{identificador}' actualizado a: {valor}")
    else:
        errores.append(f"Error: Variable '{identificador}' no declarada.")



def p_F(p):
    '''F : VQ ID PA P PC LA V C LC'''
    func_name = p[2]
    try:
        # Aquí asumimos que tienes una forma de registrar funciones en tu tabla de símbolos
        tabla_simbolos.agregar_funcion(func_name)
    except Exception as e:
        errores.append(str(e))

def p_IF(p):
    '''IF : VS PA CD PC LA V C LC NS LA C LC'''
    # Este ejemplo es simplificado; en la práctica, querrías analizar la condición CD
    try:
        cond_var = p[3]  # Asumiendo que p[3] sea una variable/condición
        if cond_var not in tabla_simbolos:
            raise Exception(f"Variable '{cond_var}' utilizada en condición no declarada.")
    except Exception as e:
        errores.append(str(e))

def p_CD(p):
    '''CD : ID OP ON'''
    # Verificar que ID esté declarado y sea del tipo esperado para la operación OP con ON
    var_name = p[1]
    operacion = p[2]
    operando = p[3]  # Podría ser un identificador o un literal
    try:
        if var_name not in tabla_simbolos:
            raise Exception(f"Variable '{var_name}' no declarada.")
        # Aquí se añadirían más verificaciones específicas según la operación y el tipo de operando
    except Exception as e:
        errores.append(str(e))

   

def p_P(p):
    '''P : TP ID'''
    
def p_CL(p):
    '''CL : PQ PA V PT ID OP ON PT ID IN PT PC LA V C LC'''
                     
def p_ON(p):
    '''ON : ID
            | N'''
    
def p_SO(p):
    '''M : VQ SO PA PC LA V C LC'''

def p_C(p):
    '''C : IM PA ID PC'''
    identificador = p[3]  # El identificador de la variable
    if identificador in tabla_simbolos.simbolos:
        # Imprime el valor de la variable
        print(tabla_simbolos.simbolos[identificador]['valor'])
    else:
        errores.append(f"Error: Variable '{identificador}' no declarada.")



def p_error(p):
    if p:
        errores.append(f"Error de sintaxis en '{p.value}'")
    else:
        errores.append("Error de sintaxis al final de la entrada")

parser = yacc.yacc()

def analizar(texto):
    # limpiar la lista de errores antes de cada análisis
    errores.clear()
    lexer.input(texto)
    tokens = []
    for token in lexer:
        tokens.append((token.type, token.value))
    parser.parse(texto)
    # Retorna la lista de errores para que pueda ser usada por la interfaz gráfica
    return errores, tokens