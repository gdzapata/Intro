import streamlit as st
from PIL import image
st.title ("Mi primera APP")
image = Image.open ("Automata.png")
st.image(image, caption="Automata.png")

