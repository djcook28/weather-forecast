import streamlit as st
import plotly.express as px
import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select how many days in the "
                                                                       "future you want to forecast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f'{option} for the next {days} days in {place}')

image_dict = {'Clear': 'sky_images/clear.png', 'Rain': 'sky_images/rain.png', 'Clouds': 'sky_images/cloud.png', 'Snow': 'sky_images/snow.png'}

if place:
    try:
        data = get_data.get_data(days, place)
    except KeyError:
        st.text('Location not found, enter a new location')
    else:
        if option == 'Temperature':
            figure = px.line(x=data['date'], y=data['temp'], labels={'x': 'Date', 'y': 'Temperature (F)'})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_list = []
            for sky in data['sky'].values():
                sky_list.append(image_dict[sky])
            st.image(sky_list, width=115)