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


"""
def imputare_con_regressione(df, col):
    # Convertiamo la colonna target in numerico, forzando i valori non numerici a diventare NaN
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Controlla quanti NaN ci sono nella colonna target
    print(f"Valori mancanti nella colonna {col}: {df[col].isna().sum()}")

    # Eseguiamo un'imputazione preliminare per la colonna target
    imputer_target = SimpleImputer(strategy='mean')  # Imputiamo i NaN con la media
    df[col] = imputer_target.fit_transform(df[[col]])
    
    # Selezioniamo le righe con valori validi nella colonna target
    train_data = df[df[col].notna()]
    if train_data.empty:
        raise ValueError(f"Non ci sono dati validi per la colonna {col} per eseguire la regressione.")
    
    # Selezioniamo le caratteristiche per la regressione (tutte le colonne tranne 'mass')
    X_train = train_data.drop(columns=[col])
    y_train = train_data[col]
    
    # Imputiamo i valori NaN nelle caratteristiche con la media (o mediana)
    imputer = SimpleImputer(strategy='mean')  # Puoi anche usare 'median' o 'most_frequent'
    X_train = imputer.fit_transform(X_train)
    
    # Creiamo il modello di regressione lineare
    model = LinearRegression()
    
    # Alleniamo il modello
    model.fit(X_train, y_train)
    
    # Ora stimiamo i valori per le righe con NaN nella colonna target
    test_data = df[df[col].isna()]
    if test_data.empty:
        print(f"Nessun valore mancante da imputare nella colonna {col}.")
        return df  # Se non ci sono valori mancanti da imputare, ritorniamo il dataframe originale
    
    X_test = test_data.drop(columns=[col])
    
    # Imputiamo i valori NaN nelle caratteristiche del test set
    X_test = imputer.transform(X_test)
    
    # Prediciamo i valori mancanti
    predictions = model.predict(X_test)
    
    # Imputiamo i valori stimati nel dataframe
    df.loc[df[col].isna(), col] = predictions
    
    
    return df
"""