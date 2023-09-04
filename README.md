# Indicateur Parcoursup 2023
Ce projet vise à afficher l'évolution des candidats sur Parcoursup pour l'année 2023.

## 📋 Prérequis
* Python 3.x 🐍
* Matplotlib 📊
* Pandas 🐼

## ⚙️ Installation
1. Clonez ce dépôt de code sur votre machine locale :
```bash
git clone https://github.com/Ahhj93/Indicateur-Parcoursup-2023.git
````

2. Accédez au répertoire du projet :
```bash
cd Indicateur-Parcoursup-2023
```

3.Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation
1. Placez votre fichier CSV contenant les données de Parcoursup dans le répertoire du projet et assurez-vous qu'il est nommé `Parcoursup 2023 - Total.csv`.

2. Exécutez le script Python pour afficher le graphique :
```bash
python main.py
```

3. Les graphiques seront enregistrés dans le répertoire du projet au format SVG.

## 👀 Aperçu du graphique
<p align="center">
  <img width="500" src="https://raw.githubusercontent.com/Ahhj93/Indicateur-Parcoursup-2023/main/%C3%89volution%20en%20fonction%20du%20temps%20du%20nombre%20de%20candidats%20sans%20affectation%20sur%20Parcoursup%20en%202023.svg">
  <img width="500" src="https://raw.githubusercontent.com/Ahhj93/Indicateur-Parcoursup-2023/main/%C3%89volution%20en%20fonction%20du%20temps%20du%20nombre%20de%20candidats%20ayant%20re%C3%A7u%20des%20propositions%20sur%20Parcoursup%20en%202023.svg">
  <img width="500" src="https://raw.githubusercontent.com/Ahhj93/Indicateur-Parcoursup-2023/main/%C3%89volution%20en%20fonction%20du%20temps%20du%20statut%20des%20candidats%20sur%20Parcoursup%20en%202023.svg">
</p>

## 🔍 Source des données
Les données utilisées dans ce projet proviennent du tableau de bord des indicateurs statistiques de Parcoursup 2023 du [Ministère de l’Enseignement supérieur et de la Recherche](https://github.com/MinistereSupRecherche), accessible à l'adresse suivante : [enseignementsup-recherche.gouv.fr/fr/parcoursup-2023-tableau-de-bord-des-indicateurs-statistiques-91079](https://www.enseignementsup-recherche.gouv.fr/fr/parcoursup-2023-tableau-de-bord-des-indicateurs-statistiques-91079).

> « Les données chiffrées de ce tableau de bord permettent de suivre, du 1er juin au 8 juillet 2023 (au lendemain de la fin de la phase d'admission principale afin de tenir compte des résultats définitifs du baccalauréat), l'évolution de la situation des lycéens de terminale scolarisés en France ou préparant le baccalauréat français dans un lycée français à l’étranger, des étudiants en réorientation et des candidats scolarisés à l'étranger en dehors des établissements français, qui ont confirmé au moins un vœu sur Parcoursup. Il est actualisé quotidiennement. »

> « Ce tableau de bord ne fait pas état de la situation des candidats en "reprise d'études" dont l’accompagnement est prévu en lien avec le ministère du Travail, du Plein emploi et de l’Insertion ainsi que les partenaires de la formation professionnelle associés dans le cadre du module Parcours+ afin, le cas échéant, de leur proposer des formations et des services adaptés à leur profil et à leur projet. »

## 📄 Licence
Les données utilisées dans ce projet sont distribuées sous la [licence ouverte 2.0 d'Etalab](https://github.com/etalab/licence-ouverte/blob/master/LO.md).

Le code source de ce projet est distribué sous la licence MIT. Vous pouvez consulter les détails de cette licence dans le fichier [LICENSE](https://github.com/Ahhj93/Indicateur-Parcoursup-2023/blob/main/LICENSE).

Veuillez noter que les informations ci-dessus sont fournies à titre indicatif et que vous devez vous référer à la licence ouverte 2.0 d'Etalab pour les conditions spécifiques de réutilisation des données.

Pour toute question concernant la licence des données, veuillez vous référer à la licence ouverte 2.0 d'Etalab. Pour toute question concernant la licence du code source, veuillez vous référer au fichier LICENSE.

Pour plus d'informations sur le projet et son fonctionnement, veuillez consulter le code source et les fichiers associés.
