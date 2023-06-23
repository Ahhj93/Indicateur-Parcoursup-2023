import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Charger les données à partir du fichier CSV
    data = pd.read_csv('Parcoursup 2023 - Total.csv', delimiter=';')

    # Extraire les colonnes nécessaires
    dates = pd.to_datetime(data['Date'], format='%d/%m')
    recus = data["Candidats ayant reçu une ou plusieurs propositions d'admission"].fillna(0)
    quittes = data["Candidats ayant quitté la plateforme avant de recevoir une proposition d'admission"].fillna(0)
    non_quittes = data["Candidats n'ayant pas encore reçu de proposition ou en attente de place n'ayant pas quitté la plateforme"].fillna(0)

    # Créer les limites des bacs pour l'histogramme empilé
    x = range(len(dates))

    # Définir la taille du graphique
    plt.figure(figsize=(8, 6))

    # Tracer l'histogramme empilé avec des barres collées
    plt.bar(x, recus, width=1, color='green', label="Candidats admis")
    plt.bar(x, quittes, width=1, bottom=recus, color='red', label="Candidats ayant quitté")
    plt.bar(x, non_quittes, width=1, bottom=recus + quittes, color='orange', label="Candidats en attente")

    # Ajouter les étiquettes et les titres
    plt.xlabel('Date')
    plt.ylabel('Nombre de candidats')
    plt.title("Évolution du statut des candidats sur Parcoursup en 2023")

    # Simplifier les étiquettes des dates
    x_ticks = range(0, len(dates), 3)
    x_labels = dates[x_ticks].dt.strftime('%d/%m')

    # Définir les positions et les étiquettes des ticks sur l'axe des x
    plt.xticks(x_ticks, x_labels, rotation=45)

    # Ajuster les limites de l'axe x pour supprimer l'espace blanc à gauche
    plt.xlim(-0.5, len(dates) - 0.5)

    # Ajouter une légende
    plt.legend()

    # Définir les limites des axes y pour le nombre de candidats
    plt.ylim(0, 827271)

    # Créer un deuxième axe y pour le pourcentage
    plt.twinx()
    # Définir les limites des axes y pour le pourcentage
    plt.ylim(0, 100)
    # Ajouter l'étiquette pour l'axe y du pourcentage
    plt.ylabel('Pourcentage en fonction du Nombre de candidats')

    # Afficher le graphique
    plt.tight_layout()
    plt.savefig("Évolution du statut des candidats sur Parcoursup en 2023.svg")
    print("Le graphique a été enregistré dans le fichier 'Évolution du statut des candidats sur Parcoursup en 2023'.")
    plt.close()

if __name__ == '__main__':
    main()