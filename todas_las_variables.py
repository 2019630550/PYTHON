variables = {
    "edad": 25,
    "nombre": "Brenda Daniela",
    "estatura": 1.67,
    "peso": 70,
    "estudiante": True
}

for nombre_var, valor in variables.items():
    print(f"{nombre_var}: {valor} (tipo: {type(valor)})")