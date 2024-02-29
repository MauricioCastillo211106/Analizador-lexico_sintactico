# import tkinter as tk
# from tkinter import ttk, messagebox
import ply.lex as lex
import ply.yacc as yacc

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
    'contenido': 'C',
    'funcion': 'VQ',
    'para': 'PQ',
    'si': 'VS',
    'sino': 'NS',
    'principal': 'SO'
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

# def p_empty(p):
#     'empty :'
#     pass

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
                            
def p_VL(p):
    '''VL : AS N
            | AS CM ID CM
            | '''
               
def p_F(p):
    '''F : VQ ID PA P PC LA C LC'''
 
def p_P(p):
    '''P : TP ID'''
    
def p_CL(p):
    '''CL : PQ PA V PT ID OP ON PT ID IN PT PC LA C LC'''
                     
def p_IF(p):
    '''IF : VS PA CD PC LA C LC NS LA C LC'''
          
def p_CD(p):
    '''CD : ID OP ON'''
    
def p_ON(p):
    '''ON : ID
            | N'''
    
def p_SO(p):
    '''M : VQ SO PA PC LA C LC'''
            
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