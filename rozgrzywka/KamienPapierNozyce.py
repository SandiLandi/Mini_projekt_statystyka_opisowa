import random

gra = ["kamien", "papier", "nozyce"]
losowanie = random.choice(gra)
runda = 0
ty = 0
komputer = 0

while runda == 0:
    for runda in range (3):
        gracz = input("Wybierz kamien, papier lub nozyce: ")
        if gracz == losowanie:
            print("remis")
            ty +=1
            komputer +=1
        elif gracz == "kamien":
            if losowanie == "papier":
                print("Papier bije kamien. Przegrywasz")
                komputer +=1
            else:
                print("Kamien bije nozyce. Wygrywasz")
                ty +=1
        elif gracz == "papier":
            if losowanie == "kamien":
                print("Papier bije kamien. Wygrywasz")
                ty +=1
            else:
                print("Nozyce bija papier. Przegrywasz")
                komputer +=1
        elif gracz == "nozyce":
            if losowanie == "kamien":
                print("Kamien bije nozyce. Przegrywasz")
                komputer +=1
            else:
                print("Nozyce bija papier. Wygrywasz")
                ty +=1
if ty < komputer:
    print("Ty: ", ty)
    print("Komputer: ", komputer)
    print("wygrał komputer")
    
elif ty == komputer:
    print("Ty: ", ty)
    print("Komputer: ", komputer)
    print("Remis")
    
else:
    print("Ty: ", ty)
    print("Komputer: ", komputer)
    print("Wygrałes")