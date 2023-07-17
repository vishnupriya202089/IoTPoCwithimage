import streamlit as st
from streamlit_option_menu import option_menu




st.set_page_config(page_title="IoT CoE Track 'N' Trace",page_icon=":tada:",layout="wide")

with st.container():
 #st.subheader("Track and Trace Application")
 st.title("IoT CoE Track 'N' Trace")

 with  st.sidebar:
  selected =option_menu(
         menu_title="Assembly Line",
         options=("Material Handling Station","Pinning and Press Station","Drilling Station"),
  )


if selected == "Pinning and Press Station":
  col1, col2, col3 = st.columns([1, 2, 1])

  camera_photo = col2.camera_input("take a photo")
  uploaded_photo = col2.file_uploader("upload a photo")

  if selected == "Pinning and Press Station":
      st.title(f"you have selected {selected}")

  if selected == "Drilling Station":
      st.title(f"you have selected {selected}")
