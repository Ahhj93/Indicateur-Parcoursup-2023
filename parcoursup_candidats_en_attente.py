import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Charger les données à partir du fichier CSV
    data = pd.read_csv("Parcoursup 2023 - Total.csv", delimiter=";")

    # Extraire les colonnes nécessaires
    dates = pd.to_datetime(data["Date"], format="%d/%m") # type: ignore
    en_attente = data[
        "Candidats n'ayant pas encore reçu de proposition ou en attente de place"
    ]

    # Créer les limites des bacs pour l'histogramme en escalier
    x = range(len(dates) + 1)
    y = list(en_attente) + [en_attente.iloc[-1]]  # Candidats en attente

    # Créer le graphique avec la courbe en rouge pour les candidats en attente
    plt.figure(figsize=(8, 6))
    plt.step(x, y, where="post", color="orange", linewidth=2, alpha=0.7)
    plt.xlabel("Date")
    plt.ylabel(
        "Candidats n'ayant pas encore reçu de\nproposition ou en attente de place"
    )
    plt.title(
        "Évolution en fonction du temps du nombre de\ncandidats sans affectation sur Parcoursup en 2023"
    )
    x_ticks = range(0, len(dates), 3)
    x_labels = dates[x_ticks].dt.strftime("%d/%m") # type: ignore
    plt.xticks(x_ticks, x_labels, rotation=45)

    # Ajuster les limites de l'axe x pour supprimer l'espace blanc à gauche
    plt.xlim(0, len(dates) - 1)

    plt.ylim(0, 400000)
    plt.twinx()
    plt.ylim(0, (400000 / 827271) * 100)
    plt.ylabel("Pourcentage en fonction du nombre de candidats")
    plt.tight_layout()
    plt.savefig(
        "Évolution en fonction du temps du nombre de candidats sans affectation sur Parcoursup en 2023.svg"
    )
    print(
        "Le graphique a été enregistré dans le fichier 'Évolution en fonction du temps du nombre de candidats sans affectation sur Parcoursup en 2023.svg'."
    )
    plt.close()


if __name__ == "__main__":
    main()
