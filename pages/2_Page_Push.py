import streamlit as st
from io import StringIO
from PIL import Image
from datetime import datetime
from services import TutorialService


######################################################### STARTS HEADER

st.set_page_config(
    page_title="Push-page",
    page_icon="👋",
)

titCol, imgCol = st.columns(2)

with titCol:
  st.markdown('# Nimbus Documentation')
  
with imgCol:
    logo = Image.open("./images/nimbus_intelligence_logo_full_transparent_dark-1024x314.png")
    st.image(logo)


######################################################## STARTS PAGE!


uploaded_file = st.file_uploader("Choose a file")

col_name, col_author = st.columns(2)

with col_name:
    new_name = st.text_input("Name")

with col_author:
    new_author = st.text_input("Author")

if(st.button("Create")):
    if(new_name != "" and new_author != "" and uploaded_file is not None):
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()

        # Obtener la fecha actual
        current_date = datetime.now()

        # Formatear la fecha como una cadena en el formato YYYY-MM-DD
        formatted_date = current_date.strftime("%Y-%m-%d")
        datalist = [{"name":new_name, "author":new_author, "date":formatted_date, "content":string_data}]
        TutorialService.push_tutorials(datalist) 
        