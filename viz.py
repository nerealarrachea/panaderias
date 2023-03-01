# importing libraries
import pandas as pd
import folium
import plotly.express as px
import types
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import warnings
warnings.filterwarnings("ignore")

def mapa(df2):
    ''' creates a map centered at Mexico using folium,
    add markers for each location using the latitude and longitude data
    and displays the map '''
    mexico_map = folium.Map(location=[23.6345, -102.5528], zoom_start=5)
    for i in range(0,df2.shape[0]):
        if pd.notnull(df2['totalScore'][i]): # check if totalScore is not null
            if df2['totalScore'][i] >= 4.5:
                icon = 'lightgreen'
            elif df2['totalScore'][i] >= 4.0:
                icon = 'green'
            elif df2['totalScore'][i] >= 3.5:
                icon = 'orange'
            elif df2['totalScore'][i] <= 3.5 and df2['totalScore'][i] > 0:
                icon = 'red'
            folium.Marker(location=[df2["location/lat"][i], df2["location/lng"][i]],
                      popup=[df2["totalScore"][i],df2["street"][i]],
                      icon= folium.Icon(color=icon, icon_color='white',icon = 'shopping-cart')
                     ).add_to(mexico_map)
    return mexico_map


def tres_d(df2):
    fig = px.scatter_3d(df2, x='rank', y='avg_compound', z='totalScore', hover_name='street', color = 'city')
    fig.update_layout(title='Análisis de las reviews obtenidas en Google para diferentes zonas')
    return fig

def ocupacion(df):
    fig = px.bar(df,x = range(5,22), y = df["Av. Henry Ford 25"])
    fig.update_xaxes(title='Horas')
    fig.update_layout(title='Ocupación de la panadería por horas del día')
    return fig

def pie(df2):
    # count the number of True and False values
    true_count = df2['additionalInfo/Accessibility/0/Wheelchair accessible entrance'].value_counts()[True]
    false_count = df2['additionalInfo/Accessibility/0/Wheelchair accessible entrance'].value_counts()[False]
    nans = df2['additionalInfo/Accessibility/0/Wheelchair accessible entrance'].isna().sum()

    # create the pie chart
    fig = px.pie(df2, values=[true_count, false_count, nans], names=['Accesible para personas en silla de ruedas', 
                                                                'No accesible para personas en silla de ruedas', 
                                                                'Sin información'], hole=0.55, 
                 )

    # add hover data
    fig.update_traces(hoverinfo="label+value", textinfo='percent+label')
    fig.update_layout(title='Porcentaje de accesibilidad')

    return fig

def wordc(df):
    nltk.download('stopwords')
    # Load Spanish stopwords
    spanish_stopwords = set(stopwords.words('spanish'))

    # Add additional custom stopwords
    custom_stopwords = {"los", "las", "el", "la", "de", "en", "y", "si", "pan"}

    # Combine all stopwords
    stop = STOPWORDS.union(spanish_stopwords, custom_stopwords)

    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop, 
                min_font_size = 10).generate(' '.join(df['rev_es_0']))

    # plot wordcloud
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    return plt