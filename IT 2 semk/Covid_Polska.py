import pandas as pd
import matplotlib.pyplot as plt

dataTimeseries = pd.read_csv('CoronavirusPL - Timeseries.csv', parse_dates = True)
dataGeneral = pd.read_csv('CoronavirusPL - General.csv', parse_dates= True)

#Zadanie 1
linia1 = dataGeneral["Confirmed"]
linia2 = dataGeneral["Recovered"]
linia3 = dataGeneral["Deaths"]
os = dataGeneral["Timestamp"]
plt.plot(os, linia1, marker = '.')
plt.plot(os, linia2, marker = '.')
plt.plot(os, linia3, marker = '.')
plt.tick_params(axis = 'x', labelsize = 6, rotation = 90)
plt.show()

#Zadanie 2
provinces = dataTimeseries["Province"].unique().tolist()
chorzy = []
for element in provinces:
    a = dataTimeseries.loc[(dataTimeseries['Province'] == element) & (dataTimeseries['Infection/Death/Recovery'] == 'I')]
    chorzy.append(len(a))
plt.bar(provinces, chorzy, color = '#ccd5ae')
plt.tick_params(axis = 'x', labelsize = 6, rotation = 90)
plt.show()

#Zadanie 3
plec = ["Kobiety", "Mezczyzni"]
choreKobiety = dataTimeseries.loc[(dataTimeseries['Sex'] == 'F') & (dataTimeseries['Infection/Death/Recovery']=='D')]
chorzyFaceci = dataTimeseries.loc[(dataTimeseries['Sex'] == 'M') & (dataTimeseries['Infection/Death/Recovery']=='D')]
wyniki = [len(choreKobiety), len(chorzyFaceci)]
pleckolory = ['#ffcad4','#90e0ef']
plt.pie(wyniki, labels = plec, autopct = '%1.1f%%', colors=pleckolory)
plt.show()

#Zadanie 4

widelki_wiekowe = [
    [1, 35],
    [36, 50],
    [51, 70],
    [71, 100],
    [101, 140]
]
DataLabels = []

smierci_wg_wieku = []
dane_wiek_out = []
for wiek in widelki_wiekowe:
    appendedVal = dataTimeseries.loc[(dataTimeseries['Age'] >= wiek[0]) & (dataTimeseries['Age'] <= wiek[1]) & (dataTimeseries['Infection/Death/Recovery'] == 'D')]
    dane_wiek_out.append(appendedVal)
    smierci_wg_wieku.append(len(appendedVal))
    DataLabels.append((str(wiek[0])+'-'+str(wiek[1])))


for  index , element in  enumerate(smierci_wg_wieku):
    if element == 0:
        DataLabels.pop(index)
        smierci_wg_wieku.pop(index)

DataColors =  ['#dad7cd', '#a3b18a', '#588157', '#3a5a40', '#344e41']
plt.pie(smierci_wg_wieku, labels = DataLabels, autopct = '%1.1f%%', colors = DataColors)
plt.show()

