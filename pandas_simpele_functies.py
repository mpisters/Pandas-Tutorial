# importeer pandas
import pandas as pd

# inlezen van data uit csv, csv moet in dezelfde folder zitten als het python/jupyter script
data = pd.read_csv('songs.csv')

# alle kolom namen
kolom_namen = list(data.columns)
print(kolom_namen)

# maximum waarde uit kolom
timbre_6_max = data['timbre_6_max']
hoogste_waarde_in_kolom_timbre_6_max = timbre_6_max.max()
print("max", hoogste_waarde_in_kolom_timbre_6_max)

# toon meerdere max waarden van verschillende kolommen
meerdere_kolommen = data[['timbre_6_max', 'timbre_5_max']]
meerdere_kolommen = meerdere_kolommen.max()
print(meerdere_kolommen)
print("\n")

# minumum waarde uit kolom
timbre_6_max = data['timbre_6_max']
laagste_waarde_in_kolom_timbre_6_max = timbre_6_max.min()
print("min", laagste_waarde_in_kolom_timbre_6_max)


# gemiddelde waarde uit kolom
timbre_6_max = data['timbre_6_max']
gemiddelde_in_kolom_timbre_6_max = timbre_6_max.mean()
print("avg", gemiddelde_in_kolom_timbre_6_max)

# verschillende statistieken over de kolom
timbre_6_max = data['timbre_6_max']
gemiddelde_in_kolom_timbre_6_max = timbre_6_max.describe()
print("statistiek")
print(gemiddelde_in_kolom_timbre_6_max)
