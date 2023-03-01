import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import viz
import plotly.express as px 

st.set_page_config(
     page_title="Sentimiento",
     page_icon="🚀",
     layout="wide",
)

df = pd.read_csv("data/lec_sent.csv")


st.header("Análisis del sentimiento de las reseñas de Google")
st.markdown('''
"Avg. compund" es un valor que va de -1 al 1 que mide la positividad o negatividad de las reseñas de Google. En la gráfica se ve
este valor junto con el rating y el ranking.''')


fig2 = viz.tres_d(df)
st.plotly_chart(fig2, use_container_width=True)





