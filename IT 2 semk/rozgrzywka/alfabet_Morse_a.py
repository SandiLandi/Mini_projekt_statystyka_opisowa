LacinaNaMorse = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----'}
MorseNaLacina = {}
for values, keys in LacinaNaMorse.items():
    MorseNaLacina[keys] = values

def morse(string):
    out = ''
    for element in string:
        out = out + LacinaNaMorse[element] + ' '
    return out

def lacina(string):
    out = ''
    splitStrings = string.split(' ')
    for element in splitStrings:
        out = out + MorseNaLacina[element]
    return out
print(morse(input("Podaj tekst, ktory chcesz zaszyfrowac: ").upper()))
print(lacina(input("Podaj szyfr, ktory chcesz odszyfrowac: ")).lower())