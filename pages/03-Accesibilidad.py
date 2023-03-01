import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import viz
import plotly.express as px 

# st.video('https://youtu.be/FVsvrFAWDTM') 

st.set_page_config(
     page_title="Accesibilidad",
     page_icon="🚀",
     layout="wide",
)


df = pd.read_csv("data/lec_sent.csv")


st.header("Accesibilidad para personas en silla de ruedas")

fig2 = viz.pie(df)
st.plotly_chart(fig2, use_container_width=True)
