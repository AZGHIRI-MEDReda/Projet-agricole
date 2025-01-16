from data_manager import AgriculturalDataManager
from bokeh.io import curdoc
from bokeh.io import curdoc
from dashboard import AgriculturalDashboard
from data_manager import AgriculturalDataManager
from map_vizualisation import AgriculturalMap
from report_generator import AgriculturalAnalyzer


# Initialisation
data_manager = AgriculturalDataManager()
data_manager.load_data()

dashboard = AgriculturalDashboard(data_manager)
layout = dashboard.create_layout()

if layout is not None:
    curdoc().add_root(layout)
    curdoc().title = "Tableau de Bord Agricole"
else:
    print("Erreur : La mise en page n'a pas été créée.")

print("Parcelles disponibles :", dashboard.get_parcelle_options())


merged_data = data_manager.prepare_features()
print("Aperçu des données fusionnées :")
print(merged_data.columns)

stress_data = dashboard.prepare_stress_data()
print("Données préparées pour la matrice de stress :")
print(stress_data)







'''if __name__ == "__main__":
    # Initialisation du gestionnaire de données
    data_manager = AgriculturalDataManager()
    print('-------------------------------------------')
    # Chargement des données
    data_manager.load_data()

    # Configuration des indices temporels
    data_manager._setup_temporal_indices()
    print('-------------------------------------------')

    # Vérification de la cohérence des données
    data_manager._verify_temporal_consistency()
    print('-------------------------------------------')

    # Préparation des caractéristiques
    features = data_manager.prepare_features()
    print('-------------------------------------------')

    # Analyse des patterns temporels pour une parcelle
    parcelle_id = 'P001'
    history, trend = data_manager.get_temporal_patterns(parcelle_id)
    history = data_manager.get_temporal_patterns(parcelle_id)


    if trend:
        print(f"Tendance de rendement : {trend['pente']:.2f} tonnes /ha/an")
        print(f"Variation moyenne : {trend['variation_moyenne']*100:.1f}%")
    else:
        print(f"Aucune donnée de tendance trouvée pour la parcelle {parcelle_id}.")
    print('-------------------------------------------')
'''

# Initialisation du gestionnaire de données
data_manager = AgriculturalDataManager()

# Chargement des données
data_manager.load_data()
print('=====================================')

# Préparation des caractéristiques
features = data_manager.prepare_features()
print('====================================================')
merged_data = data_manager.prepare_features()
print("Aperçu des données fusionnées :")
print(merged_data.columns)

stress_data = dashboard.prepare_stress_data()
print("Données préparées pour la matrice de stress :")
print(stress_data)

# Analyse des patterns temporels pour une parcelle spécifique
parcelle_id = 'P001'
history, trend = data_manager.get_temporal_patterns(parcelle_id)
print('==========================================')

# Calcul des métriques de risque
risk_metrics = data_manager.calculate_risk_metrics(features)
print('====================================================')
# Affichage des résultats
if trend is not None:
    print(f"Tendance de rendement : {trend['biomasse_estimee']:.2f} tonnes/ha/an")
    print(f"Variation moyenne : {trend['lai']*100:.1f}%")
else:
    print("Aucune tendance disponible.")

    # Calcul des métriques de risque
    risk_metrics = data_manager.calculate_risk_metrics(features)
    print(risk_metrics[['date', 'score_risque_global']].head())
    print('-------------------------------------------')
print('====================================================')


# Vérifiez les données disponibles
print(data_manager.yield_history.head())
print('------------------------------------------------------------------------')

print(data_manager.yield_history.columns)

# Analyse pour la parcelle P001
parcelle_id = 'P001'
result = data_manager.analyze_yield_patterns(parcelle_id)

if result:
    decomposition, trend, seasonal, residual, analysis_summary = result

    print(f"Analyse réussie pour la parcelle {parcelle_id} :")
    print("Résumé de l'analyse :", analysis_summary)

    # Visualiser les composantes
    decomposition.plot()
else:
    print(f"Analyse échouée pour la parcelle {parcelle_id}.")

print('-------------------------------------------')

# Analyse pour la parcelle P002
parcelle_id = 'P002'
result = data_manager.analyze_yield_patterns(parcelle_id)

if result:
    decomposition, trend, seasonal, residual, analysis_summary = result

    print(f"Analyse réussie pour la parcelle {parcelle_id} :")
    print('-------------------------------------------')

    print("Résumé de l'analyse :", analysis_summary)

    # Visualiser les composantes
    decomposition.plot()
else:
    print(f"Analyse échouée pour la parcelle {parcelle_id}.")



#officiel map :


from folium import Map
from data_manager import AgriculturalDataManager  # Importez votre classe DataManager
from map_vizualisation import AgriculturalMap  # Importez la classe AgriculturalMap

'''# Étape 1 : Initialiser et charger les données
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Étape 2 : Initialiser la carte agricole
agricultural_map = AgriculturalMap(data_manager)

# Étape 3 : Créer la carte de base
agricultural_map.create_base_map()

# Étape 4 : Ajouter des couches à la carte
agricultural_map.add_yield_history_layer()
agricultural_map.add_current_ndvi_layer()
agricultural_map.add_risk_heatmap()

# Étape 5 : Sauvegarder et afficher la carte
output_file = "agricultural_dashboard.html"
if agricultural_map.map:
    agricultural_map.map.save(output_file)
    print(f"Carte sauvegardée avec succès dans : {output_file}")
else:
    print("Erreur : La carte n'a pas pu être créée.")
'''



#analyser report
'''data_manager = AgriculturalDataManager()
data_manager.load_data()

analyzer = AgriculturalAnalyzer(data_manager)
result = analyzer.analyze_yield_factors('P001')
print("Facteurs influençant les rendements :", result)'''



#RAPPORT 
# Import des classes nécessaires
from data_manager import AgriculturalDataManager
from report_generator import AgriculturalReportGenerator
from report_generator import AgriculturalAnalyzer

'''# Étape 1 : Initialisation des classes
data_manager = AgriculturalDataManager()
data_manager.load_data()

analyzer = AgriculturalAnalyzer(data_manager)
report_generator = AgriculturalReportGenerator(analyzer, data_manager)

# Étape 2 : Génération du rapport pour une parcelle spécifique
parcelle_id = "P001"  # Remplacez par l'ID de votre parcelle
report_generator.generate_parcelle_report(parcelle_id)

# Étape 3 : Vérifiez si le fichier PDF est généré
print("Le rapport est généré sous le nom 'report.pdf'. Ouvrez-le pour le visualiser.")
'''

from agri_validation import AgriculturalValidation
# Initialiser les classes nécessaires
data_manager = AgriculturalDataManager()
data_manager.load_data()

'''analyzer = AgriculturalAnalyzer(data_manager)
report_generator = AgriculturalReportGenerator(analyzer, data_manager)

# Initialiser le système de validation
validation_system = AgriculturalValidation(analyzer, report_generator)

# Effectuer la validation pour une parcelle spécifique
parcelle_id = "P001"  # Remplacez par l'ID de la parcelle à analyser
validation_system.validate_recommendations(parcelle_id, actual_yields)

# Générer un rapport de validation
validation_system.generate_validation_report(parcelle_id)'''

from report_generator import AgriculturalReportGenerator, AgriculturalAnalyzer

# Exemple d'initialisation et d'appel des classes
from report_generator import AgriculturalReportGenerator
from agri_validation import AgriculturalValidation
from data_manager import AgriculturalDataManager

# Initialisez le gestionnaire de données
data_manager = AgriculturalDataManager()
data_manager.load_data()

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from data_manager import AgriculturalDataManager  # Assurez-vous que cette classe est correcte
from agri_validation import AgriculturalAnalyzer  # Importez la classe

# Étape 1 : Initialiser le gestionnaire de données et charger les données
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Étape 2 : Initialiser l'analyseur agricole
analyzer = AgriculturalAnalyzer(data_manager)

# Étape 3 : Définir les paramètres d'analyse
column_to_analyze = "ndvi"  # Exemple de colonne (remplacez par 'lai', 'stress_hydrique', etc.)
parcelle_id_to_analyze = "P001"  # Spécifiez l'ID de la parcelle si nécessaire
window_size = 7  # Taille de la fenêtre pour la moyenne mobile

# Étape 4 : Exécuter l'analyse des tendances
results = analyzer.analyze_trends(column=column_to_analyze, parcelle_id=parcelle_id_to_analyze, window_size=window_size)

# Étape 5 : Afficher les résultats dans le terminal
if results:
    print("\n=== Résumé des résultats ===\n")
    print("Moyenne Mobile :")
    print(results["Moyenne Mobile"].head())  # Affiche les premières lignes de la moyenne mobile
    print("\nCoefficient de Tendance (Slope) :", results["Tendance (slope)"])
    print("Intercept :", results["Intercept"])
    print("Direction de la Tendance :", results["Direction de la Tendance"])



#dashboard

from bokeh.io import curdoc
from dashboard import AgriculturalDashboard  # Importez la classe
from data_manager import AgriculturalDataManager  # Importez votre gestionnaire de données

# Charger les données avec le gestionnaire de données
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Initialiser le tableau de bord
dashboard = AgriculturalDashboard(data_manager)

# Créer la mise en page
layout = dashboard.create_layout()

# Ajouter la mise en page au document Bokeh
curdoc().add_root(layout)
curdoc().title = "Tableau de Bord Agricole"


# Crée la mise en page
layout = dashboard.create_layout()

# Affiche des informations pour le débogage
merged_data = data_manager.prepare_features(data_manager.data)
print("Aperçu des données fusionnées :")
print(merged_data.columns)

stress_data = dashboard.prepare_stress_data()
print("Données préparées pour la matrice de stress :")
print(stress_data)
print("Valeur de yield_history :", data_manager.yield_history)

'''
from data_manager import AgriculturalDataManager  # Modifiez selon votre projet
from agri_validation import predict_risks
# Charger les données météorologiques
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Extraire les données météorologiques
weather_data = data_manager.weather_data

# Prédire les risques phytosanitaires
enriched_weather_data = predict_risks(weather_data, threshold_temp=30, threshold_humidity=85)

# Afficher les résultats
if enriched_weather_data is not None:
    print("\nDonnées enrichies avec les niveaux de risque :")
    print(enriched_weather_data.head())  # Affiche les premières lignes avec la colonne 'risk_level'



data_manager = AgriculturalDataManager()
data_manager.load_data()

agri_map = AgriculturalMap(data_manager)
agri_map.create_base_map()
agri_map.add_irrigation_layer(threshold_stress=0.3)
agri_map.add_yield_history_layer()
agri_map.add_climate_sensitive_zones(temp_threshold=35, humidity_threshold=30)
agri_map.show_map().save("agricultural.html")
print("Carte générée et sauvegardée sous 'agricultural.html'.")'''
