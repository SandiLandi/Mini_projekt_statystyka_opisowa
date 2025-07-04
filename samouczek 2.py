import random
import statistics
import numpy as np 

wygenerowana_lista = [random.randint(1,100) for i in range(100)] # generacja tablicy 100 losowych liczb 
print("wygenerowana lista:", wygenerowana_lista) 

średnia = sum(wygenerowana_lista)/len(wygenerowana_lista) # średnia 


lab = sorted(wygenerowana_lista) # mediana
n = len(lab)
if n % 2 == 0:
    mediana = (lab[n//2 - 1] + lab[n//2]) / 2
else:
    mediana = lab[n//2]

najmniejsza_liczba = min(wygenerowana_lista)   # najmniejsza i największa liczby 
najwieksza_liczba = max(wygenerowana_lista)


for i in range(1, len(wygenerowana_lista)):   # sortowanie 
    tab = wygenerowana_lista[i]
    j = i - 1
    while j >= 0 and wygenerowana_lista[j] > tab:
        wygenerowana_lista[j+1] = wygenerowana_lista[j]
        j -= 1
    wygenerowana_lista[j+1] = tab     
    
odchylenie = statistics.stdev(wygenerowana_lista)  # odchylenie  

one = 50
two = 10    
wygenerowana_lista_norm = np.random.normal(one, two, 100)    
    
    
         
print("Średnia:", średnia)  # wyniki
print("Mediana:", mediana)
print("Min:", najmniejsza_liczba)
print("Max:", najwieksza_liczba)    
print("posortowana lista:" , wygenerowana_lista)   
print("Odchylenie standardowe:", odchylenie)          
print("Rozkład normalny:", wygenerowana_lista_norm)

