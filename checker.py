from lexico import create_lexer
from semantico import create_parser
import tkinter as tk

def check_code(interface, txt, token_table, resust_table, error_table):
    lexer, tokens = create_lexer(error_table) 
    parser = create_parser(error_table, resust_table, tokens)
    # Obtén el texto del código
    code = txt.get("1.0", tk.END)
    
    # Usa el lexer y el parser para analizar el código
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_table.insert(tk.END, f"{tok.type}: {tok.value}\n")
    parser.parse(code)
