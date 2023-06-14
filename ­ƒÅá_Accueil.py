import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.write('''
# Bienvenue sur l'interface de Smart Roads.\n
## Ici, vous pourrez retrouver tous les détails concernant Smart Roads, ses origines, ainsi que ses multiples fonctionnalités.\n
Si vous êtes une société et que vous souhaitez utiliser notre API, vous pouvez nous contacter au :\n
- Téléphone : 01.23.45.67.89 *(disponible de 9h à 18h du lundi au vendredi)*\n
- Mail : Smart-Roads@mail.fr\n
Pour tout autre demande ou recommendation, nous vous invitons à vous rendre ici : https://www.smart-roads.fr/forum/\n

*(Ces informations sont actuellement fictives)*
''')