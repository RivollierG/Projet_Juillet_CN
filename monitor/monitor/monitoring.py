from sqlalchemy import create_engine
import datetime
import time
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


engine = create_engine("postgresql+psycopg2://wym_admin:admin@db:5432/postgres", echo=False)
data = pd.read_sql("select * from texts", engine)
data['length'] = [len(i.split()) for i in data.contenu]
data['length_res'] = [len(i.split()) for i in data.resume]
data['ratio'] = data.length_res / data.length

image = 'https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80'

bool1 = st.sidebar.checkbox('Show dataframe')
bool2 = st.sidebar.checkbox('Show metrics')
bool3 = st.sidebar.checkbox('Show date selection')
bool4 = st.sidebar.checkbox('Show mountain picture')
bool5 = st.sidebar.checkbox('Show picture selection')
bool6 = st.sidebar.checkbox('Show map')
bool7 = st.sidebar.checkbox('Show awesome video')
st.title("GuiLoSoRe's dashboard")

if bool1:
    st.header('**Dataframe :**')
    data

if bool2:
    st.header('**Metrics :**')    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Nombre de résumés dans la base : ", value=data.shape[0])
    col2.metric(label="Nombre moyen de mots du texte à résumer : ", value=data.length.mean())
    col3.metric(label="Nombre moyen de mots du résumé : ", value=data.length_res.mean())
    col4.metric(label="Indice moyen de contraction de la summerisation : ", value=round(data.ratio.mean(),2))

if bool3:
    st.header('**Shorten dataframe :**')    
    date1 = st.date_input("select a date",datetime.date(2022, 7, 8))
    date2 = date1 + datetime.timedelta(days=1)
    st.write('**Dataframe du jour:**')
    data[((data['date']) >= np.datetime64(date1)) & (data['date'] < np.datetime64(date2))]

if bool4 or bool5 : 
    st.header('**Pictures :**')

if bool4:
    st.subheader('**Mountain picture :**')    
    st.image(image, caption='Sunrise by the mountains')

if bool5:
    st.subheader('**Chosen picture :**')       
    pict_selected = st.selectbox(
        'Which picture do you want to display?',
        ('kitten', 'dog', 'minion', 'mountain', 'aucune')
    )
    # st.write(pict_selected)
    if pict_selected == 'kitten' : 
        img = "https://media.gettyimages.com/photos/kitten-on-lap-picture-id138468381?s=2048x2048"
        capt = "teletravail"
    elif pict_selected == 'dog':
        img = "https://media.gettyimages.com/photos/-picture-id10100201?s=2048x2048"
        capt = "tigers"
    elif pict_selected == 'minion':
        img = "https://musicart.xboxlive.com/6/cfaf1e9e-0000-0000-0000-000000000009/504/image.jpg?w=1920&h=1080"
        capt = "kevin aux açores"
    elif pict_selected == 'mountain':
        img = 'https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80'
        capt = 'Sunrise by the mountains'
    else:
        capt = "error"
        img = ""
    try:
        st.image(img, caption=capt)
    except FileNotFoundError:
        st.write("error")

if bool6:
    st.header('**Map :**')
    map_data = pd.DataFrame(
        np.random.randn(10, 2) / [500, 500] + [45.185, 5.731],
        columns=['lat', 'lon'])

    st.map(map_data, zoom=11)

if bool7:
    st.header('Awesome video :')
    st.video("https://www.youtube.com/watch?v=UN4DaSAZel4&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5")

