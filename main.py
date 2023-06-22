import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick

# Charger les données à partir du fichier CSV
data = pd.read_csv('Parcoursup 2023 - Total.csv', delimiter=';')

# Extraire les colonnes nécessaires
dates = pd.to_datetime(data['Date'], format='%d/%m')
en_attente = data["Candidats n'ayant pas encore reçu de proposition ou en attente de place"]
recus = data["Candidats ayant reçu une ou plusieurs propositions d'admission"]

# Créer les limites des bacs pour l'histogramme en escalier (pour les deux courbes)
x = range(len(dates)+1)
y1 = list(en_attente) + [en_attente.iloc[-1]]  # Candidats en attente
y2 = list(recus) + [recus.iloc[-1]]  # Candidats ayant reçu une ou plusieurs propositions

# Créer le premier graphique avec la courbe en rouge pour les candidats en attente
plt.figure(figsize=(8, 6))
plt.step(x, y1, where='post', color='red', linewidth=2, alpha=0.7)
plt.xlabel('Date')
plt.ylabel("Candidats n'ayant pas encore reçu de\nproposition ou en attente de place")
plt.title("Évolution en fonction du temps du nombre de\ncandidats sans affectation sur Parcoursup en 2023")
x_ticks1 = range(0, len(dates), 3)
x_labels1 = dates[x_ticks1].dt.strftime('%d/%m')
plt.xticks(x_ticks1, x_labels1, rotation=45)
plt.ylim(0, 400000)
plt.twinx()
plt.ylim(0, (400000/827271)*100)
plt.ylabel('Pourcentage en fonction du Nombre de candidats')
plt.tight_layout()
plt.savefig("Évolution en fonction du temps du nombre de candidats sans affectation sur Parcoursup en 2023.svg")
print("Le graphique a été enregistré dans le fichier 'Évolution en fonction du temps du nombre de candidats sans affectation sur Parcoursup en 2023.svg'.")
plt.close()

# Créer le deuxième graphique avec la courbe en vert pour les candidats ayant reçu une ou plusieurs propositions
plt.figure(figsize=(8, 6))
plt.step(x, y2, where='post', color='green', linewidth=2, alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Candidats ayant reçu une ou\nplusieurs propositions d\'admission')
plt.title('Évolution en fonction du temps du nombre de\ncandidats ayant reçu des propositions sur Parcoursup en 2023')
x_ticks2 = range(0, len(dates), 3)
x_labels2 = dates[x_ticks2].dt.strftime('%d/%m')
plt.xticks(x_ticks2, x_labels2, rotation=45)
plt.ylim(0, 800000)
plt.twinx()
plt.ylim(0, (800000/827271)*100)
plt.ylabel('Pourcentage en fonction du Nombre de candidats')
plt.tight_layout()
plt.savefig("Évolution en fonction du temps du nombre de candidats ayant reçu des propositions sur Parcoursup en 2023.svg")
print("Le graphique a été enregistré dans le fichier 'Évolution en fonction du temps du nombre de candidats ayant reçu des propositions sur Parcoursup en 2023.svg'.")
plt.close()