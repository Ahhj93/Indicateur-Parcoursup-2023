import matplotlib.pyplot as plt
import pandas as pd

# Charger les données à partir du fichier CSV
data = pd.read_csv('Parcoursup 2023 - Total.csv', delimiter=';')

# Extraire les colonnes nécessaires
dates = pd.to_datetime(data['Date'], format='%d/%m')
en_attente = data["Candidats n'ayant pas encore reçu de proposition ou en attente de place"]

# Créer les limites des bacs pour l'histogramme en escalier
x = range(len(dates)+1)
y = list(en_attente) + [en_attente.iloc[-1]]

# Créer l'histogramme en escalier avec une courbe plus épaisse
plt.step(x, y, where='post', color='steelblue', linewidth=2, alpha=0.7)
plt.xlabel('Date')
plt.ylabel("Candidats n'ayant pas encore reçu de\nproposition ou en attente de place")
plt.title("Évolution en fonction du temps du nombre de\ncandidats sans affectation sur Parcoursup en 2023")

# Sélectionner les positions et les étiquettes des dates à afficher
x_ticks = range(0, len(dates), 3)
x_labels = dates[x_ticks].dt.strftime('%d/%m')

# Définir les positions et les étiquettes des ticks sur l'axe des x
plt.xticks(x_ticks, x_labels, rotation=45)

# Axe y
plt.ylim(0, 400000)

# Afficher le graphique
plt.tight_layout()
plt.show()
