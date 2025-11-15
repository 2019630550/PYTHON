import tkinter as tk
from tkinter import filedialog, messagebox

def nuevo_archivo():
    text_area.delete(1.0, tk.END)

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        text_area.delete(1.0, tk.END)
        with open(archivo, "r") as f:
            text_area.insert(1.0, f.read())

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Guardar", "Archivo guardado exitosamente.")

#Ventana principal
root = tk.Tk()
root.title("Notepad en Python")
root.geometry("700x500")

#Área de texto
text_area = tk.Text(root, wrap='word', font=("Arial", 12))
text_area.pack(expand=True, fill='both')

#Barra de menú
menu_bar = tk.Menu(root)

#Menú Archivo
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=menu_bar)
root.mainloop()