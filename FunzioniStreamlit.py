import streamlit as st
import pandas as pd
import pydeck as pdk  # libreria python per la visualizzazione interattiva di dati geospaziali

# Crea la mappa con i telescopi
# Deck crea l'immagine della mappa, ci metto tutte le caratteristiche di cui ho bisogno: 
# Layer mi specifica i livelli dell'immagine, in questo caso usiamo un layer di tipo ScatterplotLayer.
# Initial_view_stat mi indica quale sarà la visualizzazione iniziale (usa ViewState), lo zoom l'ho messo per comodità
# Map_style specifica lo stile della mappa, io ho voluto uno stile satellitare tramite Mapbox.
def create_map(telescope_data, df):
    color = {
        "Radio":[0, 255, 0, 255], # la scala di colori è [rosso verde blu opacità]
        "Ottico":[0, 0, 255, 255],
        "Solar": [255, 0, 0, 255]
    }
    df["color"] = df["Tipo"].map(color) # aggiungo color e lo attribuisco in base al tipo
    deck = pdk.Deck(
        layers=[pdk.Layer(
                "ScatterplotLayer",
                data=df, # dati che mi interessano
                get_position=["Longitudine", "Latitudine"], # metterò la posizione in base a lat e long
                get_color="color", 
                get_radius=90000,)
                ],
        initial_view_state=pdk.ViewState(
                longitude=telescope_data["Longitudine"] if telescope_data is not None else 0,
                latitude=telescope_data["Latitudine"] if telescope_data is not None else 0, # if telescope_data is not None else 0 è utile nel momento in cui non ci sono i dati a disposizione, in questo caso la mappa sarà centrata in (0,0), anche se nn sarà questo il caso
                zoom=3),
        map_style="mapbox://styles/mapbox/satellite-v9",  
    )

    st.pydeck_chart(deck) # visibile con streamlit


def get_color(tipo):
    if tipo.lower() == "ottico":
        return "[0, 0, 255, 255]"  # Blu per telescopi ottici
    elif tipo.lower() == "radio":
        return "[0, 255, 0, 255]"  # Verde per telescopi radio
    elif tipo.lower() == "solar":
        return "[255, 0, 0, 255]"  # Rosso per telescopi solari
    else:
        return "[255, 255, 255, 255]"  # Bianco per altri tipi di telescopi (predefinito)


# FUnzione che permette di inserire un telescopio se fai parte di Unipd, inoltre il telescopio comparirà nella mappa.
# Se appartiene ad Unipd, prosegue. Ti fa inserire tutte le caratteristiche necessarie e crea un dataset con quelle informazioni.
# concatena il nuovo dataset del telescopio con il dataset di tutti i telescopi.
def add_telescope(df):
    st.subheader("Aggiungi un telescopio nuovo")
    st.write("Sei un ricercatore? Vuoi aggiungere un telescopio? Inserisci la tua email, se sarai verificato ti sarà possibile aggiungere un telescopio alla lista!")
    email = st.text_input("Inserisci la tua email istituzionale: ")
    
    if email.endswith("@unipd.it"):
        st.success("Verifica andata a buon fine!") # scrittura evidenziata in verde, carino
        st.write("Aggiungi il tuo telescopio: ")
        nome = st.text_input("Nome del telescopio:")
        tipo = st.text_input("Tipo di telescopio:")
        anno = st.number_input("Anno di costruzione:", min_value=1900, max_value=2024)
        caratteristiche = st.text_area("Caratteristiche del telescopio:")
        longitudine = st.number_input("Longitudine(se è Ovest, mettere un valore negativo):", format="%.6f") # formatto 6 cifre dopo il puntino, questo è il formatto usato di solito per le longitudini e latitudini
        latitudine = st.number_input("Latitudine (se è Sud, mettere un valore negativo):", format="%.6f")
        image = st.text_input("L'URL dell'immagine del telescopio:") ### Chiediamo vari input all'utente
        if st.button("Aggiungi telescopio"): # quando clicca, viene creato il subdataframe
            color = get_color(tipo)
            new_telescopio = pd.DataFrame({
                "Nome": [nome],
                "Tipo": [tipo],
                "Anno": [anno],
                "Caratteristiche": [caratteristiche],
                "Longitudine": [longitudine],
                "Latitudine": [latitudine],
                "color": [color],
                "image" : [image]
            })
            df = pd.concat([df, new_telescopio], ignore_index=True) # concatenazione
            df.to_csv("telescopi.csv", index=False) # aggiurno il dataset originale
            st.success(f"Il telescopio '{nome}' è stato aggiunto con successo!") # figo aggiungere questo per bellezza
    else:
        st.error("Non ti è possibile aggiungere telescopi.")


