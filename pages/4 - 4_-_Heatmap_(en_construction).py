import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "http://freakonometrics.free.fr/popfr19752010.csv"
        m = leafmap.Map(center=[40, 5], zoom=4, tiles="stamentoner")
        m.add_heatmap(
            filepath,
            latitude="lat",
            longitude="long",
            value="pop_2010",
            name="dep",
            radius=20,
        )
m.to_streamlit(height=700)
