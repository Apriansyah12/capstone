import streamlit as st
import tensorflow as tf


bg_img = """

<style>

[data-testid="stAppViewContainer"] > .main{
        background-image: url("https://www.srikotamedical.com/wp-content/uploads/2021/08/Ct-Scan-2.jpg");
        background-size: 1600px 750px;
}
#MainMenu{visibility: hidden;}
footer{visibility: hidden;}
header{visibility: hidden;}

div.css-zt5igj.e16nr0p33{
        background-size: 100% ;
        top: 0px;
        height: 75px;
        position: fixed;
        background: rgba(209, 209, 209, 0.42);
        font-family: 'Inter';
        font-style: normal;
        font-weight: 700;
        font-size: 40px;
        line-height: 48px;
        text-align: center;
        color: black;
}



</style>

"""
st.header('Prediksi Cacar Monyet dan Cacar Biasa')
st.markdown(bg_img, unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding',False)
@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model('/content/model.h5')
  return model
model = load_model()



file = st.file_uploader("masukkan gambar",type=["jpg","png"])
import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):

        size = (150,150)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        prediction = model.predict(img_reshape)

        return prediction

if file is None:
    st.text("tolong masukkan gambar")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ['monkeypox', 'Others', 'smallpox']
    string = "tergolong :" +class_names[np.argmax(predictions)]
    st.success(string)
