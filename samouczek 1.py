import math

print("Ten program liczy pola i obwody figur:")
print("1 - prostokąt")
print("2 - trapez")
print("3 - koło")
print("4 - kwadrat")

wybor = input("Twój wybór (1/2/3/4): ")

try:
     wybor = int(wybor)
except ValueError:
     print("Nieprawidłowy wybór. Wpisz liczbę odpowiadającą wybranej figurze.")
     exit()
     
if wybor == 1:
    bok_a = input("Podaj długośc boku a prostokąta:")
    bok_b = input("Podaj długopść boku b prostokąta:")
    try:
        bok_a = float(bok_a)
        bok_b = float(bok_b)
    except ValueError:
        print("Nieprawidłowa wartość. Wpisz liczbę.")
        exit()

    pole = round(bok_a * bok_b, 3)
    obwod = round(2 * (bok_a + bok_b), 3)
    print("Pole prostokata wynosi:", pole)
    print("Obwód prostokąta wynosi:", obwod)
                        
elif wybor == 2:
    podstawa_a = input("Podaj długość pierwszej podstawy trapezu: ")
    podstawa_b = input("Podaj długość drugiej podstawy trapezu: ")
    bok_c =input("Podaj długość lewego boku trapezu: ")
    bok_d =input("Podaj długość prawego boku trapezu: ")
    wysokość = input("Podaj wysokość trapezu: ")
    try:
        podstawa_a = float(podstawa_a)
        podstawa_b = float(podstawa_b)
        bok_c = float(bok_c)
        bok_d = float(bok_d)
        wysokość = float(wysokość)
    except ValueError:
        print("Nieprawidłowa wartość. Wpisz liczbę.")
        exit()

    pole = round(((podstawa_a + podstawa_b) * wysokość) / 2, 3)
    obwod = round(podstawa_a + podstawa_b + bok_c + bok_d, 3)
    print("Pole trapezu wynosi:", pole)
    print("Obwód trapezu wynosi:", obwod) 
        


elif wybor == 3:
    promien = float(input("Podaj promień koła:"))
    pole = round(math.pi * promien ** 2, 3)
    obwod = round(2 * math.pi * promien, 3)
    print("Pole koła wynosi:", pole)
    print("Obwód koła wynosi:", obwod)




elif wybor == 4:
    bok = float(input("Podaj długość boku kwadratu:"))
    pole = round(bok ** 2, 3)
    obwod = round(4 * bok, 3)
    print("Pole kwadratu wynosi:", pole)
    print("Obwód kwadratu wynosi:", obwod)


else:
    print("Błędny wybór. Spróbuj ponownie.")

