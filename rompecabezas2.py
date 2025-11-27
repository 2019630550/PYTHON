import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk
import random

def cargar_imagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    return ruta

def cortar_imagen(imagen, n):
    ancho, alto = imagen.size
    pieza_ancho = ancho // n
    pieza_alto = alto // n

    piezas = []
    for i in range(n):
        for j in range(n):
            caja = (j * pieza_ancho, i * pieza_alto,
                    (j+1) * pieza_ancho, (i+1) * pieza_alto)
            piezas.append(imagen.crop(caja))
    return piezas

def mezclar_tablero(n):
    arr = list(range(n*n))
    random.shuffle(arr)
    return [arr[i*n:(i+1)*n] for i in range(n)]

def dibujar_tablero():
    imagenes_refs.clear()
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(n):
        for j in range(n):
            idx = tablero[i][j]

            if idx == n*n - 1:  # espacio vacío
                btn = tk.Button(frame, width=80, height=80,
                                command=lambda r=i, c=j: mover(r, c))
            else:
                img_tk = ImageTk.PhotoImage(piezas[idx])
                imagenes_refs.append(img_tk)
                btn = tk.Button(frame, image=img_tk,
                                command=lambda r=i, c=j: mover(r, c))
            btn.grid(row=i, column=j)

def mover(i, j):
    global tablero

    # Encontrar la posición del espacio vacío
    for x in range(n):
        for y in range(n):
            if tablero[x][y] == n*n - 1:
                vacio = (x, y)

    x, y = vacio

    # Intercambiar la pieza tocada con el hueco
    tablero[x][y], tablero[i][j] = tablero[i][j], tablero[x][y]
    dibujar_tablero()


# -------------------------------
# Ventana
# -------------------------------
root = tk.Tk()
root.title("Rompecabezas con Imagen")

# Tamaño del rompecabezas
n = simpledialog.askinteger("Tamaño",
                            "¿De cuántas piezas por lado? (Ej: 3, 4, 5)",
                            minvalue=2, maxvalue=10)

# Elegir imagen
ruta = cargar_imagen()
imagen = Image.open(ruta)

# Cortar imagen
piezas = cortar_imagen(imagen, n)

# Mezclar piezas
tablero = mezclar_tablero(n)

# Frame del tablero
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

imagenes_refs = []  # Para evitar que Tk borre las imágenes

dibujar_tablero()

root.mainloop()
