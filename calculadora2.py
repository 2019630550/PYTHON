#Pedimos al usuario que ingrese dos numeros
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

#Mostramos las opciones 
print("Elige la opcion que deseas realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

#Pedimos la opcion al usuario
opcion = input("Ingresa el numero de la opcion): ")

#Ejecutamos segun la opcion
if opcion == '1':
    print("Resultado: ", numero1 + numero2)
elif opcion == '2':
    print("Resultado: ", numero1 - numero2)
elif opcion == '3':
    print("Resultado: ", numero1 * numero2)
elif opcion == '4':
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("Resultado: ", numero1 / numero2)
else:
    print("Opcion no valida")