import tkinter as tk
from tkinter import ttk
import analizador

def check_code():
    # Limpia las tablas de tokens y errores antes de una nueva ejecución
    token_table.delete(*token_table.get_children())
    error_table.delete(*error_table.get_children())

    code = code_text.get("1.0", tk.END).strip()
    if not code:
        result_label.config(text="No hay código para verificar.")
        return  

    # Realiza el análisis y obtiene los errores y tokens
    errores, tokens = analizador.analizar(code)  
    
    if not errores:
        error_table.insert('', 'end', values=("La sintaxis es correcta.",))
        for token_type, token_value in tokens:
            token_table.insert('', 'end', values=(token_type, token_value))

    else:
        # Muestra los errores en la interfaz gráfica
        for error in errores:
            error_table.insert('', 'end', values=(error,))

        # Muestra los tokens en la interfaz gráfica
        for token_type, token_value in tokens:
            token_table.insert('', 'end', values=(token_type, token_value))

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")
root.geometry("800x900")

# Configuración del área de texto para ingresar código
code_text = tk.Text(root, wrap=tk.WORD)
code_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Botón para iniciar el análisis
btn = tk.Button(root, text="Analizar", command=check_code)
btn.pack(padx=10, pady=(0, 10), anchor=tk.E)

# Configuración del área para mostrar los tokens identificados
token_frame = ttk.LabelFrame(root, text="Tokens")
token_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 10), pady=(0, 10))

token_table = ttk.Treeview(token_frame, columns=('Type', 'Value'), show='headings')
token_table.heading('Type', text='Token')
token_table.heading('Value', text='Valor')
token_table.pack(fill=tk.BOTH, expand=True)

# Configuración del área para mostrar los errores sintácticos
error_frame = ttk.LabelFrame(root, text="Mensajes de Sintaxis")
error_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=(5, 10), pady=10)

error_table = ttk.Treeview(error_frame, columns=('Error',), show='headings')
error_table.heading('Error', text='Mensajes')
error_table.pack(fill=tk.BOTH, expand=True)

# Etiqueta para mostrar el resultado del análisis
result_label = tk.Label(error_frame, text="", fg="Blue")
result_label.pack(fill=tk.X, padx=10, pady=(0, 10))

root.mainloop()
