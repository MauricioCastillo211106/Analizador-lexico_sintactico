import tkinter as tk
from tkinter import messagebox
import checker
root = tk.Tk()
root.title("Lexical, Syntactic, and Semantic Analyzer")
codigo = '''funcion imprimir ( cadena prim ) {
prim=Hola
 }
'''
txt = tk.Text(root, width=55, height=10)
txt.pack()
txt.insert(tk.END, codigo)
btn = tk.Button(root, text="Analyze", command=lambda: checker.check_code(root, txt, token_table, resust_table, error_table))
btn.pack()
token_table = tk.Text(root, height=10, width=40)
token_table.pack(padx=10, pady=5)
resust_table = tk.Text(root, height=10, width=50)
resust_table.pack(padx=10, pady=5)
error_table = tk.Text(root, height=10, width=40)
error_table.pack(padx=10, pady=5)
root.mainloop()