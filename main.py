import pandas as pd
import streamlit as st
import FunzioniStreamlit as FS
import PlanetFunctions as PF
## DA FARE: STATISTICHE E GRAFICI SU QUESTE

url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/oec_tables/refs/heads/master/comma_separated/open_exoplanet_catalogue.txt" # prendo i dati da questo file che verrà aggiornato ogni volta che un nuovo esopianeta verrà scoperto.
df = pd.read_csv(url, delimiter=",", index_col=0)
df = df.fillna("NA")  # ci sono dei valori mancanti, li ho riscritti con NA


st.sidebar.title("Cosa cerchi?")
selezione = st.sidebar.radio("vai a:", ["Cos'è l'Astronomia?","Telescopi", "Esopianeti", "Satelliti"])

if selezione == "Cos'è l'Astronomia?":
    st.image("https://www.astronomy.com/uploads/2023/09/Astronomy-Home-Page-Image.png")
    st.title("Astroworld")
    st.subheader("Piattaforma di ricerca astronomica")
    st.text("L'astronomia è la scienza naturale che si occupa dell'osservazione e della spiegazione degli eventi celesti che si verificano nello spazio." 
        " Studia le origini e l'evoluzione, le proprietà fisiche, chimiche e temporali degli oggetti che formano l'universo e che possono essere osservati sulla sfera celeste." 
        " È una delle scienze più antiche e molte civiltà arcaiche in tutto il mondo hanno studiato in modo più o meno sistematico il cielo e gli eventi astronomici: egizi e greci nell'area mediterranea," 
        " babilonesi, indiani e cinesi nell'Oriente e infine i maya e gli incas nelle Americhe. Questi antichi studi astronomici erano orientati verso lo studio delle posizioni degli astri (astrometria),"
        " la periodicità degli eventi e la cosmologia e quindi, in particolare per questo ultimo aspetto, l'astronomia antica è quasi sempre fortemente collegata con aspetti religiosi e di divinazione aspetti" 
        " nei tempi passati ritenuti importanti e strategici. Nel ventunesimo secolo, invece, la ricerca astronomica moderna è praticamente sinonimo di astrofisica. L'astronomia non va confusa con l'astrologia," 
        " una pseudoscienza che sostiene che i moti apparenti del Sole e dei pianeti nello zodiaco influenzino in qualche modo gli eventi umani, personali e collettivi. Anche se le due discipline hanno un'origine" 
        " comune e per secoli accomunate, esse sono oggi totalmente differenti: gli astronomi hanno abbracciato il metodo scientifico sin dai tempi di Galileo, a differenza degli astrologi. L'astronomia è una delle" 
        " poche scienze in cui il lavoro di ricerca del dilettante e dell'amatore (l'astrofilo) può giocare un ruolo rilevante, fornendo dati sulle stelle variabili o scoprendo comete, nove, supernove, asteroidi o altri oggetti.")
    YT_url = "https://www.youtube.com/watch?v=ujg8lsjdqT0"
    st.video(YT_url)

    col1, col2 = st.columns([1, 3])  # Puoi modificare la larghezza delle colonne

# Colonna con la foto
    with col1:
        st.image(
            "https://selbst-management.biz/wp-content/uploads/2013/10/albert-einstein.jpg", 
            caption="Albert Einstein", 
            width=150
        )

    # Colonna con la citazione
    with col2:
        st.markdown("> **“L'immaginazione è più importante della conoscenza.”** – Albert Einstein, un normalissimo Fisico")

elif selezione == "Telescopi":
    st.title("Telescopi")
    FS.final_map()
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
 
    FS.add_telescope()
    
elif selezione == "Esopianeti":
    st.title("Esopianeti")
    st.subheader("Metodi di rilevazione")
    st.write("I metodi di individuazione di pianeti extrasolari sono diversi e si sono evoluti nel corso degli anni, permettendo oggi di scoprire nuovi pianeti a un ritmo sempre crescente. Le metodologie si possono dividere in due classi principali: "
             "rilevamento diretto e rilevamento indiretto. Nella classe del rilevamento diretto si includono tutte le tecniche che permettono di osservare direttamente al telescopio questi pianeti. "
             "Nella classe del rilevamento indiretto ricadono quelle tecniche che permettono di individuare un pianeta a partire dagli effetti che esso induce (o vengono indotti) sulla (o dalla) stella ospite. "
             "Per confermare un pianeta e meglio definirne le caratteristiche fisiche è necessario l'utilizzo di più tecniche differenti. Al momento attuale la tecnica di maggior successo è quella del transito. "
             "I primi risultati sono stati ottenuto con il metodo delle velocità radiali. Sono stati scoperti attualmente (2023) più di 5000 pianeti extrasolari. "
             "Già nel 1955 Otto Struve aveva prospettato la possibilità di scoprire sistemi planetari extrasolari proprio con il metodo del transito e delle velocità radiali.")
    PF.plot_detection_methods(df)
    st.write("Dal 2013 si nota un importante aumento nelle rilevazioni, soprattutto attraverso il metodo si transizione, questo è dovuto al fatto che nel 2009 la NASA ha iniziato la missione KEPLER. La missione, durata quasi 10 anni "
             "aveva come obiettivo quello di scoprire esopianeti e in particolare quelli che potenzialmente potrebbero ospitare vita extraterrestre.")
    st.subheader("Ci sono esopianeti abitabili?")
    st.write("Per trovare i pianeti abitabili abbiamo bisogno di tutte le caratterstiche degli esopianeti, ma il dataset iniziale riporta moltissimi valori mancanti e ciò limita le analisi che si possono fare. Per risolvere questo problema sarà necessario stimare i valori mancanti. Si inizia con la pulizia del dataset, "
             "togliendo colonne non significative per le analisi d'interesse e le colonne che presentano almeno il 90 per cento di valori mancanti, poiché indica una variabile di poco interesse. Facende le analisi risulta il dataset seguente (prime 20 righe):")
    st.dataframe(PF.final_dataset(df).head(20))
    st.write("A questo punto manca stimare gli elementi mancanti. Operando una non so cosa si ottiene ")
    
elif selezione == "Satelliti":
    st.title("Satelliti")
    st.write("Il mondo dei satelliti è affascinante, contribuiscono sia alla conoscenza dello spazio che allo studio approfondito dell'atmosfera terrestre o della crosta terrestre.")





































