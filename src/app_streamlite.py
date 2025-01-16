import streamlit as st
from data_manager import AgriculturalDataManager  # Classe pour gérer les données
from integration import IntegratedDashboard  # Tableau de bord intégré

# Initialiser le gestionnaire de données
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Initialiser le tableau de bord intégré
dashboard = IntegratedDashboard(data_manager)

# Initialiser les visualisations
dashboard.initialize_visualizations()

# Afficher le tableau de bord dans Streamlit
dashboard.create_streamlit_dashboard()

'''
import streamlit as st
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import components
from streamlit_folium import st_folium
import folium
from data_manager import AgriculturalDataManager
from dashboard import AgriculturalDashboard
from map_vizualisation import AgriculturalMap

# Titre de l'application
st.title("Tableau de Bord Agricole Interactif")

# Initialisation du gestionnaire de données
st.sidebar.header("Options")
st.sidebar.subheader("Chargement des données")
data_manager = AgriculturalDataManager()
data_manager.load_data()

# Sélection de la parcelle
parcelles = data_manager.monitoring_data['parcelle_id'].unique()
selected_parcelle = st.sidebar.selectbox("Sélectionnez une parcelle", parcelles)

# Création du tableau de bord Bokeh
st.sidebar.subheader("Visualisations")
dashboard = AgriculturalDashboard(data_manager)
bokeh_layout = dashboard.create_layout()

# Ajout de la carte Folium
st.sidebar.subheader("Carte")
agri_map = AgriculturalMap(data_manager)
agri_map.create_base_map()
agri_map.add_irrigation_layer(threshold_stress=0.3)
agri_map.add_yield_history_layer()
agri_map.add_climate_sensitive_zones(temp_threshold=35, humidity_threshold=30)

# Intégration de Bokeh dans Streamlit
st.subheader("Visualisations")
bokeh_script, bokeh_div = components(bokeh_layout)
st.components.v1.html(bokeh_script + bokeh_div, height=1000, scrolling=True)

# Intégration de Folium dans Streamlit
st.subheader("Carte Interactive")
map_component = st_folium(agri_map.show_map(), width=700, height=500)
'''
