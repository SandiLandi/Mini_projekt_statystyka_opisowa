from random import randint

zgadniecie = 0
liczba = randint(1,100)

zgadniecie = int(input("Zgadnij liczbe miedzy 1 a 100: "))
while zgadniecie != liczba:
    if zgadniecie > liczba:
        print("Za duzo")
        zgadniecie = int(input(" Zgadnij ponownie: "))
        zgadniecie +=1
    elif zgadniecie < liczba:
        print("Za malo")
        zgadniecie +=1
        zgadniecie = int(input(" Zgadnij ponownie: "))

print("Dobrze!")
print("Zgadywales", zgadniecie, " razy")