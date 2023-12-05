import streamlit as st
import pandas as pd
from PIL import Image

from services import TutorialService

######################################################### STARTS HEADER

st.set_page_config(
    page_title="Streamlit-template",
    page_icon="👋",
)

titCol, imgCol = st.columns(2)

with titCol:
  st.markdown('# Nimbus Documentation')
  
with imgCol:
    logo = Image.open("./images/nimbus_intelligence_logo_full_transparent_dark-1024x314.png")
    st.image(logo)


######################################################## STARTS PAGE!

## Create Variables
if 'results' not in st.session_state:
    st.session_state.results = pd.DataFrame()

if 'markdown' not in st.session_state:
    st.session_state.markdown = ''
    

def update_input():
    results = TutorialService.get_tutorial_by_name(st.session_state.name_query)
    #data = [{'name': obj.name, 'date': obj.date, 'author': obj.author, 'content': obj.content} for obj in results]
    #df = pd.DataFrame(data)
    #st.session_state.results = df
    st.session_state.results = results


st.session_state.name_query = st.text_input("title_to_search")


colsearch, colall = st.columns(2)
with colsearch:
  if(st.button("Search")):
      update_input()

with colall:
  if st.button("Get All"):
    st.session_state.results = TutorialService.get_all_tutorials()

emptyResults = len(st.session_state.results) == 0
with st.expander("See Results", expanded=emptyResults):
  for result in st.session_state.results:
      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
          st.write(result.name)
      with col2:
          st.write(result.author)
      with col3:
          st.write(result.date)
      with col4:
          a = st.button("Show", key=f"{result.id}_create")
      with col5:
          b = st.button("Delete", key=result.id)
      if(a):
          st.session_state.markdown = result.content
      if(b):
          TutorialService.delete_tutorial_by_id(result.id)
          new_list = [item for item in st.session_state.results if item.id != result.id]
          st.session_state.results = new_list



st.markdown(st.session_state.markdown)

