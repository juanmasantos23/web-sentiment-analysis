import streamlit as st
import pandas as pd

st.title("Dashboard de prueba - Web Sentiment Analysis")

# Datos de ejemplo
data = {
    "Equipo": ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla"],
    "Puntos": [68, 64, 59, 55]
}

df = pd.DataFrame(data)

st.write("Tabla de ejemplo de la liga española:")
st.dataframe(df)

st.bar_chart(df.set_index("Equipo")["Puntos"])
