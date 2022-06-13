import streamlit as st
from streamlit_option_menu import option_menu
from page import home, me
from PIL import Image
from utils import *

def app():
    img = Image.open("img/page_icon.png")
    st.set_page_config(page_title="Analyze your data",
                       page_icon=img,
                       layout="wide",
                       initial_sidebar_state="auto")

    # Bootstrap CSS
    st.markdown("""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous" />""", unsafe_allow_html=True)

    # Custom CSS
    with open("css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Google Fonts
    st.markdown("""<link rel="preconnect" href="https://fonts.gstatic.com" />
    <link href="https://fonts.googleapis.com/css2?family=Viga&display=swap" rel="stylesheet" />""", unsafe_allow_html=True)
    
    # Font Awesome Icons
    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />""", unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu(
            menu_title='Main Menu',
            options=['Home', 'Me'],
            icons=['house', 'person-circle'],
            menu_icon='cast',
            default_index=0
        )
        
    dict_function = {
        "Home": home,
        "Me": me
    }

    dict_function[selected].app()  

app()