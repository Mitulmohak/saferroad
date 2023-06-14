import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.title("L'histoire de Smart Roads")
DEFAULT_WIDTH = 100
VIDEO_DATA = "https://youtu.be/osUzc9Yts_g"


width = st.sidebar.slider(
    label="Taille de la vidéo", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
)

width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)

_, container, _ = st.columns([side, width, side])
container.video(data=VIDEO_DATA)

st.write('''
*"Les routes endommagées... Les routes endommagées sont synonymes de dangers !"*

Une fois de plus... Un appel en détresse retentit... Damaged Roads, l'incarnation des routes endommagées, continues de sévir... Cette fois, c'est celle de trop ! 

Evolukid n'a pas pu ignorer plus longtemps cette menace grandissante qui détruisait intérieurement notre si beau pays, il fallait mettre fin à cette calamité qu'est Damaged Roads !\n
Cependant, conscient que ce combat ne pouvait être mené seul, Evolukid s'est lancé dans une quête acharnée pour trouver des alliés à se joindre à sa cause dans les 4 coins de la France.\n
C'est ainsi que dans le Pas-de-Calais, un alliance naquît entre Evolukid, Sap, L'Oréal et les communautés d'agglomération de Lens-Liévin/Hénin-Carvin.
''')
st.write("## L'alliance pour le nord vient de naitre.")

st.write('''
Ces 4 puissances réunis formèrent ainsi une équipe de choc, composé de :''')

col1,col2,col3 = st.columns(3)
with col1 :
    st.image('Roman.png', caption="Roman Coulon, un ex-streamer sortant fraichement d'un titre de Technicien Informatique.", use_column_width="always")
with col2 :
    st.image("Hasina.png",caption="Hasina Sitraka Rakotoarison, future étudiante en École d'Ingénieur en recherche d'alternance dans le développement Informatique.", use_column_width="always")
with col3 :
    st.image('Kevin.png', caption="Kévin Lopez, un Technicien Supérieur Systèmes et Réseaux développant ses propres jeux à ses temps perdus.", use_column_width="always")

st.write("### Le projet Safer Roads venait ainsi de débuter !")

st.write(' ')
st.write(' ')
st.write('''# "Safer Roads ? Qu'est ce que c'est?"''')
st.write('''
Le projet Safer Roads se déroule en 3 étapes :\n
1 - L'entrainement des 3 jeunes prodiges par le biais d'un bootcamp de 5 jours, aliant apprentissage du langage de programmation *Python* ainsi que la compréhension des fondement de l'Intelligence Artificielle\n
2 - Des Séannces "POC" consistant à la création d'une IA, passant de la préparation des données, par l'entrainement du modèle,  pour enfin mettre en place un prototype fonctionnel.\n
3 - La mise en marche de l'IA qui changera le futur de la sécurité routière. Némésis de Damaged Roads... Le fameux.. 
# Smart Roads ! #
''')
