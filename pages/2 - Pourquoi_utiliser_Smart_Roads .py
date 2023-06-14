import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Smart Roads")
logo = "Smart-Roads.png"
st.sidebar.image(logo)

st.title('Pourquoi utiliser Smart Roads ? ')

st.write('''Smart Roads a pour but d'être un moyen de prévention sur les dégâts des routes.\n
Ce dernier permet donc de détecter des fissures, des nids de poules ainsi que des craquelures provenant de flux d'images ou vidéos.\n
Il est important de prendre soin des routes de notre si beau pays, lui qui est passé de 1er à 18ème dans le classement de la qualité des infrastructures routières par le forum économique mondial. Et ce, en l'espace de seulement 10ans.\n
Les infrastructures routières endommagées étant des dangers pour tout le monde, et également très compliquées à traiter de par leurs coûts de réparations, exponentiels à l'importance du dégât visé, il est maintenant devenu impératif que nous agissions au plus vite pour éviter que tout cela s'aggrave.\n
Ceci permettrait ainsi de pouvoir avoir une solution viable sur le long terme, permettant également une meilleure attribution du budget concernant les routes, et également de réduire l'impact écologique que peuvent causer de tels danger.
C'est pourquoi utiliser Smart Roads, c'est agir pour tous, et par tous. Que ce soit piétons, conducteurs, entreprises, organismes de transport ou encore des fournisseurs de navigation.\n
### Car Smart Roads, c'est être ensemble pour des routes plus sûres !
''')
         
st.write(" ")
st.write(" ")
st.write(" ")

st.write('### Fournisseurs de navigation'
'''
Les fournisseurs de navigation peuvent être amené à utiliser l'API de Smart Roads afin d'améliorer leurs calculs d'itinéraires, en plus de variables telles que les travaux, bouchons, etc..\n
Les dégâts de la route que Smart Roads détecterait permettront de proposer aux utilisateurs des trajets qui soient moins impactants sur les suspensions des véhicules. 
'''
)

st.write(" ")

st.write('### Organisme de transport'
'''
Les organismes de transport peuvent être amené à utiliser Smart Roads afin de pouvoir superviser l'état de leurs trajets, comme par exemple celui des bus, afin de pouvoir préparer en amont des problèmes potentiels.\n
De plus, des sociétés, telle que Transdev qui ont pour projet d'améliorer la mobilité douce, pourraient ainsi avoir une manière d'estimer les coûts de rénovations/installations de nouvelles routes/pistes. 
'''
)

st.write(" ")

st.write('### Entreprises'
'''
Des entreprises peuvent être amené à utiliser Smart Roads afin de pouvoir adapter les trajets de leurs véhicules professionnels.\n
En effet ces derniers, effectuant pour certains les mêmes trajets régulièrement, pourraient comprendre exactement où se situe les potentiels problèmes qui causeraient une dégradation accélerée des véhicules.
'''
)

st.write(" ")

st.write('### Conducteurs'
'''
Les conducteurs sont les plus concernés. Avec plus de 39 millions de véhicules circulants sur les routes françaises, ainsi que d'une étude mené par l'association *40 Millions d'automobilistes* qui estime que \n
" 47% des accidents de la route mettent en cause la qualité ou l'entretien des infrastructures routières".\n
Il est donc facilement compréhensible que l'état des routes est un problème de taille qui en va de la sécurité de tous. Ainsi, un conducteur lambda pourrait très bien être amené à aider à régler cela en envoyant, par exemple, un flux vidéo filmé par une dash-cam lors de ses trajets.
'''
)

st.write(" ")

st.write('### Piétons'
'''
Bien que le nom de "Smart Roads" semble évoquer le fait que cette intelligence artificielle s'occuppe exclusivement des routes, elle est également utilisable dans d'autres circonstances, qui est celui des trottoirs par exemple.\n
De plus, les piétons sont  une priorité concernant les dangers sur le sujet des accidents, ces derniers représentant une part importante de la mortalité sur les routes. Car dans le cas d'un heurt avec un véhicule, les piétons ont une grande chance de subir des dégâts critiques, et ce même dans le cas d'un heurt avec un véhicule roulant à faible allure. Ainsi, participer à cette prévention des routes permet également de jouer un rôle dans la vigilance générale.\n
De ce fait, un piéton peut être amené à aider contre ce problème que ce soit en prenant des photos ou des vidéos de n'importe quelle infrastructure routière !
'''
)
