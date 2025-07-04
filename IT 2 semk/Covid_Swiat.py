import pandas as pd
import matplotlib.pyplot as plt

confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')

countries = ['Poland', 'Italy', 'Spain', 'Germany', 'Albania']


for country in countries:
    data = confirmed_df.loc[confirmed_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    plt.plot(data.index, data.values, label = country)

plt.title('Liczba potwierdzonych przypadków koronawirusa')
plt.xlabel('Data')
plt.ylabel('Liczba przypadków')
plt.legend()
plt.show()

for country in countries:
    confirmed_cases = confirmed_df.loc[confirmed_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    death_cases = deaths_df.loc[deaths_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    mortality_rate = (death_cases / confirmed_cases) * 100
    plt.bar(country, mortality_rate[-1], label=country)

worldwide_mortality_rate = (deaths_df.iloc[:, 4:].sum(axis=0) / confirmed_df.iloc[:, 4:].sum(axis=0)) * 100
plt.axhline(worldwide_mortality_rate[-1], color='black', linestyle='--', label='Średni wskaźnik śmiertelności na świecie')

plt.title('Współczynnik śmiertelności')
plt.xlabel('Kraj')
plt.ylabel('Współczynnik śmiertelności')
plt.legend()
plt.show()

for country in countries:
    confirmed_cases = confirmed_df.loc[confirmed_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    death_cases = deaths_df.loc[deaths_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    mortality_rate = (death_cases / confirmed_cases) * 100
    plt.plot(mortality_rate.index, mortality_rate.values, label=country)
    
plt.title('Ilosc zakażonym w danym kraju')
plt.xlabel('Kraj')
plt.ylabel('Współczynnik zakażeń')
plt.legend()
plt.show()