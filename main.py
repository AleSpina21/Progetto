import pandas as pd
import streamlit as st
import FunzioniStreamlit as FS
import PlanetFunctions as PF
import numpy as np
import Archeology as AR
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


## DA FARE: STATISTICHE E GRAFICI SU QUESTE
## OCCHIO ALLE DEPENDENCIES 

url = "open_exoplanet_catalogue.txt" # prendo i dati da questo file che verrà aggiornato ogni volta che un nuovo esopianeta verrà scoperto.
df = pd.read_csv(url, delimiter=",", index_col=0)
df = df.fillna("NA")  # ci sono dei valori mancanti, li ho riscritti con NA
df.replace("NA", np.nan, inplace=True) # Forzo la numericità nei NA




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
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(
            "https://selbst-management.biz/wp-content/uploads/2013/10/albert-einstein.jpg", 
            caption="Albert Einstein", 
            width=150
        )
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
    FS.plot_detection_methods(df)
    st.write("Dal 2013 si nota un importante aumento nelle rilevazioni, soprattutto attraverso il metodo si transizione, questo è dovuto al fatto che nel 2009 la NASA ha iniziato la missione KEPLER. La missione, durata quasi 10 anni "
             "aveva come obiettivo quello di scoprire esopianeti e in particolare quelli che potenzialmente potrebbero ospitare vita extraterrestre.")
    st.subheader("Ci sono esopianeti abitabili?")
    st.write("Per trovare i pianeti abitabili abbiamo bisogno di tutte le caratterstiche degli esopianeti, ma il dataset iniziale riporta moltissimi valori mancanti e ciò limita le analisi che si possono fare. Per risolvere questo problema sarà necessario stimare i valori mancanti. Si inizia con la pulizia del dataset, "
             "togliendo colonne non significative per le analisi d'interesse e le colonne che presentano almeno il 90 per cento di valori mancanti, poiché indica una variabile di poco interesse. Facende le analisi risulta il dataset seguente (prime 20 righe):")
    st.dataframe(PF.final_dataset(df).head(20))
    df1 = PF.final_dataset(df)
    df1 = df1.apply(pd.to_numeric, errors = "coerce")
    st.write("A questo punto manca stimare gli elementi mancanti. Operando una regressione si ottiene il dataset (prime 20 righe)")
    df2 = PF.data_estimates(df1)
    st.dataframe(df2.head(20))
    st.write("ATTENZIONE queste stime sono state fatte attraverso un modello di regressione LINEARE, perciò non sono scientificamente approvate. Inoltre, valori negativi sono possibili, in quanto sono in confronto a valori di alcuni corpi del Sistema Solare (es. Terra, Giove, Sole).")
    st.write("")
    st.write("")
    st.write("Ora possiamo trovare i pianeti potenzialmente abitabili: Stanno in un determinato raggio dalla loro stella, hanno una certa massa e la loro stella deve avere una certa temperatura:")
    df_habit = PF.habitable(df2)
    names = df_habit.index.tolist()
    for name in names:
        st.write(name)
    st.write("Ovviamente, ci sono tantissimi altri fattori da tenere in considerazione, ma questo è solo un algoritmo iniziale, se si rilevano altri fattori importanti basta aggiungerli.")
    st.write("")
    st.write("")
    
elif selezione == "Satelliti":
    st.title("Satelliti")
    st.write("Il mondo dei satelliti è affascinante, contribuiscono sia alla conoscenza dello spazio che allo studio approfondito della Terra.")
    st.subheader("Utilizzo in Archeologia")
    st.write("Un utilizzo molto affascinante della mappatura satellitare è in archeologia, in particolare per la scoperta di segni di civiltà perdute. Negli ultimi 30 anni questo è un metodo molto utilizzato nel settore. I metodi più utilizzati sono le immagini a infrarosso, radar o il LiDAR (Light Detection and Ranging), che penetra il fogliame per mappare la topografia del terreno e rivelare resti nascosti. "
             "Un esempio interessante sono le piramidi Maya in Messico, ancora oggi, attraverso immagini satellitari, si stanno scoprendo sempre più strutture antiche create dai nostri antenati e un modo efficace è usare le immagini radar: ")
    Piramide_Uxmal = "PiramideUxmal.png"
    image = AR.load_image_gray(Piramide_Uxmal)
    view_option = st.radio("Seleziona la modalità di visualizzazione:",["Vista normale", "Vista radar"])
    if view_option == "Vista normale":
        st.write("### Vista normale")
        fig, ax = plt.subplots()
        ax.imshow(image, cmap='gray')  # Mostra l'immagine in scala di grigi, perché se no usciva brutto.
        ax.set_title("Gran Piramide di Uxmal: Originale")
        st.pyplot(fig)
    elif view_option == "Vista radar":
        st.write("### Vista radar")
        radar_view = gaussian_filter(image, sigma=10)
        fig, ax = plt.subplots()
        ax.imshow(radar_view, cmap='inferno')  # Mostra l'immagine con il filtro radar
        ax.set_title("Gran Piramide di Uxmal: Radar")
        st.pyplot(fig)
    st.write("Le aree con colori più intensi nella vista radar rappresentano potenziali strutture artificiali, come piramidi o altre costruzioni. In un'analisi reale, si trovano algoritmi molto più complessi per la rilevazione anche di dati sotterranei.")
    st.title('Analisi delle Strutture Archeologiche con Immagini Satellitari')

    Piramide_Maya = "PiramideMaya.png" 
    image = AR.load_image(Piramide_Maya)  # ATTENZIONE PROVO AD USARE UNA E UNA SOLA FUNZIONE DI CARICAMENTO D'IMMAGINI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    st.image(image, caption="Immagine Satellitare Caricata", use_container_width=True)
    
    analysis_method = st.selectbox("Scegli il metodo di analisi", 
                                   ["Seleziona un metodo", "Edge Detection", "NDVI", "Texture Analysis"])
    
    if analysis_method == "Edge Detection":
        st.write("""
        **Rilevamento dei Bordi (Edge Detection)**:
        Questo metodo utilizza l'algoritmo di Canny per rilevare i bordi dell'immagine. 
        È utile per identificare strutture geometriche o schemi nel terreno che potrebbero suggerire la presenza di strutture sotterranee o anomalie nel paesaggio.
        """)
        edges = AR.edge_detection(image)
        AR.visualize_results(image, edges=edges)

    elif analysis_method == "NDVI":
        st.write("""
        **Indice di Vegetazione (NDVI)**:
        L'NDVI è un indice che misura la salute della vegetazione utilizzando i canali rosso e verde dell'immagine. 
        Un valore elevato di NDVI indica una vegetazione sana, mentre un valore più basso può suggerire anomalie nel terreno, come la presenza di strutture sotterranee.
        """)
        ndvi = AR.compute_ndvi(image)
        AR.visualize_results(image, ndvi=ndvi)

    elif analysis_method == "Texture Analysis":
        st.write("""
        **Analisi della Texture (LBP - Local Binary Patterns)**:
        Questa tecnica esamina la texture dell'immagine, cercando schemi di intensità locali che potrebbero essere associati a strutture o modifiche nel terreno. 
        LBP è utile per distinguere tra aree naturali e potenziali strutture nascoste.
        """)
        lbp = AR.texture_analysis(image)
        AR.visualize_results(image, lbp=lbp)



