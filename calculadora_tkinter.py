import tkinter as tk
import math

# --- Variables globales ---
modo_grados = True  # True = grados, False = radianes

# --- Funciones trigonométricas según modo ---
def sin_m(x):
    return math.sin(math.radians(x)) if modo_grados else math.sin(x)

def cos_m(x):
    return math.cos(math.radians(x)) if modo_grados else math.cos(x)

def tan_m(x):
    return math.tan(math.radians(x)) if modo_grados else math.tan(x)

# --- Funciones de la calculadora ---
def click(boton):
    actual = entrada.get()
    if boton == "π":
        boton = str(math.pi)
    elif boton == "e":
        boton = str(math.e)
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, actual + str(boton))

def borrar():
    entrada.delete(0, tk.END)

def retroceso():
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, actual[:-1])

def alternar_modo():
    global modo_grados
    modo_grados = not modo_grados
    modo_btn.config(text="GRADOS" if modo_grados else "RADIANES")

def calcular():
    try:
        expr = entrada.get().replace("^", "**").replace("√", "math.sqrt").replace("log", "math.log10")
        contexto = {
            "sin": sin_m,
            "cos": cos_m,
            "tan": tan_m,
            "sqrt": math.sqrt,
            "log": math.log10,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "pow": pow
        }
        resultado = eval(expr, {"__builtins__": None}, contexto)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(round(resultado, 10)))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("500x600")
ventana.configure(bg="#1e1e1e")

for i in range(8):
    ventana.rowconfigure(i, weight=1)
for i in range(6):
    ventana.columnconfigure(i, weight=1)

entrada = tk.Entry(ventana, font=("Consolas", 24), borderwidth=5, relief="sunken",
                   justify="right", bg="#333", fg="white", insertbackground="white")
entrada.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)

# --- Botones ---
botones = [
    ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("log", 1, 3), ("√", 1, 4), ("^", 1, 5),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("π", 2, 4), ("(", 2, 5),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("e", 3, 4), (")", 3, 5),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("C", 4, 4), ("⌫", 4, 5),
    ("0", 5, 0), (".", 5, 1), ("+", 5, 2), ("=", 5, 3, 3)
]

for boton in botones:
    texto = boton[0]
    fila = boton[1]
    columna = boton[2]
    colspan = boton[3] if len(boton) == 4 else 1

    if texto == "=":
        color = "#4CAF50"
        comando = calcular
    elif texto == "C":
        color = "#f44336"
        comando = borrar
    elif texto == "⌫":
        color = "#FF9800"
        comando = retroceso
    else:
        color = "#555"
        comando = lambda t=texto: click(t)

    tk.Button(ventana, text=texto, bg=color, fg="white", font=("Arial", 16, "bold"),
              relief="raised", borderwidth=3, command=comando
             ).grid(row=fila, column=columna, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# --- Botón GRADOS/RADIANES ---
modo_btn = tk.Button(ventana, text="GRADOS", bg="#2196F3", fg="white", font=("Arial", 14, "bold"),
                     command=alternar_modo)
modo_btn.grid(row=6, column=0, columnspan=6, sticky="nsew", padx=5, pady=5)

ventana.mainloop()
