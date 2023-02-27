import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import plotly.express as px


df = pd.read_csv("data/lekaroz.csv")


st.set_page_config(
     page_title="Lecaroz",
     layout="wide"
)



image = Image.open('images/logo.png')

st.image(image)
# Title
st.title("Análisis de Google reviews: panaderías Lecaroz")

st.subheader("Datos")
st.markdown('''
Los datos fueron escrapeados de Google Maps a través de una API. 
''')

#st.dataframe(df)

st.plotly_graph()

