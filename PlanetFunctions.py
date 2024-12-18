import altair as alt
import streamlit as st
from sklearn.linear_model import LinearRegression


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
    return d