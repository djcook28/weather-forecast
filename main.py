import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select how many days in the "
                                                                       "future you want to forecast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f'{option} for the next {days} days in {place}')

if option == 'Temperature':
    st.line_chart()
if option == "Sky":
    st.graphviz_chart()