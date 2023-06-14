import ast
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.title('Le futur de Smart Roads')

st.write('''
### À l'heure actuelle, Smart Roads est encore à ses débuts, étant dans sa phase prototypale.\n 
### Cependant, nous avons déjà commencé à travailler sur différents aspects d'évolution de l'IA que nous comptons ajouter, voici les suivants :\n''')
st.write('')
st.write('''
### Prendre en compte des variables complémentaires :\n
Smart Roads ayant un système de détection vidéo, l'ajout de variables telles que la signalisation, la vitesse des véhicules, les vibrations des véhicules, etc.. Qui pourraient être détectables via une vidéo, permettraient de pouvoir établir un degré de dangerosité des dégâts, permettant ainsi de mettre un point sur les différents endroits où la réparations des infrastructures routière est d'une importance critique.\n
''')
st.write('')
st.write('''
### Détection d'autres dégâts routiers :\n
À l'heure actuelle, Smart Roads détecte les fissures, les craquelures et les nids-de-poules dans certaines conditions.\n
En addition au fait d'améliorer la détections des trois précédents, et ce dans n'importe quel contexte du dégât *(ex : nid-de poule rempli de pluie)*,
nous avons pour projet d'ajouter des dégâts de la routes supplémentaires, telle que le délaminage, l'érosion/l'usure, les affaissements, les tassements ou encore bien d'autres.\n
Ainsi, cela permettrait de détecter l'entièreté des problèmes de sécurité que peuvent faire face nos conducteurs.
''')
st.write('')
st.write('''
### Détection d'éléments supplémentaires :\n
L'algorithme utilisé par Smart Roads ayant une vaste capacité de détection, il pourrait être viable d'ajouter la détection d'éléments supplémentaires, comme par exemple les déchets dans les rues.\n
Cependant, ceci pourrait également faire objet d'une IA "cousine", une éventuelle IA "Smart City" est ainsi envisageable dans un futur proche.
''')
         
st.write('')
st.write('')
st.write('')
st.write('')

st.write("Vous avez une recommendation sur une éventuelle amélioration de Smart Roads ? N'hésitez à venir nous en faire part depuis le lien suivant : https://www.smart-roads.fr/forum/ ")