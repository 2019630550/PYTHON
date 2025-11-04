import tkinter as tk
from tkinter import messagebox

def karatsuba_visual(x, y, text_widget):
    text_widget.insert(tk.END, f"Multiplicando {x} x {y}\n")

    if x < 10 or y < 10:
        text_widget.insert(tk.END, f"Resultado directo: {x * y}\n\n")
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    text_widget.insert(tk.END, f"Dividiendo: a={a}, b={b}, c={c}, d={d}\n")

    ac = karatsuba_visual(a, c, text_widget)
    bd = karatsuba_visual(b, d, text_widget)
    ab_cd = karatsuba_visual(a + b, c + d, text_widget) - ac - bd

    res = ac * 10**(2*m) + ab_cd * 10**m + bd
    text_widget.insert(tk.END, f"Resultado parcial: {res}\n\n")
    return res

def calcular():
    try:
        x = int(entry1.get())
        y = int(entry2.get())
        resultado = karatsuba_visual(x, y, text)
        messagebox.showinfo("Resultado final", f"{x} x {y} = {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números enteros.")

ventana = tk.Tk()
ventana.title("Visualizador de Karatsuba")

tk.Label(ventana, text="Número 1:").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Número 2:").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack(pady=10)


text = tk.Text(ventana, height=20, width=50)
text.pack()

ventana.mainloop()