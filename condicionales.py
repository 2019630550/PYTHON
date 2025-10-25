edad = 25
tiene_bono = True
es_estudiante = True

if edad >= 18:
    print("Puede entrar")
elif es_estudiante and tiene_bono:
    print("Puede entrar con bono")
else:
    print("No puede entrar")