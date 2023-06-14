import streamlit as st
import leafmap.foliumap as leafmap
import random
import base64
import requests
import json
import numpy as np
import pandas as pd
import pydeck as pdk
import asyncio
import threading
import requests

from streamlit.components.v1 import html
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
API_URL_PREDICT = "https://keskia-poc-infrastructures-jghnjvcirq-od.a.run.app/predict"

# Warmup
requests.get(API_URL_PREDICT)
np.random.seed(0)

st.set_page_config(layout="wide")
st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.title("Détection des dégâts")
tab_image, tab_video = st.tabs([" 📷 Détection d'image", "📹 Détection vidéo (à venir)"])
tab_image.write(
    "Vous pouvez charger n'importe quelle image d'une infrastructure publique (route, bâtiment, etc) afin de détecter les dommages sur celle-ci (fissures, nids de poule, craquelures, etc)."
)


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def detect(upload):
    image = Image.open(upload)
    col1.write("Image d'origine :camera:")
    col1.image(image, use_column_width=True)
    file = {'file': convert_image(image)}
    response = requests.post(API_URL_PREDICT, files=file)
    if response is not None:
        predictions = json.loads(response.content)
        # Image avec les prédictions
        draw = ImageDraw.Draw(image, "RGBA")
        img_fraction = image.size[1] / 3200
        bounding_boxes = []
        for i, p in enumerate(predictions):
            x, bbox = p[0], p[1]
            bbox_list = [x] + bbox
            bounding_boxes.append(bbox_list)

        color = (255, 0, 0, 32)

        for i, p in enumerate(bounding_boxes):
            x, y, w, h = p[1], p[2], p[3], p[4]
            draw.rectangle([(x, y), (w, h)], outline='red', fill=color, width=2)
            
        col2.write("Image avec les dommages détectées :wrench:")
        col2.image(image, use_column_width=True)

file_upload = tab_image.file_uploader("Charger une image", type=["png", "jpg", "jpeg"])
col1, col2 = tab_image.columns(2)

if file_upload is not None:
    detect(file_upload)
    st.write("#### Quelles sont les coordonnées de la photo ?")
    cols = st.columns(2)
    latitude = cols[0].number_input("Latitude", value=48.822507, min_value=0.0, max_value=90.0)
    longitude = cols[1].number_input("Longitude", value=2.268754, min_value=-180.0, max_value=180.0)
    validate_coords = st.button("Valider les coordonnées")

    if validate_coords:
        st.success("Image ajoutée dans la Map !")
        points = pd.concat((
            points,
            pd.DataFrame([[latitude, longitude]], columns=['lat', 'lon'])
        ), ignore_index=True)
        st.session_state["points"] = points.to_dict()

tab_image.write(''' Exemple d'image détectée''')
tab_image.image('Exemple-image.png')

