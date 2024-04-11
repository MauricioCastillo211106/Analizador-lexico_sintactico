import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import inspector  # Asegúrate de que este módulo esté implementado correctamente

# Inicialización de la ventana principal
root = tk.Tk()
root.title("Analizador Léxico, Sintáctico y Semántico")

# Configuración del tamaño de la ventana
root.geometry("800x600")

# Función para realizar el análisis y actualizar las áreas de texto
def analizador():
    try:
        content = text_code.get("1.0", tk.END)
        tokens, errors = inspector.look_code(content, text_code, text_tokens, text_syntax, text_errors)

        if tokens:
            text_tokens.insert(tk.END, tokens)

        # Si hay errores, los insertamos en la tabla de errores.
        if errors:
            text_errors.insert(tk.END, errors)
        if text_syntax:
            text_syntax.insert(tk.END,text_syntax)
        # Además, insertamos el resultado en la tabla de resultados, si no hay errores.
        if tokens and not errors:
            text_syntax.insert(tk.END, "Análisis completado con éxito.\n")
            messagebox.showinfo("Análisis Completo", "El análisis se ha completado exitosamente.")
        else:
            text_syntax.insert(tk.END, "Errores detectados durante el análisis.\n")
            messagebox.showerror("Error de Análisis", "No se pudo completar el análisis correctamente debido a errores.")

        # Si deseas imprimir algún resultado adicional o manejo específico de errores, puedes agregarlo aquí.
    except Exception as e:
        print(" ")
# Área de texto para la entrada de código
label_code = tk.Label(root, text="Código Fuente")
label_code.pack()
text_code = scrolledtext.ScrolledText(root, height=10)
text_code.pack(fill=tk.BOTH, expand=True)

# Área de texto para mostrar los tokens
label_tokens = tk.Label(root, text="Tokens")
label_tokens.pack()
text_tokens = scrolledtext.ScrolledText(root, height=10)
text_tokens.pack(fill=tk.BOTH, expand=True)

# Área de texto para mostrar los resultados del análisis sintáctico
label_syntax = tk.Label(root, text="Resultado Sintáctico")
label_syntax.pack()
text_syntax = scrolledtext.ScrolledText(root, height=10)
text_syntax.pack(fill=tk.BOTH, expand=True)

# Área de texto para mostrar los errores
label_errors = tk.Label(root, text="Errores")
label_errors.pack()
text_errors = scrolledtext.ScrolledText(root, height=10)
text_errors.pack(fill=tk.BOTH, expand=True)

# Botón para iniciar el análisis
button_analyze = tk.Button(root, text="Analizar", command=analizador)
button_analyze.pack()

# Carga el código inicial en el área de entrada
text_code.insert(tk.END, '''funcion imprimir ( cadena prim ) {
prim=Hola
 }
''')

# Ejecución del bucle principal
root.mainloop()
