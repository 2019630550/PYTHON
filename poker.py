#Definir el orden de las cartas
orden = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
         "7": 7, "8": 8, "9": 9, "10": 10,
         "J": 11, "Q": 12, "K": 13, "A": 14}

def bubble_sort_cartas(cartas):
    n = len(cartas)
    for i in range(n):
        for j in range (n - i - 1):
            if orden[cartas[j]] > orden[cartas[j + 1]]:
                cartas[j], cartas[j + 1] = cartas[j + 1], cartas[j]

#ejemplo
mazo = ["K", "3", "A", "10", "7", "J", "2"]
bubble_sort_cartas(mazo)
print(mazo)