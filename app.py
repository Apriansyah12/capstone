import streamlit as st

st.header('Prediksi Cacar Monyet dan Cacar Biasa')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

picture = st.camera_input("Masukkan Gambar")

if picture:
    st.image(picture)

st.button('input gambar')