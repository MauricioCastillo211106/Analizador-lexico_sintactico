import tkinter as tk
import ply.lex as lex

def reserved_words():
    return {
        'entero': 'ENTERO',
        'para': 'PARA',
        'variable': 'VARIABLE',
        'cadena': 'CADENA',
        'si': 'SI',
        'sino': 'SINO',
        'funcion': 'FUNCION',
        'siono': 'SIONO',
        'contenido': 'CONTENIDO'
    }

def token_definitions():
    return [
        'DOUBLESTRING', 'ID', 'ENTERO', 'PAREL', 'ID', 'ASSIG', 'NUMB', 'SEMI',
        'MAY', 'INCR', 'PARER', 'BRACL', 'BRACR', 'STRING', 'MENOS', 'MAS',
        'MULTI', 'DIV', 'MAYIG', 'MENIG', 'IGIG', 'PUNTOCOMA', 'MENO', 'DIFER', 'COMILLA'
    ] + list(reserved_words().values())

def create_lexer(error_table):
    tokens = token_definitions()

    t_DOUBLESTRING = r'"[^"]*"'
    t_PAREL = r'\('
    t_ASSIG = r'='
    t_MAY = r'>'
    t_INCR = r'\+\+'
    t_PARER = r'\)'
    t_BRACL = r'{'
    t_BRACR = r'}'
    t_MAS = r'\+'
    t_MENOS = r'-'
    t_MULTI = r'\*'
    t_DIV = r'\\'
    t_MAYIG = r'>='
    t_MENIG = r'<='
    t_IGIG = r'=='
    t_PUNTOCOMA = r';'
    t_MENO = r'<'
    t_DIFER = r'!='
    t_COMILLA = r'"'    

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved_words().get(t.value, 'ID')
        return t

    def t_NUMB(t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ignore = ' \t\n'

    def t_error(t):
        error_table.insert(tk.END, f"Illegal character '{t.value[0]}'\n")
        t.lexer.skip(1)

    lexer = lex.lex()

    return lexer, tokens
