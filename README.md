# Projet d'Analyse Agricole

## Description
Ce projet est une solution d'analyse et de gestion des données agricoles permettant de surveiller, analyser et optimiser la performance des parcelles agricoles. Il combine des outils d'analyse des données (NDVI, stress hydrique, rendements estimés), des visualisations interactives (cartes, graphiques) et des modèles pour fournir des recommandations précises et exploitables pour les agriculteurs et les gestionnaires.

## Fonctionnalités
- **Analyse des performances agricoles** :
  - Analyse des rendements (estimés et réels).
  - Détection des tendances et variations saisonnières.
- **Gestion des risques phytosanitaires** :
  - Prédiction des risques basés sur les seuils climatiques (température et humidité).
- **Cartographie interactive** :
  - Visualisation des parcelles avec stress hydrique élevé.
  - Cartes interactives des rendements estimés et historiques.
- **Rapports automatisés** :
  - Génération de rapports au format Markdown ou PDF avec des recommandations spécifiques.

## Technologies Utilisées
- **Langage** : Python
- **Bibliothèques principales** :
  - Pandas (gestion des données)
  - NumPy (calculs mathématiques)
  - Scipy (analyses statistiques)
  - Folium (cartes interactives)
  - Matplotlib et Seaborn (visualisations)
  - Scikit-learn (modèles prédictifs)
  - Streamlit (interface utilisateur interactive)

## Structure du Projet
```
.
├── data_manager.py        # Gestion des données (monitoring, météo, sol)
├── analyzer.py            # Analyse des données agricoles
├── report_generator.py    # Génération des rapports
├── validation.py          # Validation des prédictions et recommandations
├── app.py                 # Interface utilisateur avec Streamlit
├── README.md              # Documentation du projet
├── requirements.txt       # Dépendances Python
├── data/                  # Dossier des données (CSV, JSON, etc.)
├── outputs/               # Dossier des rapports générés (PDF, images)
└── visuals/               # Graphiques et cartes générés
```

## Installation

1. **Cloner le dépôt** :
```bash
git clone https://github.com/votre-utilisateur/projet-agricole.git
cd projet-agricole
```

2. **Créer un environnement virtuel et installer les dépendances** :
```bash
python -m venv env
source env/bin/activate   # Pour Linux/Mac
env\Scripts\activate     # Pour Windows
pip install -r requirements.txt
```

3. **Lancer l'application Streamlit** :
```bash
streamlit run app.py
```

## Utilisation
- **Analyse des données** : Chargez vos fichiers de données (CSV/JSON) dans le dossier `data/`.
- **Visualisation interactive** : Accédez aux cartes et graphiques via l'interface Streamlit.
- **Génération de rapports** : Les rapports seront générés dans le dossier `outputs/`.

## Exemples de Visualisations
1. **Matrice de stress hydrique** :
![Matrice de Stress](visuals/matrice_stress.png)
2. **Évolution du NDVI** :
![NDVI](visuals/evolution_ndvi.png)
3. **Historique des rendements** :
![Rendements](visuals/rendements_parcelles.png)

## Contributions
Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez :
1. Forker le dépôt.
2. Créer une branche pour votre fonctionnalité ou correction de bug :
   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalite
   ```
3. Soumettre une Pull Request.

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

## Contact
Pour toute question ou suggestion, contactez [votre nom] à l'adresse : **votre-email@example.com**.

---

Profitez de cet outil pour optimiser la gestion de vos parcelles agricoles et améliorer vos rendements de manière durable ! 🌾
