import streamlit as st
from map_vizualisation import AgriculturalMap
from dashboard import AgriculturalDashboard
import folium
from streamlit_folium import folium_static



class IntegratedDashboard:
    def __init__(self, data_manager):
        """
        Crée un tableau de bord intégré combinant graphiques Bokeh et carte Folium.
        """
        self.data_manager = data_manager
        self.bokeh_dashboard = AgriculturalDashboard(data_manager)
        self.map_view = AgriculturalMap(data_manager)

    def initialize_visualizations(self):
        """
        Initialise toutes les composantes visuelles.
        """
        self.bokeh_dashboard.create_layout()
        self.map_view.create_base_map()
        self.map_view.add_yield_history_layer()
        self.map_view.add_current_ndvi_layer()
        self.map_view.add_risk_heatmap()

    def create_streamlit_dashboard(self):
        """
        Crée une interface Streamlit intégrant toutes les visualisations.
        """
        self.setup_interactions()  # Configure les interactions

        st.title("Tableau de Bord Agricole Intégré")

        # Section des graphiques Bokeh
        st.header("Visualisations Bokeh")
        selected_parcelle = st.selectbox(
            "Sélectionnez une parcelle",
            options=self.bokeh_dashboard.get_parcelle_options()
        )
        self.update_visualizations(selected_parcelle)

        bokeh_placeholder = st.empty()
        bokeh_placeholder.bokeh_chart(self.bokeh_dashboard.create_layout(), use_container_width=True)

        # Section de la carte Folium
        st.header("Carte Agricole Interactive")
        folium_placeholder = st.empty()
        folium_map = self.map_view.show_map()
        folium_placeholder.write(folium_map._repr_html_(), unsafe_allow_html=True)
        folium_static(folium_map)



        # Section des graphiques Bokeh
        st.subheader("Visualisations Bokeh")
        st.markdown("Les graphiques ci-dessous montrent les tendances des rendements et des indices NDVI.")
        bokeh_placeholder = st.empty()
        bokeh_placeholder.bokeh_chart(self.bokeh_dashboard.create_layout(), use_container_width=True)

        # Section de la carte Folium
        st.subheader("Carte Agricole Interactive")
        st.markdown("Explorez les données spatiales et les tendances par parcelle.")
        folium_placeholder = st.empty()
        folium_map = self.map_view.show_map()
        folium_placeholder.write(folium_map._repr_html_(), unsafe_allow_html=True)

    def update_visualizations(self, parcelle_id):
        """
        Met à jour toutes les visualisations pour une parcelle donnée.
        """
        # Mise à jour des graphiques Bokeh
        self.bokeh_dashboard.update_plots('value', '', parcelle_id)

        # Mise à jour de la carte Folium
        self.map_view.create_base_map()
        self.map_view.add_yield_history_layer()
        self.map_view.add_current_ndvi_layer()
        self.map_view.add_risk_heatmap()



    def setup_interactions(self):
        """
        Configure les interactions entre les visualisations Bokeh et Folium.
        """
        # Ajouter un callback pour le sélecteur de parcelles Bokeh
        if hasattr(self.bokeh_dashboard, "create_parcelle_selector"):
            parcelle_selector = self.bokeh_dashboard.create_parcelle_selector()
            parcelle_selector.on_change('value', self.handle_parcelle_selection)

        print("Interactions Bokeh configurées.")

        # Note : Les interactions Folium nécessitent une approche basée sur les popups ou tooltips.
        # Exemple : Ajouter un survol personnalisé via des popups
        for _, row in self.data_manager.monitoring_data.iterrows():
            tooltip = f"Parcelle: {row['parcelle_id']}, NDVI: {row['ndvi']}"
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                color='blue',
                fill=True,
                fill_opacity=0.6,
                tooltip=tooltip
            ).add_to(self.map_view.map)

        print("Interactions Folium configurées.")

    
    def handle_parcelle_selection(self, attr, old, new):
        """
        Gère la sélection d’une nouvelle parcelle.
        """
        print(f"Parcelle sélectionnée : {new} (ancienne : {old})")

        # Mise à jour des visualisations Bokeh
        self.bokeh_dashboard.update_plots(attr, old, new)

        # Mise à jour des couches sur la carte Folium
        self.map_view.create_base_map()
        self.map_view.add_yield_history_layer()
        self.map_view.add_current_ndvi_layer()
        self.map_view.add_risk_heatmap()
        
    def handle_map_hover(self, feature):
        """
        Gère le survol d’une parcelle sur la carte.
        """
        # Exemple : Mettre en surbrillance les données liées sur la carte
        parcelle_id = feature['properties']['parcelle_id']  # À adapter selon vos données
        print(f"Survol de la parcelle : {parcelle_id}")
        self.update_visualizations(parcelle_id)

    
    def highlight_parcelle(self, parcelle_id):
        """
        Met en évidence une parcelle sélectionnée sur la carte.
        """
        for _, row in self.data_manager.monitoring_data.iterrows():
            if row['parcelle_id'] == parcelle_id:
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=f"Parcelle ID: {parcelle_id}",
                    icon=folium.Icon(color='red')
                ).add_to(self.map)






