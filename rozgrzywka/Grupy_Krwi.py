krew = ['ARh+', 'ARh-', 'BRh+', 'BRh-', 'ABRh+', 'ABRh-', '0Rh+', '0Rh-']
print(input("Grupy krwi to: ARh+, Arh-, BRh+, BRh-, ABRh+, ABRh-, 0Rh+, 0Rh-"))
dawca = input("Jaka grupe krwi ma dawca? ")
biorca = input("Jaka grupe krwi ma biorca? ")

def krew(dawca, biorca):
 

    if dawca == "ABRh+":
        if biorca == "ABRh+":
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "ABRh-":
        if ((biorca == "ABRh+") or (biorca == "ABRh-")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "BRh+":
        if((biorca == "ABRh+") or (biorca=="BRh+")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "BRh-":
        if((biorca == "ABRh+") or (biorca == "ABRh-") or (biorca == "BRh+") or (biorca == "BRh-")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "ARh+":
        if ((biorca == "ABRh+") or (biorca == "ARh+")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "ARh-":
        if ((biorca == "ABRh+") or (biorca == "ABRh-") or (biorca == "ARh+") or (biorca == "ARh-")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "0Rh+":
        if ((biorca == "ABRh+") or (biorca == "BRh+") or (biorca == "ARh+") or (biorca == "0Rh+")):
            print("Dawca i biorca sa kompatybilni")
        else:
            print("Dawca i biorca nie sa kompatybilni")
    elif dawca == "0Rh-":
        print("Dawca i biorca sa kompatybilni")
    else:
        print("Nie wpisano odpowiednich grup krwi")
        return
krew(dawca, biorca)