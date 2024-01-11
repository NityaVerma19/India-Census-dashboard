import streamlit as st
import pandas as pd
import numpy as np
import  plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title("India's Census")

selected_state = st.sidebar.selectbox('Select a state', list_of_states)

primary = st.sidebar.selectbox('Select primary parameter', ['Population','sex_ratio','Households_with_Internet'])
secondary = st.sidebar.selectbox('Select secondary parameter', ['Population','sex_ratio','Households_with_Internet'])

plot = st.sidebar.button('Plot graph')

if plot:

    st.text('Size represents primary parameter')
    st.text('Colour represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=4, mapbox_style='carto-positron', size = primary, color = secondary, height = 700, width= 1200, hover_name='District')
        st.plotly_chart(fig, use_container_width= True)
    else:
         state_df =df[df['State'] == selected_state]
         fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=4, mapbox_style='carto-positron',
                                size=primary, color=secondary, height=700, hover_name='District')
         st.plotly_chart(fig, use_container_width=True)


