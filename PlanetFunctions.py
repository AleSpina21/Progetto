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
import plotly.graph_objects as go 

# Funzione per caricare i dati
@st.cache
def load_data():
    return pd.read_csv("emissioni.csv")

# Carica il dataset
data = load_data()

# Seleziona l'anno con uno slider
year = st.slider("Seleziona un anno", min_value=1800, max_value=2023, step=1)
filtered_data = data[data["year"] == year]

# Calcola l'intensità globale delle emissioni
global_emission_intensity = filtered_data["emissioni"].sum()

# Creazione della sfera del globo
theta = []
phi = []
emission_colors = []

# Creazione della griglia sferica per il globo
for lat in range(-90, 91, 5):  # Passo di 5 gradi in latitudine
    for lon in range(-180, 181, 5):  # Passo di 5 gradi in longitudine
        theta.append(lon)
        phi.append(lat)
        emission_colors.append(global_emission_intensity)  # Valore uniforme per l'anno selezionato

# Normalizza i valori delle emissioni per colorazione
max_emission = data["emissioni"].sum()
colors = [(e / max_emission) for e in emission_colors]

# Crea la visualizzazione 3D
fig = go.Figure()

# Aggiungi la sfera come superficie
fig.add_trace(
    go.Mesh3d(
        x=[lon for lon in theta],
        y=[lat for lat in phi],
        z=[0 for _ in theta],
        intensity=colors,
        colorscale="Reds",  # Gradiente di colori (rosso per emissioni alte)
        opacity=0.7,
        showscale=True,
    )
)

# Configura il layout del globo
fig.update_layout(
    scene=dict(
        xaxis=dict(showbackground=False),
        yaxis=dict(showbackground=False),
        zaxis=dict(showbackground=False),
    ),
    title=f"Emissioni globali nel {year}",
)

# Mostra il globo 3D
st.plotly_chart(fig)
