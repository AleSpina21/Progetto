from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
import PlanetFunctions as PF
import pandas as pd
import streamlit as st
import numpy as np
url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/oec_tables/refs/heads/master/comma_separated/open_exoplanet_catalogue.txt" # prendo i dati da questo file che verrà aggiornato ogni volta che un nuovo esopianeta verrà scoperto.
df = pd.read_csv(url, delimiter=",", index_col=0)
df = df.fillna("NA")
df.replace("NA", np.nan, inplace=True)
d = PF.final_dataset(df)
def imputer(d):
    knn_imputer = KNNImputer(n_neighbors=3, weights="uniform")
    df_KNN = st.dataframe(knn_imputer.fit_transform(d))
    return df_KNN
