import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
import pickle
from PIL import Image
import sys
sys.path.append('/.../viz.py') 
import viz
import plotly.express as px
from streamlit_folium import st_folium
import folium
import os
# get the current working directory
cwd = os.getcwd()

# # create the path to the file
# file_path = os.path.join(cwd, 'data', 'lec_sent.csv')

# # open the file
# with open(file_path, 'r') as f:
#     df = f.read()


df = pd.read_csv("/Users/narea/Desktop/panaderias/data/lec_sent.csv")


st.set_page_config(
     page_title="Mapa",
     layout="wide"
)

# Title
st.title("Análisis del rating de las panaderías Lecaroz")
st.subheader("Colores de los marcadores:")
st.markdown('''
- Verde clarito: 4.5-5 ⭐️
- Verde fuerte: 4.0-4.5 ⭐️
- Naranja: 3.5-4.0 ⭐️
- Rojo: < 3.5 ⭐️
''')

fig3 = viz.mapa(df)
st_folium(fig3)

df3 = df.nsmallest(10, 'totalScore')
df2 = df.nlargest(10, 'totalScore')
df3 = df3[["street", "totalScore"]]
df2 = df2[["street", "totalScore"]]


col1, col2 = st.columns(2)
col1.markdown("### Top 10 sucursales con mejor rating")
col1.dataframe(df2)

col2.markdown("### Top 10 sucursales con peor rating")
col2.dataframe(df3)

#st.dataframe(df2)

#st.dataframe(df3)
