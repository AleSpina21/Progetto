from sklearn.linear_model import LinearRegression
import streamlit as st
def final_dataset(df):
    eliminate_columns = [
         "binaryflag", "age", "discoverymethod", "discoveryyear", "lastupdate", "system_rightascension", "system_declination", "system_distance", "hoststar_age", "list"
    ]
    filtered_df = df.drop(columns=eliminate_columns)
    missing = filtered_df.isnull().mean() 
    drop_col = missing[missing >= 0.60].index
    df_final = filtered_df.drop(columns=drop_col)
    return df_final

def data_estimates(d):
    for target in d.columns:
        known = d[d[target].notna()]
        missing = d[d[target].isna()]

        x_train = known.drop(columns = [target])
        y_train = known[target]
        x_test = missing.drop(columns=[target])

        x_train = x_train.fillna(x_train.mean())
        x_test = x_test.fillna(x_train.mean())

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


