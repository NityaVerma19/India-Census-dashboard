import streamlit as st
import pandas as pd
import  plotly.express as px

st.set_page_config(layout='wide',page_icon= '🗺️', page_title= "Analysis")

df = pd.read_csv('India_census.csv')

df.rename(columns = {'Male_Literate' : 'Male literacy', 'Female_Literate' : 'Female Literacy', 'Households_with_Internet' : 'Households with internet', 'Housholds_with_Electric_Lighting': 'Households with electricity', 'sex_ratio': 'Sex Ratio', 'literacy_rate': 'literacy Rate'} , inplace = True)

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')
param = sorted(list(df.columns[5:]))

button = st.button("Learn More", type="primary")
if button:
    st.title("Analysis of India's Census data")
    st.divider()
    st.subheader("DESCRIPTION")
    st.write("A district wise analysis of India's data collected from Census 2011")
    st.divider()
    st.subheader("DATA")
    st.dataframe(df.head())
    st.caption('A preview of the data')
    st.divider()
    st.write('This dataset is made using two datasets')
    st.markdown("""
            > Dataset link - [Census data]("https://www.kaggle.com/datasets/danofer/india-census?select=india-districts-census-2011.csv")
            """)
    st.markdown("""
                > Dataset link - [Indian Census Data with Geospatial indexing]("https://www.kaggle.com/datasets/sirpunch/indian-census-data-with-geospatial-indexing")
                """)
    st.download_button(label='Download data as CSV', data=df.to_csv(index=False), file_name='India_data.csv',
                          key='download_button')





selected_state = st.sidebar.selectbox('Select a state', list_of_states)

primary = st.sidebar.selectbox('Select primary parameter', param)
secondary = st.sidebar.selectbox('Select secondary parameter', param)


plot = st.sidebar.button('Plot graph')

if plot:


    if selected_state == 'Overall India':
        st.subheader(f"{primary} vs {secondary}")
        fig = px.scatter_mapbox(df,
                                lat='Latitude',
                                lon='Longitude',
                                zoom=4,
                                size = primary,
                                color = secondary,
                                height = 700,
                                width= 1200,
                                hover_name='District',
                                color_continuous_scale='Agsunset',
                                mapbox_style = 'carto-positron',
                                opacity = 0.7
                                )
        st.plotly_chart(fig, use_container_width= True)

    else:

        state_df = df[df['State'] == selected_state]
        st.subheader(f"{primary} vs {secondary} in {selected_state}")
        fig = px.scatter_mapbox(state_df,
                                lat='Latitude',
                                lon='Longitude',
                                zoom=4,
                                color_continuous_scale='Agsunset',
                                mapbox_style='carto-positron',
                                size=primary,
                                color=secondary,
                                height=700,
                                hover_name='District',
                                opacity = 0.7
                                )
        st.plotly_chart(fig, use_container_width=True)

    st.caption('Size represents primary parameter')
    st.caption('Colour represents secondary parameter')




