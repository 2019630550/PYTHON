import tkinter as tk
from tkinter import ttk

def cifrado_cesaar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nueva_pos = (ord(char) - base + desplazamiento) % 26
            resultado += chr(base + nueva_pos)
        else:
            resultado += char
    return resultado
    
def cifrar():
    texto = entrada_texto.get()
    k = int(entrada_k.get())
    salida.delete(0, tk.END)
    salida.insert(0, cifrado_cesaar(texto, k))
    
def descifrar():
    texto = entrada_texto.get()
    k = int(entrada_k.get())
    salida.delete(0, tk.END)
    salida.insert(0, cifrado_cesaar(texto, -k))
    
#--- Ventana ---
ventana = tk.Tk()
ventana.title("Cifrado Cesar")
ventana.geometry("400x250")
ventana.resizable(False, False)

#--- Widgets ---
tk.Label(ventana, text="Texto:").pack(pady=5)
entrada_texto = ttk.Entry(ventana, width=40)
entrada_texto.pack()

ttk.Label(ventana, text="Desplazamiento (n):").pack(pady=5)
entrada_k = ttk.Entry(ventana, width=10)
entrada_k.insert(0, "3")
entrada_k.pack()

ttk.Label(ventana, text="Resultado:").pack(pady=5)
salida = ttk.Entry(ventana, width=40)
salida.pack()

frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)

btn_cifrar = ttk.Button(frame_botones, text="Cifrar", command=cifrar)
btn_cifrar.grid(row=0, column=0, padx=10)


btn_decifrar = ttk.Button(frame_botones, text="Decifrar", command=descifrar)
btn_cifrar.grid(row=0, column=1, padx=10)

#Ejecutar ventana
ventana.mainloop()