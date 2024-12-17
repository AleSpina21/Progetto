import altair as alt
import streamlit as st
#from sklearn.linear_model import LinearRegression
#from sklearn.impute import SimpleImputer

def plot_detection_methods(df):
    selected_year = st.slider("Seleziona l'anno", min_value=int(2002), max_value=int(2023), step=1)
    filtered_data = df[df['discoveryyear'] == selected_year]
    method_counts = filtered_data['discoverymethod'].value_counts().reset_index()
    method_counts.columns = ['discoverymethod', 'count']
    chart = alt.Chart(method_counts).mark_bar().encode(
        x=alt.X('discoverymethod:N', title='Metodo di rilevazione', sort='y'),
        y=alt.Y('count:Q', title='Numero di rilevazioni'),
        color='discoverymethod:N',
        tooltip=['discoverymethod:N', 'count:Q']
    ).properties(
        title=f"Numero di rilevazioni per metodo nel {selected_year}",
        width=800,
        height=400
    )
    
    st.altair_chart(chart, use_container_width=True)



def final_dataset(df):
    eliminate_columns = [
         "binaryflag", "age", "discoverymethod", "discoveryyear", "lastupdate", "system_rightascension", "system_declination", "system_distance", "hoststar_age", "list"
    ]
    filtered_df = df.drop(columns=eliminate_columns)
    missing = filtered_df.isnull().mean() 
    drop_col = missing[missing >= 0.90].index
    df_final = filtered_df.drop(columns=drop_col)
    return df_final


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
