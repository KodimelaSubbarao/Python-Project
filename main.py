# importing libraries
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from tensorflow import keras
from PIL import Image
import cv2
import os

file = open('pesticides.txt', 'r')
text = file.read()

labels = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

model = keras.models.load_model('Model.h5')

dic = {}

dic['Tomato___Bacterial_spot'] = 'BLUE COPPER,UTHANE M-45'
dic['Tomato___Early_blight'] =  "AMISTAR TOP,NATIVO"
dic['Tomato___Leaf_Mold'] = 'INDOFIL Z-78'
dic['Tomato___Late_blight'] = 'FOLIO GOLD,ABIC'
dic['Tomato___Spider_mites Two-spotted_spider_mite'] = 'OBERON'
dic['Tomato___Target_Spot'] = 'M-45INDOFIL,COPPEROXYCHLORIDE'
dic['Tomato___Tomato_Yellow_Leaf_Curl_Virus'] = 'CONFIDER,BENEVIA'
dic['Tomato___Septoria_leaf_spot'] = 'CHLOROTHALONIL,MANCOZEB'
dic['Tomato___Tomato_mosaic_virus'] = 'RAZE,FOLIOS'
dic['Pepper,_bell___Bacterial_spot'] = 'FOLIAR SPRAY,CAREBENDAZIM 12.0% WP'
dic['Strawberry___Leaf_scorch'] = 'TRICHOCARE,MALATHION 50'
dic['Potato___Late_blight'] = 'MANCOZEB, DIMETHOMORPH 20.27%'
dic['Potato___Early_blight'] = 'KNOCKOUT NANO,PROPI'
dic['Squash___Powdery_mildew'] = 'BAVISTIN,DHANUSTIN'
dic['Grape___Black_rot'] = 'MANCOZEB'
dic['Grape___Esca_(Black_Measles)'] = 'CUSTODIA'
dic['Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'] = 'CURZATE M8'
dic['Cherry_(including_sour)___Powdery_mildew'] = 'PROPICONAZOLE'
dic['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot'] = 'ZEB M- 45,AZOXYSTROBIN'
dic['Corn_(maize)___Common_rust_'] = 'MACOBAN M-45,ABIC'
dic['Corn_(maize)___Northern_Leaf_Blight'] = 'INDOFIL Z-78,MOUNT -45'
dic['Apple___Cedar_apple_rust'] = 'LIQUID COPPER'
dic['Apple___Black_rot'] = 'CAPTAN,SULFUR'
dic['Apple___Apple_scab'] = 'MYCLOBUTANIL'
dic['Orange___Haunglongbing_(Citrus_greening)']='ZINCO'
dic['Peach___Bacterial_spot']='FURY,RENO'

dic1 = {}

dic1['BLUE COPPER'] = 'https://amzn.eu/d/56MZZBN'
dic1['UTHANE M-45'] = 'https://amzn.eu/d/erW82yE'
dic1['AMISTAR TOP'] = 'https://amzn.eu/d/c7WcbcR'
dic1['NATIVO'] = 'https://amzn.eu/d/hCIfO8B'
dic1['INDOFIL Z-78'] = 'https://amzn.eu/d/3ZQZQZQ'
dic1['FOLIO GOLD'] = 'https://amzn.eu/d/4nQxDsm'
dic1['ABIC'] = 'https://amzn.eu/d/5biBSj7'
dic1['OBERON'] = 'https://amzn.eu/d/5AElS7L'
dic1['M-45INDOFIL'] = 'https://amzn.eu/d/0JLv5q2'
dic1['COPPEROXYCHLORIDE'] = 'https://amzn.eu/d/3FVXnre'
dic1['CONFIDER'] = 'https://amzn.eu/d/7X00LEN'
dic1['BENEVIA'] = 'https://amzn.eu/d/dY8OilX'
dic1['CHLOROTHALONIL'] = 'https://amzn.eu/d/dKViMd1'
dic1['MANCOZEB'] = 'https://amzn.eu/d/3ChkiJf'
dic1['RAZE'] = 'https://amzn.eu/d/12rLJmW'
dic1['FOLIOS'] = 'https://amzn.eu/d/7TpuIy5'
dic1['FOLIAR SPRAY'] = 'https://amzn.eu/d/9LK8od2'
dic1['CAREBENDAZIM 12.0% WP'] = 'https://images.app.goo.gl/iMazq3gw3MJAz6WGA'
dic1['TRICHOCARE'] = 'https://amzn.eu/d/9VDEmZT'
dic1['MALATHION 50'] = 'https://amzn.eu/d/9VDEmZT'
dic1['DIMETHOMORPH 20.27%'] = 'https://amzn.eu/d/bTpVPYK'
dic1['KNOCKOUT NANO'] = 'https://amzn.eu/d/hiuacz3'
dic1['PROPI'] = 'https://amzn.eu/d/d3Pi6uH'
dic1['BAVISTIN'] = 'https://amzn.eu/d/4bRrr4q'
dic1['CUSTODIA'] = 'https://amzn.eu/d/ff3rmLi'
dic1['CURZATE M8'] = 'https://amzn.eu/d/0lJf9Ew'
dic1['PROPICONAZOLE'] = 'https://amzn.eu/d/0IVf3jp'
dic1['ZEB M- 45'] = 'https://amzn.eu/d/3Aom2UO'
dic1['AZOXYSTROBIN'] = 'https://amzn.eu/d/0uoaHoS'
dic1['MACOBAN M-45'] = 'https://amzn.eu/d/7vjgWvD'
dic1['INDOFIL Z-78'] = 'https://amzn.eu/d/276XfPD'
dic1['LIQUID COPPER'] = 'https://amzn.eu/d/1TrelaV'
dic1['CAPTAN'] = 'https://amzn.eu/d/13pz4g6'
dic1['SULFUR'] = 'https://amzn.eu/d/ibeppTH'
dic1['MYCLOBUTANIL'] = 'https://farmkey.in/product/index%E0%A4%87%E0%A4%82%E0%A4%A1%E0%A5%87%E0%A4%95%E0%A5%8D%E0%A4%B8'
dic1['ZINCO']='https://amzn.eu/d/6j6RAie'
dic1['FURY']='https://amzn.eu/d/ceU75ju'
dic1['RENO']='https://amzn.eu/d/j02A4b6'

def predict(img):
    img = np.asarray(img)
    img = cv2.resize(img, (224, 224))
    img = img.reshape(1, 224, 224, 3)
    prediction = model.predict(img)
    label = labels[np.argmax(prediction[0])]
    confidence = round( (np.max(prediction[0])), 2) 
    return label, confidence


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():

    # sidebar for navigation
    with st.sidebar:
        
        selected = option_menu('Leaf Disease Detector',
                            
                            ['Home','Disease Detector'],
                            icons=['activity','heart',],
                            default_index=0)

    if selected == "Home":
        st.markdown("<h1 style='text-align: center; color: #08e08a;'>Leaf Disease Detector</h1>", unsafe_allow_html=True)
        st.markdown("<h4 '>A web app to detect diseases in leafs using Deep Learning and computer vision</h4>", unsafe_allow_html=True)
        lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1plcwvk5.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="High",
            #renderer="svg",
            height=400,
            width=-900,
            key=None,
        )
        st.markdown("<h4 '>About:</h4>", unsafe_allow_html=True)
        st.write("<p align='justify' '>Food security for billions of people on earth requires minimizing crop damage by timely detection of diseases.Developing methods for detection of plant diseases serves the dual purpose of increasing crop yield and reducing pesticide use without knowing about the proper disease. Along with development of better crop varieties, disease detection is thus paramount goal for achieving food security. The traditional method of disease detection has been to use manual examination by either farmers or experts, which can be time consuming and costly, proving infeasible for millions of small and medium sized farms around the world.</p>",unsafe_allow_html=True)

        st.markdown("<h4 '>Features:</h4>", unsafe_allow_html=True)
        st.write("Easy Detection of diseases in leafs: Just need to click and upload leaf image.")
        st.write("Fast and Accurate: Provides the disease with high accuracy and fast")
        st.write("Cause and Solution of diseases: Provides the cause and solution of the disease")
        st.write('Large Plant Support: Supports 38 different classes')

        # list of plants we can detect
        st.markdown("<h4  '>List of Plant diseases we can predict</h4>", unsafe_allow_html=True)
        st.write(labels)
        lotti = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_srcvuh0h.json")
        st_lottie(
            lotti,
            speed=1,
            reverse=False,
            loop=True,
            quality="High",
            #renderer="svg",
            height=400,
            width=-900,
            key=None,
        )

    elif selected == "Disease Detector":
        st.markdown("<h1 style='text-align: center; color: #08e08a;'>Disease Detector</h1>", unsafe_allow_html=True)
        lot = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_0xbu1xfo.json')
        st_lottie(
            lot,
            speed=1,
            reverse=False,
            loop=True,
            quality="High",
            #renderer="svg",
            height=400,
            width=-900,
            key=None,
        )
        image  = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        if image is not None:
            image = Image.open(image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.write("")
            label, confidence = predict(image)
            st.write(f"**Predicted Class:** {label}")
            st.write(f"**Confidence:** {confidence}")
            st.write("")
            x = label
            if x in text:
                if text.split(x)[1].splitlines()[1] != '':
                    st.write(text.split(x)[1].splitlines()[1])
                    if text.split(x)[1].splitlines()[2] != '':
                        st.write(text.split(x)[1].splitlines()[2])
                        if text.split(x)[1].splitlines()[3] != '':
                            st.write(text.split(x)[1].splitlines()[3])
                            if text.split(x)[1].splitlines()[4] != '':
                                st.write(text.split(x)[1].splitlines()[4])
                                if text.split(x)[1].splitlines()[5] != '':
                                    st.write(text.split(x)[1].splitlines()[5])
                                    if text.split(x)[1].splitlines()[6] != '':
                                        st.write(text.split(x)[1].splitlines()[6])
                                        if text.split(x)[1].splitlines()[7] != '':
                                            st.write(text.split(x)[1].splitlines()[7])
                                            if text.split(x)[1].splitlines()[8] != '':
                                                st.write(text.split(x)[1].splitlines()[8])
                                                if text.split(x)[1].splitlines()[9] != '':
                                                    st.write(text.split(x)[1].splitlines()[9])
                                                    if text.split(x)[1].splitlines()[10] != '':
                                                        st.write(text.split(x)[1].splitlines()[10])
                                                        if text.split(x)[1].splitlines()[11] != '':
                                                            st.write(text.split(x)[1].splitlines()[11])
                                                            if text.split(x)[1].splitlines()[12] != '':
                                                                st.write(text.split(x)[1].splitlines()[12])
                                                                if text.split(x)[1].splitlines()[13] != '':
                                                                    st.write(text.split(x)[1].splitlines()[13])
            #st.warning(text.split(x)[1].splitlines()[2])
            if 'Disease: No disease' in text.split(x)[1].splitlines()[2]:
                st.success("Your plant is healthy")
            else:
                st.write("Suggested Pesticides:")
                pes = dic[x]
                st.write(pes)
                pes = pes.split(',')
                for i in pes:
                    path = 'Pesticides/' + i + '.jpg'
                    if os.path.exists(path):
                        st.write("Which looks like:")
                        st.image(path, caption=i, use_column_width=True)
                        st.write("You can buy it from here:")
                        st.write(dic1[i])
                        pass
                    else:
                        pass

if __name__ == "__main__":
    main()
