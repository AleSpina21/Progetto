from sklearn.linear_model import LinearRegression
import streamlit as st

# Funzione per la creazione del dataset che serve per le analisi.
# Tolgo colonne qualitative
# Tolgo colonne che hanno il 60% di valori mancanti (insignificanti), questo anche per non appensantire il modello e evitare multicollinearità
def final_dataset(df):
    eliminate_columns = [
         "binaryflag", "age", "discoverymethod", "discoveryyear", "lastupdate", "system_rightascension", "system_declination", "system_distance", "hoststar_age", "list"
    ]
    filtered_df = df.drop(columns=eliminate_columns)
    missing = filtered_df.isnull().mean() 
    drop_col = missing[missing >= 0.60].index # index mi restituisce il nome delle colonne, mi serve quello per filtrare dopo
    df_final = filtered_df.drop(columns=drop_col)
    return df_final

# Funzione che utilizza un modello di regressione lineare per stimare i valori mancanti del dataset.
# Prende di riferimento una colonna target, prende le righe in cui i valori della colonna sono nulli e le righr in cui non sono nulli.
# x_train: Tutte le colonne tranne il target in cui però ci sono i valori presenti nel target.
# y_train: I valori non nulli nella colonna target.
# Il modello userà questi per allenare il modello che poi userà per stimare i valori mancanti
# x_test: prendendo le righe dove target è nullo, prende tutte le altre colonne
# Con la funzione LinearRegression() creiamo il modello e lo modelliamo sui valori train (quindi dove abbiamo effettivamente i valori nel target), ora si avrà un modello allenato.
# Usiamo il modello allenato e gli facciamo fare le previsioni tramite la finzione predict() sui dati x_test
# Mettiamo in d i valori mancanti
# contiamo i valori mancanti
def data_estimates(d):
    for target in d.columns:
        known = d[d[target].notna()]
        missing = d[d[target].isna()]

        x_train = known.drop(columns = [target])
        y_train = known[target]

        x_test = missing.drop(columns=[target])

        x_train = x_train.fillna(x_train.mean())
        x_test = x_test.fillna(x_train.mean()) # qui semplicemente evitiamo il problema di valori nulli mettendoci le medie

        model = LinearRegression()
        model.fit(x_train, y_train)

        predict = model.predict(x_test)

        d.loc[d[target].isna(), target] = predict 
    count_na = d.isna().sum()
    total = count_na.sum()
    st.write(f"Il dataset ha {total} valori mancanti!")
    return d

# funzione che dice se un esopianeta è abitabile o meno, ovvero se valgono le condizioni:
#  distanza dalla stella, massa, temperatura della stella
def habitable(d):
    distance_min = 0.95
    distance_max = 1.05
    mass_min = 0.9
    mass_max = 1.2
    temp_star_min = 4800
    temp_star_max = 6300

    habitables = d[
        (d["mass"] >= mass_min) & (d["mass"] <= mass_max) &
        (d["semimajoraxis"] >= distance_min) & (d["semimajoraxis"] <= distance_max) &
        (d["hoststar_temperature"] >= temp_star_min) & (d["hoststar_temperature"] <= temp_star_max)
    ]
    
    return habitables


