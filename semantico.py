import ply.yacc as yacc
import tkinter as tk

def create_parser(error_table, resust_table, tokens):
    global variableelse, operado1, numeroIF, valor, numberFun, typevar

    def p_init(p):
        '''init : forpara 
                    | opcion2 
                    | opcion3 
                    | opcion4 
                    | funcad'''

    def p_opcion2(p):
        '''opcion2 : VARIABLE CADENA ID ASSIG ID
                    | VARIABLE ENTERO ID ASSIG NUMB'''
        global variableelse, valorsi
        variableelse, valorsi = p[5], p[5]
        resust_table.insert(tk.END, f"Variable declarada '{p[3]}' con valor '{p[5]}'\n")


    def p_opcion3(p):
        '''opcion3 : opcion2 SI PAREL ID operando contentn PARER BRACL contentIF print BRACR SINO BRACL contentELSE print BRACR'''
        var = p[4]
        operador = operado1  # Usar operado1, que debería haber sido definido en p_operando

        print(f"Debug: num_variable = {valorsi}, num_numeroIF = {numeroIF}, operador = {operador}")

        funcion_condicional = {
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '=': lambda x, y: x == y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '!=': lambda x, y: x != y
        }.get(operador, lambda x, y: False)

        num_variable = int(valorsi)
        num_numeroIF = int(numeroIF)

        if funcion_condicional(num_variable, num_numeroIF):
            resust_table.insert(tk.END, f"Resultado si: {valor02}\n")
        else:
            resust_table.insert(tk.END, f"Resultado sino: {valor03}\n")

    def p_opcion4(p):
        '''opcion4 : FUNCION ID PAREL ENTERO ID PARER BRACL opcion2 var ID ASSIG ID MAS ID BRACR'''
        num_variable1 = int(variablef)
        num_numeroIF = int(variableelse)
        suma = num_variable1 + num_numeroIF if typevar == "entero" and p[12] == valor and p[14] == valor3 and valor != valor3 and p[5] == p[10] else None
        if suma:
            resust_table.insert(tk.END, f"resultado '{suma}'\n")
        else:
            error_table.insert(tk.END, f"Error, variables utilizadas no declaradas\n")

    def p_funcad(p):
        '''funcad : FUNCION ID PAREL CADENA ID PARER BRACL ID ASSIG ID BRACR'''
        if p[5] == p[8]:
            resust_table.insert(tk.END, f"La variable tiene el resultado '{p[10]}'\n")
        else:
            error_table.insert(tk.END, f"Error, variable no definida\n")

    def p_forpara(p):
        '''forpara : PARA PAREL value ID ASSIG NUMB PUNTOCOMA ID operando NUMB PUNTOCOMA ID INCR PUNTOCOMA PARER BRACL content print BRACR'''
        global user_value, user_value2, number2
        user_value, user_value2 = p[6], p[10]
        number2 = user_value2 - user_value
        for _ in range(number2):
            resust_table.insert(tk.END, f"resultado '{valor_varsi}'\n")

    def p_forvar(p):
        '''forvar : VARIABLE CADENA ID ASSIG ID
                    | VARIABLE ENTERO ID ASSIG NUMB'''
        global typevar,valor_varsi
        if isinstance(p[5], int) and p[2] == "entero":
           valor_varsi=p[5]
        elif isinstance(p[5], str) and p[2] == "cadena":
            valor_varsi=p[5]
        else:
            resust_table.insert(tk.END, f"sintaxis de variable mal '{p[3]}' con valor '{p[5]}'\n")
        variableelse, valor, typevar = p[5], p[3], p[2]


    def p_value(p):
        '''value : CADENA
                    | ENTERO'''
        global varfor
        varfor = p[1]
    
    def p_print(p):
        '''print : IMPRIMIR PAREL ID PARER'''

    def p_content(p):
        '''content : CONTENIDO
                     | ID
                     | forvar'''
        global valor01,valorop2
        valor01 = p[1]
        valorop2 =valor_varsi

    def p_contentIF(p):
        '''contentIF : CONTENIDO
                     | ID
                     | forvar'''
        global valor02,valorsi
        valor02 = p[1]
        valorsi=valor_varsi

    def p_contentELSE(p):
        '''contentELSE : CONTENIDO
                     | ID
                     | forvar'''
        global valor03,valorelse
        valor03 = p[1]
        valorelse =valor_varsi

    def p_operando(p):
        '''operando : MAY
                    | MAYIG
                    | MENIG
                    | IGIG
                    | MENO
                    | DIFER
                    | ASSIG'''
        global operado1
        operado1 = p[1]

    def p_contentn(p):
        '''contentn : ID  
                 | NUMB'''  
        global numeroIF
        numeroIF = p[1]

    def p_var(p):
        '''var : VARIABLE ENTERO ID ASSIG NUMB'''
        global variablef, valor3
        variablef, valor3 = p[5], p[3]
        resust_table.insert(tk.END, f"Variable declarada '{valor3}' con valor '{variablef}'\n")

    def p_error(p):
        error = f"Syntax error in token '{p.value}'" if p else "Syntax error at EOF"
        error_table.insert(tk.END, error + "\n")

    parser = yacc.yacc()
    return parser

