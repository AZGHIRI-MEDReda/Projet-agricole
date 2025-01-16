import numpy as np
import pandas as pd
from scipy import stats

class AgriculturalValidation:
    def __init__(self, analyzer, report_generator):
        """
        Initialise le système de validation des analyses
        et recommandations agricoles.
        """
        self.analyzer = analyzer
        self.report_generator = report_generator
        self.validation_metrics = {}

    def validate_recommendations(self, parcelle_id):
        """
        Valide les recommandations en comparant les résultats prédits
        (rendement_estime) aux rendements réels obtenus (rendement_final).
        """
        # Récupérer les données pour la parcelle depuis yield_history
        parcelle_data = self.report_generator.data_manager.yield_history[
            self.report_generator.data_manager.yield_history['parcelle_id'] == parcelle_id
        ]

        if parcelle_data.empty:
            print(f"Erreur : Pas de données pour la parcelle {parcelle_id}")
            return None

        predicted = parcelle_data['rendement_estime']
        actual = parcelle_data['rendement_final']

        # Vérifier si les colonnes sont complètes
        if predicted.isnull().any() or actual.isnull().any():
            print(f"Erreur : Données manquantes dans rendement_estime ou rendement_final pour {parcelle_id}")
            return None

        # Calculer les métriques d'erreur
        mae = np.mean(np.abs(predicted - actual))  # Mean Absolute Error
        mse = np.mean((predicted - actual) ** 2)  # Mean Squared Error
        rmse = np.sqrt(mse)                       # Root Mean Squared Error
        accuracy = 1 - (mae / actual.mean())      # Précision relative

        # Stocker les résultats dans les métriques de validation
        self.validation_metrics[parcelle_id] = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "Accuracy": accuracy
        }

        # Afficher les résultats dans le terminal
        print("\n")
        print("=" * 50)
        print(f"Validation des Recommandations pour la Parcelle : {parcelle_id}")
        print("-" * 50)
        print(f"  Rendement estimé moyen : {predicted.mean():.2f} t/ha")
        print(f"  Rendement final moyen  : {actual.mean():.2f} t/ha")
        print(f"  MAE (Erreur Moyenne Absolue) : {mae:.2f}")
        print(f"  MSE (Erreur Moyenne Quadratique) : {mse:.2f}")
        print(f"  RMSE (Racine de l'Erreur Quadratique) : {rmse:.2f}")
        print(f"  Précision : {accuracy:.2%}")
        print("=" * 50)

        return {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "Accuracy": accuracy
        }


    def _calculate_prediction_accuracy(self, predictions, actuals):
        """
        Calcule la précision des prédictions par rapport
        aux résultats réels.
        """
        mae = np.mean(np.abs(predictions - actuals))
        accuracy = 1 - (mae / actuals.mean())
        return accuracy

    def _update_confidence_factors(self, parcelle_id, accuracy):
        """
        Met à jour les facteurs de confiance pour
        différents types de recommandations.
        """
        if parcelle_id not in self.validation_metrics:
            self.validation_metrics[parcelle_id] = {}
        self.validation_metrics[parcelle_id]['Confidence'] = accuracy
        print(f"Facteur de confiance mis à jour pour la parcelle {parcelle_id} : {accuracy:.2%}")

    def generate_validation_report(self, parcelle_id):
        """
        Génère un rapport de validation détaillé pour
        améliorer les futures recommandations.
        """
        if parcelle_id not in self.validation_metrics:
            print(f"Aucune métrique de validation disponible pour la parcelle {parcelle_id}.")
            return None

        metrics = self.validation_metrics[parcelle_id]
        print("\nRapport de Validation :")
        print(f"Parcelle : {parcelle_id}")
        for key, value in metrics.items():
            print(f"  {key} : {value:.2f}")

    def _generate_improvement_suggestions(self, metrics):
        """
        Génère des suggestions pour améliorer la qualité
        des analyses et recommandations.
        """
        suggestions = []
        if metrics['Accuracy'] < 0.8:
            suggestions.append("Augmenter la granularité des données.")
            suggestions.append("Vérifier les conditions climatiques spécifiques.")
        if metrics['RMSE'] > 0.5:
            suggestions.append("Réexaminer les hypothèses du modèle.")
        if not suggestions:
            suggestions.append("Les performances sont satisfaisantes.")
        print("\nSuggestions d'amélioration :")
        for suggestion in suggestions:
            print(f"  - {suggestion}")

from sklearn.linear_model import LinearRegression

class AgriculturalAnalyzer:
    def __init__(self, data_manager):
        """
        Initialise l'analyseur agricole avec les données du gestionnaire.
        """
        self.data_manager = data_manager

    def analyze_trends(self, column, parcelle_id=None, window_size=7):
        """
        Analyse les tendances des indicateurs clés à l'aide des données du data_manager.

        Paramètres :
            column (str): Nom de la colonne à analyser (e.g., 'ndvi', 'lai', 'stress_hydrique').
            parcelle_id (str, optional): Si spécifié, analyse uniquement pour la parcelle donnée.
            window_size (int): Taille de la fenêtre pour la moyenne mobile (par défaut : 7).

        Retourne :
            dict : Résultats comprenant la moyenne mobile, les coefficients de tendance,
                   et des informations sur la direction des tendances.
        """
        # Charger les données de monitoring
        data = self.data_manager.monitoring_data

        if data is None or data.empty:
            print("Erreur : Les données de monitoring sont absentes ou vides.")
            return None

        # Filtrer par parcelle si spécifié
        if parcelle_id:
            data = data[data['parcelle_id'] == parcelle_id]

        if data.empty:
            print(f"Erreur : Pas de données disponibles pour la parcelle {parcelle_id}.")
            return None

        if column not in data.columns:
            print(f"Erreur : La colonne '{column}' est absente des données.")
            return None

        if 'date' not in data.columns:
            print("Erreur : Les données doivent contenir une colonne 'date'.")
            return None

        # Convertir les dates si nécessaire
        if not pd.api.types.is_datetime64_any_dtype(data['date']):
            data['date'] = pd.to_datetime(data['date'])

        # Trier par date
        data = data.sort_values(by='date')

        # Calculer la moyenne mobile
        data[f"{column}_ma"] = data[column].rolling(window=window_size).mean()

        # Supprimer les lignes NaN causées par la moyenne mobile
        trend_data = data.dropna(subset=[f"{column}_ma", 'date'])

        # Préparer les données pour la régression linéaire
        X = np.array((trend_data['date'] - trend_data['date'].min()).dt.days).reshape(-1, 1)
        y = trend_data[f"{column}_ma"]

        # Régression linéaire pour détecter la tendance
        model = LinearRegression()
        model.fit(X, y)
        trend_slope = model.coef_[0]  # Coefficient directeur
        trend_intercept = model.intercept_

        # Déterminer la direction de la tendance
        trend_direction = (
            "Croissante" if trend_slope > 0 else "Décroissante" if trend_slope < 0 else "Stable"
        )

        # Résumer les résultats
        results = {
            "Moyenne Mobile": trend_data[[f"{column}_ma", "date"]].copy(),
            "Tendance (slope)": trend_slope,
            "Intercept": trend_intercept,
            "Direction de la Tendance": trend_direction,
        }

        # Afficher les résultats dans le terminal
        print("\n")
        print("=" * 50)
        print(f"Analyse des Tendances pour '{column}'")
        if parcelle_id:
            print(f"Parcelle : {parcelle_id}")
        print("-" * 50)
        print(f"  Coefficient de Tendance (Slope) : {trend_slope:.5f}")
        print(f"  Intercept : {trend_intercept:.2f}")
        print(f"  Direction de la Tendance : {trend_direction}")
        print("=" * 50)

        return results


import pandas as pd

def predict_risks(weather_data, threshold_temp=25, threshold_humidity=80):
    """
    Prédit les risques phytosanitaires basés sur les conditions météorologiques.

    Paramètres :
        weather_data (pd.DataFrame): Les données météorologiques avec au moins les colonnes 'temperature' et 'humidite'.
        threshold_temp (float): Seuil de température au-delà duquel le risque est élevé.
        threshold_humidity (float): Seuil d'humidité au-delà duquel le risque est élevé.

    Retourne :
        pd.DataFrame: Les données enrichies avec une colonne 'risk_level' indiquant les niveaux de risque.
    """
    if weather_data is None or weather_data.empty:
        print("Erreur : Les données météorologiques sont absentes ou vides.")
        return None

    # Vérifier si les colonnes nécessaires sont présentes
    required_columns = ['date', 'temperature', 'humidite']
    for col in required_columns:
        if col not in weather_data.columns:
            print(f"Erreur : La colonne '{col}' est absente des données météorologiques.")
            return None

    # Ajouter une colonne 'risk_level' basée sur les seuils
    def calculate_risk(row):
        if row['temperature'] > threshold_temp and row['humidite'] > threshold_humidity:
            return "Élevé"
        elif row['temperature'] > threshold_temp or row['humidite'] > threshold_humidity:
            return "Modéré"
        else:
            return "Faible"

    weather_data['risk_level'] = weather_data.apply(calculate_risk, axis=1)

    # Compter le nombre de jours à risque par niveau
    risk_summary = weather_data['risk_level'].value_counts()

    # Afficher le résumé des risques
    print("\n=== Résumé des Risques ===")
    print(risk_summary)

    return weather_data
