import streamlit as st
import pandas as pd
import pydeck as pdk

# Funzione per caricare il dataset
@st.cache
def load_data():
    # Sostituisci con il tuo dataset
    data = pd.read_csv("emissioni.csv")
    return data

# Carica i dati
data = load_data()

# Filtro anno scelto dall'utente
year = st.slider("Seleziona un anno", min_value=data["year"].min(), max_value=data["year"].max(), step=1)
filtered_data = data[data["year"] == year]

# Layer per le emissioni come "nuvole"
layer = pdk.Layer(
    "HeatmapLayer",
    data=filtered_data,
    get_position=["lon", "lat"],
    get_weight="emissioni",  # Intensità basata sulle emissioni
    radius=50000,  # Raggio delle nuvole (in metri)
    opacity=0.8,  # Trasparenza delle nuvole
)

# Stato iniziale della mappa
view_state = pdk.ViewState(
    latitude=20,  # Centro della mappa
    longitude=0,
    zoom=1.5,
    pitch=45,  # Angolazione per vedere l'altezza
)

# Configura la mappa
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{emissioni} emissioni"},
))
