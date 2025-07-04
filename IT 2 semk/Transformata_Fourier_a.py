import numpy as np
import matplotlib.pyplot as plt


def moj_sinus(dzien, miesiac):
    N = 2**12
    fs = 10e3
    czas = np.arange(0, N/fs, 1.0/fs)

    amplituda = miesiac
    czestotliwosc = dzien

    sin = amplituda * np.sin(2 * np.pi * czestotliwosc * czas)
    plt.plot(czas, sin)
    plt.title(f"Amplituda: {amplituda}, Częstotliwość: {czestotliwosc}")
    plt.xlabel("Czas")
    plt.ylabel("Amplituda")
    plt.show()
    
    return sin

test1 = moj_sinus(8, 7)
test2 = moj_sinus(1, 12)
test3 = moj_sinus(12, 9)
test4 = test2 + test3

transformata1 = np.fft.rfft(test1)
transformata2 = np.fft.rfft(test2)
transformata3 = np.fft.rfft(test3)
transformata4 = np.fft.rfft(test4)

norm1 = 2*np.abs(transformata1)/len(test1)
print(norm1)
norm2 = 2*np.abs(transformata2)/len(test2)
norm3 = 2*np.abs(transformata3)/len(test3)
norm4 = 2*np.abs(transformata4)/len(test4)

f1 = np.linspace(0, 5000, len(norm1))
plt.plot(f1, norm1)
plt.title("Transformaty sygnału 1")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.show()

f2 = np.linspace(0, 5000, len(norm2))
plt.plot(f2, norm2)
plt.title("Transformaty sygnału 2")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.show()

f3 = np.linspace(0, 5000, len(norm3))
plt.plot(f3, norm3)
plt.title("Transformaty sygnału 3")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.show()

f4 = np.linspace(0, 5000, len(norm4))
plt.plot(f4, norm4)
plt.title("Transformaty sygnału 4")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.show()