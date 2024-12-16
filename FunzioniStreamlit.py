import streamlit as st
import pandas as pd
import pydeck as pdk

# Creo la mappa con i telescopi
def create_map(telescope_data=None):
    df = pd.read_csv("telescopi.csv")
    deck = pdk.Deck(
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position=["Longitudine", "Latitudine"],
                get_color=[255, 0, 0, 255],
                get_radius=50000,
            )
        ],
        initial_view_state=pdk.ViewState(
            longitude=telescope_data["Longitudine"] if telescope_data is not None else 0,
            latitude=telescope_data["Latitudine"] if telescope_data is not None else 0,
            zoom=3
        ),
        map_style="mapbox://styles/mapbox/satellite-v9",  
    )

    st.pydeck_chart(deck)

def final_map():
    df = pd.read_csv("telescopi.csv")
    st.subheader("Lista dei Telescopi")
    selected_telescopio = st.selectbox("Seleziona un telescopio:", df["Nome"], key = "selectbox_telescopio")
    selected_telescopio_data = df[df["Nome"] == selected_telescopio].iloc[0]  
    create_map(selected_telescopio_data)

    st.subheader(f"Informazioni su: {selected_telescopio}")
    st.write(f"**Tipo:** {selected_telescopio_data['Tipo']}")
    st.write(f"**Anno di costruzione:** {selected_telescopio_data['Anno']}")
    st.write(f"**Caratteristiche:** {selected_telescopio_data['Caratteristiche']}")


def add_telescope():
    st.subheader("Aggiungi un telescopio nuovo")
    st.write("Sei un ricercatore? Vuoi aggiungere un telescopio? Inserisci la tua email, se sarai verificato ti sarà possibile aggiungere un telescopio alla lista!")
    email = st.text_input("Inserisci la tua email istituzionale: ")
    
    if email.endswith("@unipd.it"):
        st.success("Verifica andata a buon fine!")
        st.write("Aggiungi il tuo telescopio: ")
        nome = st.text_input("Nome del telescopio:")
        tipo = st.text_input("Tipo di telescopio:")
        anno = st.number_input("Anno di costruzione:", min_value=1900, max_value=2024)
        caratteristiche = st.text_area("Caratteristiche del telescopio:")
        longitudine = st.number_input("Longitudine:", format="%.6f")
        latitudine = st.number_input("Latitudine:", format="%.6f")
        if st.button("Aggiungi telescopio"):
            new_telescopio = pd.DataFrame({
                "Nome": [nome],
                "Tipo": [tipo],
                "Anno": [anno],
                "Caratteristiche": [caratteristiche],
                "Longitudine": [longitudine],
                "Latitudine": [latitudine]
            })
            df = pd.read_csv("telescopi.csv")
            df = pd.concat([df, new_telescopio], ignore_index=True)
            df.to_csv("telescopi.csv", index=False)
            st.success(f"Il telescopio '{nome}' è stato aggiunto con successo!")
    else:
        st.error("Non ti è possibile aggiungere telescopi.")









































