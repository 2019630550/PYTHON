import tkinter as tk
import calendar
from datetime import date

root = tk.Tk()
root.title("Calendario 2026")
root.configure(bg="#ffd8e8")

# ======= CONFIGURACIÓN DE COLORES =======
color_fondo = "#ffd8e8"
color_marco = "#ff9fcf"
color_header = "#ff9fcf"
color_festivo = "#ff2f92"   # rosa fuerte para festivos
color_normal = "black"

# ======= FUENTES =======
font_header = ("Arial", 14, "italic")
font_dayname = ("Courier New", 10, "bold")
font_daynum = ("Courier New", 11)

# ======= FESTIVOS OFICIALES 2026 (México) =======
festivos = {
    date(2026, 1, 1),   # Año Nuevo
    date(2026, 2, 5),   # Constitución
    date(2026, 3, 16),  # Natalicio Benito Juárez (puente)
    date(2026, 5, 1),   # Día del Trabajo
    date(2026, 9, 16),  # Independencia
    date(2026, 11, 16), # Revolución (puente)
    date(2026, 12, 25)  # Navidad
}

cal = calendar.Calendar(firstweekday=6)  # domingo = 6
year = 2026

row = 0
col = 0

for month in range(1, 13):
    # Marco del mes
    frame = tk.Frame(root, bg=color_marco, bd=3, relief="ridge")
    frame.grid(row=row, column=col, padx=10, pady=10)

    # Encabezado del mes
    nombre = calendar.month_name[month].upper()
    header = tk.Label(frame, text=nombre, bg=color_header, fg="white",
                      font=font_header)
    header.pack(fill="x")

    # Contenedor interno
    inner = tk.Frame(frame, bg="white", padx=8, pady=8)
    inner.pack()

    # Nombres de días
    dias = ["D", "L", "M", "M", "J", "V", "S"]
    for i, d in enumerate(dias):
        tk.Label(inner, text=d, font=font_dayname,
                 bg="white", fg="black").grid(row=0, column=i)

    # Días del mes
    r = 1
    for week in cal.monthdayscalendar(year, month):
        for c, day in enumerate(week):
            if day == 0:
                # Celda vacía
                tk.Label(inner, text=" ", bg="white").grid(row=r, column=c)
            else:
                fecha = date(year, month, day)

                # Si es festivo → rosa fuerte
                color = color_festivo if fecha in festivos else color_normal

                tk.Label(inner,
                         text=f"{day:2}",
                         font=font_daynum,
                         fg=color,
                         bg="white").grid(row=r, column=c)
        r += 1

    # Ajustar cuadrícula
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
