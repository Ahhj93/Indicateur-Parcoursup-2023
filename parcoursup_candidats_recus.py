import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Charger les données à partir du fichier CSV
    data = pd.read_csv('Parcoursup 2023 - Total.csv', delimiter=';')

    # Extraire les colonnes nécessaires
    dates = pd.to_datetime(data['Date'], format='%d/%m')
    recus = data["Candidats ayant reçu une ou plusieurs propositions d'admission"]

    # Créer les limites des bacs pour l'histogramme en escalier
    x = range(len(dates)+1)
    y = list(recus) + [recus.iloc[-1]]  # Candidats ayant reçu une ou plusieurs propositions

    # Créer le graphique avec la courbe en vert pour les candidats ayant reçu une ou plusieurs propositions
    plt.figure(figsize=(8, 6))
    plt.step(x, y, where='post', color='green', linewidth=2, alpha=0.7)
    plt.xlabel('Date')
    plt.ylabel('Candidats ayant reçu une ou\nplusieurs propositions d\'admission')
    plt.title('Évolution en fonction du temps du nombre de\ncandidats ayant reçu des propositions sur Parcoursup en 2023')
    x_ticks = range(0, len(dates), 3)
    x_labels = dates[x_ticks].dt.strftime('%d/%m')
    plt.xticks(x_ticks, x_labels, rotation=45)
    plt.ylim(0, 800000)
    plt.twinx()
    plt.ylim(0, (800000/827271)*100)
    plt.ylabel('Pourcentage en fonction du Nombre de candidats')
    plt.tight_layout()
    plt.savefig("Évolution en fonction du temps du nombre de candidats ayant reçu des propositions sur Parcoursup en 2023.svg")
    print("Le graphique a été enregistré dans le fichier 'Évolution en fonction du temps du nombre de candidats ayant reçu des propositions sur Parcoursup en 2023.svg'.")
    plt.close()

if __name__ == '__main__':
    main()