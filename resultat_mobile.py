import streamlit as st
import time 
from datetime import datetime, timedelta
from PIL import Image
import base64
from streamlit_autorefresh import st_autorefresh

def init_state():   
        if "etape" not in st.session_state:
            st.session_state.etape = 0

def etape_suivante():
    st.session_state.etape +=1

def merge_images_side_by_side(paths, target_height=400):
    imgs = [Image.open(p) for p in paths]
    # redimensionner toutes à la même hauteur en gardant le ratio
    resized = []
    for img in imgs:
        ratio = target_height / img.height
        new_width = int(img.width * ratio)
        resized.append(img.resize((new_width, target_height)))
    
    total_width = sum(img.width for img in resized)
    combined = Image.new("RGB", (total_width, target_height), "white")
    
    x = 0
    for img in resized:
        combined.paste(img, (x, 0))
        x += img.width
    
    return combined

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

    
st_autorefresh(interval=50000, key="refresh")
st.set_page_config(layout="wide")
st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

            html, body, [class*="css"] {
                font-family: 'Poppins', sans-serif;
            }

        /* La bulle du chat */
        div[data-testid="stChatMessage"] {

            background: white;

            border: 2px solid black;

            border-radius: 20px;

            padding: 20px;

            margin-bottom: 5px;

            box-shadow: 2px 2px 0px black;
        }

        /* Bouton mobile */
        .stButton > button {

            width: 100%;

            background-color:  #FCA616;
            color: white;
            border: 2px solid #14203E;

            border-radius: 16px;

            padding: 10px 14px;

            font-size: 0.95rem;
            font-weight: 600;

            box-shadow: 2px 2px 0 black;

            transition: all .15s ease;

            min-height: 44px;      /* recommandé pour le tactile */

            touch-action: manipulation;
        }

        /* Hover (visible surtout sur tablette) */
        .stButton > button:hover {

            transform: translate(-1px,-1px);

            box-shadow: 6px 6px 0px #14203E;
        }

        /* Appui */
        .stButton > button:active {

            transform: translate(1px,1px);
            box-shadow: 1px 1px 0 #14203E;
        }

        /* Focus */
        .stButton > button:focus {
            outline: none !important;
        }

/* Cache la checkbox native */
input[type="checkbox"] {
    display: none;
}

/* Carte */
div[data-testid="stCheckbox"] label {

    background: white;

    border: 2px solid black;

    border-radius: 20px;

    padding: 12px 18px;

    margin-bottom: 12px;

    box-shadow: 4px 4px 0px black;

    cursor: pointer;

    transition: all 0.15s ease;
}

/* Hover */
div[data-testid="stCheckbox"] label:hover {

    transform: translate(-2px,-2px);

    box-shadow: 2px 2px 0px black;
}

/* Sélectionné */
div[data-testid="stCheckbox"] label:has(input:checked) {

    background: #4F73D1 !important;
    color: white !important;
    transform: translate(2px,2px);

    box-shadow: 1px 1px 0px black;
}
div[data-testid="stCheckbox"] label:has(input:checked)
[data-testid="stMarkdownContainer"] {
    color: white !important;
}
div[data-testid="stCheckbox"] label span:first-child {
    display: none;
}
@media (max-width:768px){

div[data-testid="stCheckbox"] label{

border-width:1px;

border-radius:16px;

padding:8px 12px;

box-shadow:2px 2px 0 black;

margin-bottom:8px;

font-size:.92rem;
}

}

    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0rem !important;
    }

    header[data-testid="stHeader"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)


langue, vide, coltitre, vide = st.columns([1,2,3,1])
with langue:
    lang = st.session_state["langue"]
if lang == "Fr":
    title_site = "SysTox Game"
    subheader_title = "Alerte au laboratoire !"
    intro_equipe = "Cet escape game pédagogique a été conçu et déeloppé par l'équipe SysTox de l'INSERM à l'Université Paris Cité (https://systox.u-paris-sciences.fr/)"
    text_intro ="<strong>Bienvenue dans votre mission !</strong><br> Vous incarnez un stagiaire dans un laboratoire universitaire.<br> <strong> À 16 h 15…</strong> Alors que vous êtes seul dans le laboratoire lorsque,…<br> <strong>BIP ! BIP ! BIP !</strong><br> Une alarme retentit. Un flacon contenant un produit toxique vient s'est renversé sur la paillasse de la salle de chimie analytique.<br><br> Le temps presse. Vous devez analyser la situation, sécuriser les lieux et agir sans mettre votre santé ni celle des autres en danger.<br><br> <strong> Attention !</strong> Chaque bonne décision vous révélera un chiffre du code final <strong>code secret</strong>. Une erreur pourrait aggraver l'incident... </strong><br><br> Saurez-vous garder votre sang-froid ?"
    #text_intro = "<strong>Bonjour !</strong><br><br> Vous êtes dans la peau d’un stagiaire en laboratoire universitaire."
    warning_time = "Cela fait plus de 1 minutes."
    initialisation_button = "C'est parti !"
    validermesreponses = "Valider mes réponses"
    felicitationcode = ":sparkles: félicitations vous avez trouvé un code  :sparkles: "
    #niveau1
    text_bulle_mission1 = "VITE! Un flacon contenant une poudre toxique s'est renversé sur la paillasse. Réagissez rapidement!"
    text_question1 = "Mission 1 : Quels sont vos premiers réflexes ?"
    question1A = "A. Ramasser immédiatement le flacon"
    question1B = "B. Quitter la pièce"
    question1C = "C. Identifier le produit"
    question1D = "D. Nettoyer avec du papier absorbant puis de l’eau distillée"
    question1E = "E. continuer vos manipulations"
    text_bulle_mission2= "L'alarme retentit toujours.\
    Une forte odeur se répand dans le laboratoire. La ventilation est insuffisante et un étudiant est encore présent à proximité."
    text_question2 = "Même sans symptôme, cela signifie:"
    question2A = "A. il n'a pas été exposé"
    question2B = "B. Son EPI (équipement de protection individuelle) empêche toute exposition."
    question2C = "C. l'exposition est possible avec des effets retardée."
    question2D = "D. La substance est inoffensive"
    question2E = "E. Aucune de ces réponses"
    text_bulle_mission3 = "L’étiquette du flacon est illisible, mais les pictogrammes de danger restent visibles."
    text_question3 = "Que vous indiquent-ils ?"
    question3A = "A. Toxicité aigüe, corrosion/irritation cutanée, sensibilisation respiratoire"
    question3B = "B. Explosif, corrosion/irritation cutanée, toxicité aiguë"
    question3C = "C. Danger pour le milieu aquatique et l’homme, irritant cutané, toxicité aiguë"
    question3D = "D. Gaz inflammable, irritant cutané, CMR (Cancérogène, Mutagène, Reprotoxique)"
    question3E = "E. Aucune de ses réponses"
    text_bulle_mission4= "La nomenclature de IUPAC et donc sa structure chimique du produit est encore visible. À l’aide du catalogue du laboratoire, identifiez la substance."
    text_question4 = "Quelle molécule correspond à cette structure"
    question4A = "A.  Acide pentadécafluorooctanoïque (PFOA)"
    question4B = "B.  Acide perfluorononanoïque (PFNA)"
    question4C = "C.  Acide heptafluorobutanoïque (PFBA)"
    question4D = "D.  Acide perfluorodécanoïque (PFDA)"
    question4E = "E.  Acide perfluoroheptanoïque (PFHpA)"
    question4F = "F.  Aucune réponse"
    text_bulle_mission5 = "La substance est identifiée. Consultez sa fiche de données de sécurité : <br>H318 : provoque des lésions oculaires graves. <br>H351 : susceptible de provoquer le cancer. <br>H315 : provoque une irritation cutanée. <br>Quels EPI choisir avant toute intervention ?"
    text_question5 = "Quels équipements de protection individuelle (EPI) devez-vous choisir avant toute intervention ?"
    question5A ="A.Lunettes de protection"
    question5B ="B.Gants nitrile adaptés"
    question5C ="C.Gants de vaisselle en latex"
    question5D ="D. Masque de protection respiratoire adapté"
    question5E ="E.Respirateur à cartouche"
    question5F ="F. Blouse de laboratoire"
    question5G ="G. Masque FFP3"
    text_bulle_mission6 = "La substance identifiée appartient à la famille des PFAS, appelés « polluants éternels »"
    text_question6 = "Quelles sont leurs caractéristiques ?"
    question6A ="A. Certains peuvent avoir des effets toxiques sur la santé"
    question6B ="B. Ils se dégradent rapidement à la lumière"
    question6C ="C. Ils sont très stables et persistants dans l’environnement"
    question6D ="D. Ils peuvent se déplacer sur de longues distances et contaminer l’eau et les sols"
    question6E ="E. Ils peuvent s’accumuler dans les organismes vivants"
    text_bulle_mission7 = "L'incident est désormais terminé ! Vous avez analysé la situation et agit en conséquence. Le directeur du laboratoire a été informé et l'évènement a été signalé dans le registre SST"
    text_question7 = "Pour éviter de futurs accidents, quelles bonnes pratiques adopter ?"
    question7A = "A. Garder des étiquettes lisibles sur tous les flacons"
    question7B = "B. Ranger les produits inutilisés dans une armoire adaptée"
    question7C = "C. Signaler clairement la présence de substances dangereuses"
    question7D = "D. Installer une caméra dans le laboratoire"
    question7E = "E. Aucune réponse"
    text_avant_code ="Ca y est. Vous y êtes presque. Ecrivez maintenant les lettres et chiffres que vous avez obtenu afin de vérifier vos reponses !"
    text_input_code = "Votre code :"
    text_erreur_code = "Oh non ! Vous avez fait au moins une erreur !"
    text_bravo_code = "BRAVO :sparkles:"
    text_bulle_fin = "Ouah Bravo ! <br/> <br/>À savoir!\
                                    Les PFOA sont des substances préoccupantes pour la santé et l’environnement !<br/>\
                                    Ils appartiennent à la famille des PFAS, surnommés « polluants éternels » en raison de leur extrême résistance à la dégradation. Ils peuvent persister longtemps dans l’environnement, contaminer les sols, les eaux et s’accumuler dans les organismes vivants. <br/>\
                                    Chez l’homme, une exposition prolongée ou répétée aux PFOA a été associée à plusieurs effets préoccupants sur la santé. Des études scientifiques ont notamment mis en évidence des liens possibles avec une augmentation du taux de cholestérol, des perturbations du fonctionnement du foie, des effets sur le système immunitaire, ainsi que des impacts sur le développement du fœtus et la fertilité. Le PFOA est également classé comme cancérogène (CIRC, groupe 1) en raison d’un lien établi avec certains cancers, notamment le cancer du rein et des testicules.<br/>\
                                    Face à ces risques, l’utilisation des PFOA est aujourd’hui fortement limitée. Le PFOA est inscrit à la Convention de Stockholm sur les polluants organiques persistants, ce qui entraîne son interdiction ou sa restriction à l’échelle internationale, avec quelques exceptions spécifiques. En Europe, sa fabrication et son utilisation sont également très encadrées dans le cadre de la réglementation REACH. <br/>\
                                    À retenir : même lorsqu’un produit n’entraîne pas d’effet immédiat visible, une exposition répétée peut avoir des conséquences à long terme. La connaissance des dangers, le respect des procédures de sécurité et la réduction des expositions sont essentielles pour protéger la santé humaine et l’environnement.<br/>\
                                    <strong>Pour en savoir plus:</strong><br/>\
                                    <a href='https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/'>https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/ </a> <br/>\
                                    <a href='https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes'>https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes </a>\
                                    "
    text_bulle_fin_echec = "Oh non, tu as échoué.. <br/> <br/>À savoir!\
                                    Les PFOA sont des substances préoccupantes pour la santé et l’environnement !<br/>\
                                    Ils appartiennent à la famille des PFAS, surnommés « polluants éternels » en raison de leur extrême résistance à la dégradation. Ils peuvent persister longtemps dans l’environnement, contaminer les sols, les eaux et s’accumuler dans les organismes vivants. <br/>\
                                    Chez l’homme, une exposition prolongée ou répétée aux PFOA a été associée à plusieurs effets préoccupants sur la santé. Des études scientifiques ont notamment mis en évidence des liens possibles avec une augmentation du taux de cholestérol, des perturbations du fonctionnement du foie, des effets sur le système immunitaire, ainsi que des impacts sur le développement du fœtus et la fertilité. Le PFOA est également classé comme cancérogène (CIRC, groupe 1) en raison d’un lien établi avec certains cancers, notamment le cancer du rein et des testicules.<br/>\
                                    Face à ces risques, l’utilisation des PFOA est aujourd’hui fortement limitée. Le PFOA est inscrit à la Convention de Stockholm sur les polluants organiques persistants, ce qui entraîne son interdiction ou sa restriction à l’échelle internationale, avec quelques exceptions spécifiques. En Europe, sa fabrication et son utilisation sont également très encadrées dans le cadre de la réglementation REACH. <br/>\
                                    À retenir : même lorsqu’un produit n’entraîne pas d’effet immédiat visible, une exposition répétée peut avoir des conséquences à long terme. La connaissance des dangers, le respect des procédures de sécurité et la réduction des expositions sont essentielles pour protéger la santé humaine et l’environnement.<br/>\
                                    <strong>Pour en savoir plus:</strong><br/>\
                                    <a href='https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/'>https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/ </a> <br/>\
                                    <a href='https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes'>https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes </a>\
                                    "
    text_correction = "<strong> Corrections </strong> <br/> <br/> <strong>" + text_question1 + " :</strong> " + question1C + "<br/><br/> <strong>" + text_question2 + " </strong> " + question2C + "<br/><br/> <strong>" + text_question3 +  " </strong> : " + question3A + "<br/> <br/> <strong>" + text_question4 +  "</strong> : " + question4A + "<br/> <br/> <strong>" + text_question5 +  " </strong> : " + question5A +", "+ question5B +", "+ question5F +", "+ question5G + "<br/><br/><strong>" + text_question6 +  "</strong> : " + question6A +", "+ question6C +", "+ question6D + ", "+ question6E + "<br/><br/><strong>"+ text_question7 +  " </strong>: " + question7A +", "+ question7B +", "+ question7C
else:
    title_site = "SysTox Game"
    subheader_title = "Alert in labs !"
    intro_equipe = "This educational escape game was developed by the SysTox INSERM team at the Université Paris Cité, France (https://systox.u-paris-sciences.fr/ )."
    text_intro ="<strong>Welcome to Your Mission!</strong><br/><br/>\
    You are an intern working in a university laboratory. At 4:15 p.m., while you are alone in the lab...<br/>\
    <strong>BEEP! BEEP! BEEP!</strong><br/>\
    An alarm suddenly goes off. A vial containing a toxic chemical has been spilled in the analytical chemistry laboratory.<br/>\
    Time is running out! Your mission is to assess the situation, secure the area, and respond without putting yourself or others at risk.<br/>\
    Each correct answer will reveal a character of the final code. A wrong decision could make the situation worse...<br/>\
    Will you be able to handle the situation?        "
    warning_time = "Oh no ! Time is out !"
    initialisation_button = "C'est parti !"
    validermesreponses = "Valider mes réponses"
    felicitationcode = ":sparkles: félicitations vous avez trouvé un code  :sparkles: "
    #niveau1
    text_bulle_mission1 = "A vial containing a toxic powder has spilled onto the laboratory bench. React quickly!"
    text_question1 = "What should be your first action?"
    mission_1 = "Task 1!"
    question1A = "A. Pick up the flask immediately"
    question1B = "B. Leave the room"
    question1C = "C. Identify the substance"
    question1D = "D. Clean it up with paper towels and distilled water"
    question1E = "E. Continue your experiment"
    mission_2 = "Task 2!"
    text_bulle_mission2= "The alarm is still sounding. A strong odor is spreading throughout the laboratory. Ventilation is inadequate, and another student is still nearby."
    text_question2 = "Even if the student hasn’t any symptoms, this means:"
    question2A = "A. They haven’t been exposed."
    question2B = "B. Their PPE completely prevents exposure."
    question2C = "C. Exposure is possible, and some health effects may be delayed."
    question2D = "D. The substance is harmless."
    question2E = "E. None of the above."
    mission_3 = "Task 3!"
    text_bulle_mission3 = "The label on the flask is unreadable, but the hazard pictograms are still visible."
    text_question3 = " What do they indicate?"
    question3A = "A. Acute toxicity, skin corrosion/irritation, respiratory sensitization"
    question3B = "B.  Explosive, skin corrosion/irritation, acute toxicity"
    question3C = "C. Hazardous to the aquatic environment and human health, skin irritant, acute toxicity"
    question3D = "D. Flammable gas, skin irritant, CMR (Carcinogenic, Mutagenic, Reprotoxic)"
    question3E = "E. None of the above"
    mission_4 = "Task 4!"
    text_bulle_mission4= "The IUPAC name and therefore the chemical structure of the substance is still visible. Using the laboratory chemical catalog, identify the compound."
    text_question4 = "Which compound corresponds to this structure?"
    question4A = "A. Perfluorooctanoic acid (PFOA)"
    question4B = "B. Perfluorononanoic acid (PFNA)"
    question4C = "C. Heptafluorobutanoic acid (PFBA)"
    question4D = "D. Perfluorodecanoic acid (PFDA)"
    question4E = "E. Perfluoroheptanoic acid (PFHpA)"
    question4F = "F. None of the above"
    mission_5 = "Task 5!"
    text_bulle_mission5 = "he substance has now been identified. Consult its Safety Data Sheet (SDS):<br/>\
H318: Causes serious eye damage.<br/>\
H332: Harmful if inhaled.<br/>\
H351: Suspected of causing cancer.<br/>\
H372 - Causes damage to organs through prolonged or repeated exposure."       
    text_question5 = "Which personal protective equipment (PPE) should you wear before responding?"
    question5A ="A. Safety glasses"
    question5B ="B. Suitable nitrile gloves"
    question5C ="C. Household latex gloves"
    question5D ="D. Appropriate respiratory protective mask"
    question5E ="E. Cartridge respirator"
    question5F ="F. Laboratory coat"
    question5G ="G. FFP3 mask respirator"
    mission_6 = "Task 6!"
    text_bulle_mission6 = "The identified substance belongs to the PFAS family, often referred to as \"forever chemicals.\""
    text_question6 = "Which of the following statements are true?"
    question6A ="A. Some PFAS may have harmful effects on human health."
    question6B ="B. They break down rapidly when exposed to sunlight."
    question6C ="C. They are extremely stable and persistent in the environment."
    question6D ="D. They can travel long distances and contaminate water and soil."
    mission_7 = "Task 7!"
    question6E ="E. They can accumulate in living organisms."
    text_bulle_mission7 = "Bravo ! L’incident est maîtrisé. Vous avez appliqué les bonnes mesures de sécurité. Pour éviter de futurs accidents, quelles bonnes pratiques adopter ? "
    text_question7 = "To help prevent future accidents, which good laboratory practices should be followed?"
    question7A = "A. Keep all chemical containers clearly labeled."
    question7B = "B. Store unused chemicals in appropriate storage cabinets."
    question7C = "C. Clearly indicate the presence of hazardous substances."
    question7D = "D. Install surveillance cameras in the laboratory."
    question7E = "E. None of the above. "
    text_avant_code ="That's it. You're almost there. Now write down the letters and numbers you got to check your answers!"
    text_input_code = "Your code :"
    text_erreur_code = "Oh no, you failed.."
    text_bravo_code = "BRAVO :sparkles:"   
    text_bulle_fin = "Bravo ! Great job ! <br/> <br/>Did you know?\
                                    Did You Know? <br/> <br/>\
                                    PFOA: A Chemical of Concern for Human Health and the Environment <br/> \
                                    Perfluorooctanoic acid (PFOA) belongs to the PFAS family, commonly known as \"forever chemicals\" because of their exceptional resistance to degradation. These substances can persist in the environment for decades, contaminating soil, groundwater, surface water, and living organisms.<br/> \
                                    In humans, repeated or long-term exposure to PFOA has been associated with several adverse health effects. Scientific studies have reported possible links with increased cholesterol levels, liver dysfunction, impaired immune response, developmental effects in fetuses, and reduced fertility. PFOA has also been classified as carcinogenic to humans (IARC Group 1) due to sufficient evidence linking exposure to cancers, particularly kidney and testicular cancer.<br/> \
                                    Because of these risks, the use of PFOA is now strictly regulated worldwide. It is listed under the Stockholm Convention on Persistent Organic Pollutants, resulting in international bans or restrictions with only limited exemptions. Within the European Union, its manufacture and use are also tightly regulated under the REACH Regulation.<br/><br/> \
                                    <strong>Key Takeaway</strong><br/> \
                                    Even when no immediate symptoms are observed, repeated exposure to hazardous chemicals may have long-term health consequences. Understanding chemical hazards, following laboratory safety procedures, and minimizing exposure are essential for protecting both human health and the environment.<br/> \
                                    Learn more: <br/> \
                                    <a href='https://www.anses.fr/en/content/pfass-very-persistent-chemicals'> https://www.anses.fr/en/content/pfass-very-persistent-chemicals</a><br/> \
                                    <a href ='https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas'> https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas</a>"
    text_bulle_fin_echec = "oh no ! You failed ...<br/> <br/>Did you know?\
                                    Did You Know? <br/> <br/>\
                                    PFOA: A Chemical of Concern for Human Health and the Environment <br/> \
                                    Perfluorooctanoic acid (PFOA) belongs to the PFAS family, commonly known as \"forever chemicals\" because of their exceptional resistance to degradation. These substances can persist in the environment for decades, contaminating soil, groundwater, surface water, and living organisms.<br/> \
                                    In humans, repeated or long-term exposure to PFOA has been associated with several adverse health effects. Scientific studies have reported possible links with increased cholesterol levels, liver dysfunction, impaired immune response, developmental effects in fetuses, and reduced fertility. PFOA has also been classified as carcinogenic to humans (IARC Group 1) due to sufficient evidence linking exposure to cancers, particularly kidney and testicular cancer.<br/> \
                                    Because of these risks, the use of PFOA is now strictly regulated worldwide. It is listed under the Stockholm Convention on Persistent Organic Pollutants, resulting in international bans or restrictions with only limited exemptions. Within the European Union, its manufacture and use are also tightly regulated under the REACH Regulation.<br/><br/> \
                                    <strong>Key Takeaway</strong><br/> \
                                    Even when no immediate symptoms are observed, repeated exposure to hazardous chemicals may have long-term health consequences. Understanding chemical hazards, following laboratory safety procedures, and minimizing exposure are essential for protecting both human health and the environment.<br/> \
                                    Learn more: <br/> \
                                    <a href='https://www.anses.fr/en/content/pfass-very-persistent-chemicals'> https://www.anses.fr/en/content/pfass-very-persistent-chemicals</a><br/> \
                                    <a href ='https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas'> https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas</a>"
    text_correction = "<strong> Correction </strong> <br/> <br/> <strong>" + text_question1 + " :</strong> " + question1C + "<br/><br/> <strong>" + text_question2 + " </strong> " + question2C + "<br/><br/> <strong>" + text_question3 +  " </strong> : " + question3A + "<br/> <br/> <strong>" + text_question4 +  "</strong> : " + question4A + "<br/> <br/> <strong>" + text_question5 +  " </strong> : " + question5A +", "+ question5B +", "+ question5F +", "+ question5G + "<br/><br/><strong>" + text_question6 +  "</strong> : " + question6A +", "+ question6C +", "+ question6D + ", "+ question6E + "<br/><br/><strong>"+ text_question7 +  " </strong>: " + question7A +", "+ question7B +", "+ question7C

st.title(title_site)
st.subheader(subheader_title)
st.write(intro_equipe)
st.write(text_avant_code)
reponse_utilisateur = st.text_input(text_input_code)
if reponse_utilisateur != "": 
    if reponse_utilisateur == "5Y5T0X!":
        st.session_state.reussite = True
    else:
        st.session_state.reussite = False
if st.session_state.reussite == True:
    st.badge(text_bravo_code, color = "green")
    st.image("img/mascotte_reussite.png")
    with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
        st.markdown(text_bulle_fin, unsafe_allow_html=True)
        temps_choisi = 10000000000000 
    with st.chat_message("SysTox", avatar="img/mascotte_prof.png"):
        st.markdown(text_correction, unsafe_allow_html=True)
        temps_choisi = 10000000000000         
else:
    st.badge(text_erreur_code, color = "red")
    st.image("img/mascotte_gameover.png")
    with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
        st.markdown(text_bulle_fin_echec, unsafe_allow_html=True)
    temps_choisi = 10000000000000
    with st.chat_message("SysTox", avatar="img/mascotte_prof.png"):
                st.markdown(text_correction, unsafe_allow_html=True)
                temps_choisi = 10000000000000 


