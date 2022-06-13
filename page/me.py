import streamlit as st
from utils import *

def app():
    image = decode_img("img/geza.jpg")
    
    st.markdown("""
        <h1 class="adding-top-0">
            Muhammad Geza Ruly Syahputra
        </h1>""", unsafe_allow_html=True)

    st.write("""
    ##### ***Data Enthusiasm***
    """)

    # image
    st.markdown(f"""
        <div class="text-center">
          <img src="data:image/png;base64,{image}" width="200" height="150" class="rounded-circle img-thumbnail">
        </div>""", unsafe_allow_html=True)
    #  End Image

    st.markdown("""
        <h1 class="margin-top-2rem padding-top-0">
            Contact Me at:
        </h1>""", unsafe_allow_html=True)

    # Social Media Buttons
    st.markdown("""
        <div class="container">
          <div class="row">
            <div class="wrapper justify-content-center">
              <div class="col-2">
                <a class="color-black" href="https://wa.me/6282129033281/?text=" target="_blank">
                  <div class="icon whatsapp color-black">
                    <div class="tooltip">MyWa</div>
                    <span><i class="fab fa-whatsapp"></i></span>
                  </div>
                </a>
              </div>
              <div class="col-2">
                <a class="color-black" href="https://www.linkedin.com/in/muhammad-geza-ruly-syahputra-091393240/" target="_blank">
                  <div class="icon linkedin-in color-black">
                    <div class="tooltip">MyLinkedin</div>
                    <span><i class="fab fa-linkedin-in"></i></span>
                  </div>
                </a>
              </div>
              <div class="col-2">
                <a class="color-black" href="https://www.instagram.com/muh_geza/" target="_blank">
                  <div class="icon instagram color-black">
                    <div class="tooltip">@muh_geza</div>
                    <span><i class="fab fa-instagram"></i></span>
                  </div>
                </a>
              </div>
              <div class="col-2">
                <a class="color-black" href="mailto:gezaruly998@gmail.com" target="_blank">
                  <div class="icon envelope color-black">
                    <div class="tooltip">gezaruly998@gmail.com</div>
                    <span><i class="fas fa-envelope"></i></span>
                  </div>
                </a>
              </div>
              <div class="col-2">
                <a class="color-black" href="https://github.com/MuhammadGeza" target="_blank">
                  <div class="icon github color-black">
                    <div class="tooltip">MyGithub</div>
                    <span><i class="fab fa-github"></i></span>
                  </div>
                </a>
              </div>
            </div>
          </div>
      </div>""", unsafe_allow_html=True)
        # End Social Media Buttons