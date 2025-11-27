import tkinter as tk
from tkinter import simpledialog
import random

def crear_tablero(n):
    nums = list(range(1, n*n))
    nums.append("")  # Espacio vacío
    random.shuffle(nums)
    return [nums[i*n:(i+1)*n] for i in range(n)]

def dibujar_tablero():
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(n):
        for j in range(n):
            valor = tablero[i][j]
            btn = tk.Button(frame, text=valor, width=6, height=3,
                            command=lambda r=i, c=j: mover(r, c))
            btn.grid(row=i, column=j, padx=3, pady=3)

def mover(i, j):
    global tablero

    # Buscar espacio vacío alrededor
    posiciones = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for x, y in posiciones:
        if 0 <= x < n and 0 <= y < n:
            if tablero[x][y] == "":
                tablero[x][y], tablero[i][j] = tablero[i][j], ""
                dibujar_tablero()
                return

# ---- Ventana principal ----
root = tk.Tk()
root.title("Rompecabezas Deslizante")

# Pedir tamaño al usuario
n = simpledialog.askinteger("Tamaño", "¿De cuántas piezas por lado? (Ej: 3, 4, 5)", minvalue=2, maxvalue=10)

tablero = crear_tablero(n)

frame = tk.Frame(root)
frame.pack(pady=20)

dibujar_tablero()

root.mainloop()
