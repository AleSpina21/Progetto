import pandas as pd
import plotly.graph_objects as go
from planet import Planet

url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/oec_tables/refs/heads/master/comma_separated/open_exoplanet_catalogue.txt"
df = pd.read_csv(url, delimiter=",")

class PlanetGraphs:
    def __init__(self, planet: Planet):
        self.planet = planet

    ### Questo istogramma rileva quanti esopianeti sono stati scoperti in base al metodo di rilevazione utilizzato. Innanzitutto vado a prendere tutti i metodi usati e li conto, poi nel grafico prendo gli indici, ovvero i nomi, e li metto nell'ascisse, 
    # poi prendo il numero di rilevazioni fatti per metodo (ovvero i values) e lo metto nelle ordinate. Creo il grafico con colonne blu per quante colonne ci sono in tutto. Mostro il grafico con il titolo scelto.
    def detectionsGraph(self):
        conteggio_metodi_generale = df["discoverymethod"].value_counts()
        fig = go.Figure(
            data=[go.Bar(x = conteggio_metodi_generale.index, y=conteggio_metodi_generale.values, marker=dict(color=["blue"]*len(conteggio_metodi_generale)))],
            layout_title_text="Numero di rilevazioni per metodo di rilevazione"
        )
        fig.show()

    ### Questo grafico ritorna il numero di rivelazioni per metodo di rilevazione in base al tipo di pianeta che interessa all'utente. IL tipo di pianeta me lo dà l'utente (L'ho definito nel main), conto i metodi di rilevazione in base al pianeta tipo scelto, 
    # sulle ordinate metto il nome dei metodi e sulle ascisse metto il numero di rilevazioni. Voglio colonne di colore blu tante quante sono i metodi di rilevazione. Mostro il grafico con il titolo scelto che richiama anche il tipo di pianeta.
    def ExoplanetTypeDetections(self, planet_type):  
        conteggio_metodi = df.loc[(df.planet_type == planet_type), ["detection_method"]].detection_method.value_counts()
        fig = go.Figure(
            data=[go.Bar(x = conteggio_metodi.index, y=conteggio_metodi.values, marker=dict(color=["blue"]*len(conteggio_metodi)))],
            layout_title_text=f"Numero di rilevazioni di esopianeti di tipo {planet_type} per metodo di rilevazione"
            )
        fig.show()

    ### Questo grafico a torta mostra la percentuale di esopianeti con massa simile a pianeti del Sistema Solare. Conto quanti sono tutti i pianeti con massa simile ad un pianeta del sistema solare e ogni fetta sarà nominata con il pianeta del sistema solare che rappresenta, 
    # mentre la grandezza della fetta sarà rappresentata dalla quantità di esopianeti con massa simile. Imposto i colori rosso e blu. Mostro il grafico con il titolo scelto.
    def massWrtGraphs(self):
        conteggio_massa= df.mass_wrt.value_counts()
        fig = go.Figure(
        data=[go.Pie(labels= conteggio_massa.index, values=conteggio_massa.values, marker=dict(colors=["red", "blue"]))],
        layout_title_text="Percentuali di pianeti con massa simile ad un pianeta del Sistema Solare"
        )
        fig.show()
