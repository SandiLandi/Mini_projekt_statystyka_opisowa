def palindrom(a):
    a = input("Czy dane slowo jest palindromem?: ")
    return (a == a[::-1])
print(palindrom(""))
