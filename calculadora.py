#Pedimos los numeros 
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

#Operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

#division con verificacion de cero
if numero2 == 0:
    print("No se puede dividir entre 0")
else:
    division = numero1 / numero2
    print("La division es: ", division)

#Mostramos los resultados de las otras operaciones
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multiplicacion)