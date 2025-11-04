import tkinter as tk

#Crear la ventana principal
ventana = tk.Tk()

#Título de la ventana
ventana.title("Mi Aplicación")

#Tamaño de la ventana
ventana.geometry("400x300")

#Etiqueta de bienvenida
etiqueta = tk.Label(ventana, text="¡Bienvenido a mi aplicación!")
etiqueta.pack(pady=20)

#Botón para cerrar la aplicación
boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
boton.pack()

#Bucle principal de la ventana
ventana.mainloop()