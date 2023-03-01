import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import sys
sys.path.append('/.../viz.py') 
import viz
import plotly.express as px 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import importlib
importlib.reload(viz)

st.set_page_config(
     page_title="Reseñas",
     page_icon="🚀",
     layout="wide",
)

df = pd.read_csv("data/lec_sent.csv")
df_stop = df.dropna(subset=['rev_es_0'])
df_pos = df_stop[df_stop["rev_en_0_compound"] > 0]
df_neg = df_stop[df_stop["rev_en_0_compound"] < 0]

st.header("De qué hablan los consumidores")

st.subheader("Palabras más repetidas en reseñas positivas:")

fig2 = viz.wordc(df_pos)
st.pyplot(fig2)

st.subheader("Palabras más repetidas en reseñas negativas:")

fig3 = viz.wordc(df_neg)
st.pyplot(fig3)
