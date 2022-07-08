from sqlalchemy import create_engine
import datetime
import time
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

engine = create_engine("postgresql+psycopg2://wym_admin:admin@localhost:5432/postgres", echo=False)
data = pd.read_sql("select * from texts", engine)
data['length'] = [len(i.split()) for i in data.contenu]
data['length_res'] = [len(i.split()) for i in data.resume]
data['ratio'] = data.length_res / data.length

st.write('**Dataframe :**')
data

d = st.date_input(
     "select a date",
     datetime.date(2022, 7, 6))
st.write('selected date is:', d)

st.write('**Dataframe du jour:**')
data[datetime.datetime(data.date) == datetime.datetime(d)]


image = 'https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80'
st.image(image, caption='Sunrise by the mountains')

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Nombre de résumés dans la base : ", value=data.shape[0])
col2.metric(label="Nombre moyen de mots du texte à résumer : ", value=data.length.mean())
col3.metric(label="Nombre moyen de mots du résumé : ", value=data.length_res.mean())
col4.metric(label="Indice moyen de contraction de la summerisation : ", value=round(data.ratio.mean(),2))

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")