import streamlit as st
from PIL import Image

######################################################### STARTS HEADER

st.set_page_config(
    page_title="About-page",
    page_icon="👋",
)

titCol, imgCol = st.columns(2)

with titCol:
  st.markdown('# Nimbus Documentation')
  
with imgCol:
    logo = Image.open("./images/nimbus_intelligence_logo_full_transparent_dark-1024x314.png")
    st.image(logo)


######################################################## STARTS PAGE!

st.markdown("Here will go all the About")