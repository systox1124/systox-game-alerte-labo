import streamlit as st
import time 
from datetime import datetime, timedelta
from PIL import Image
import base64
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components

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

    
def show_escape_mobile():
    st_autorefresh(interval=50000, key="refresh")
    st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
    st.markdown("""
<style>
    /* Réduire les marges générales */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* Réduire l'espace au-dessus des éléments */
    .stMainBlockContainer {
        padding-top: 0rem !important;
    }

    /* Masquer l'en-tête Streamlit */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Réduire les marges des titres */
    h1, h2, h3 {
        margin-top: 0.3rem !important;
    }

    div[data-testid="stRadioGroup"] div[role="radiogroup"] {
        padding: 0 !important;
        margin: 0 !important;
        min-height: 0 !important;
    }
    /* Cache le rond radio */
    div[role="radiogroup"] > label > div:first-child {
        display: none;
    }

div[data-testid="stRadioGroup"]
label[data-testid="stRadioOption"]
> div
> div
> div:first-child {
    display: none;
}
    /* Carte radio */
    div[role="radiogroup"] label {

        background: white;

        border: 3px solid black;

        border-radius: 20px;

        padding: 12px 18px;

        margin: 0px;

        box-shadow: 4px 4px 0px black;

        cursor: pointer;

        transition: all 0.15s ease;
    }

    /* Hover */
    div[role="radiogroup"] label:hover {

        transform: translate(-2px, -2px);

        box-shadow: 6px 6px 0px black;
    }

    /* Option sélectionnée */

    div[role="radiogroup"] label:has(input:checked) {

        background: #4F73D1 !important;
        color: white !important;
        transform: translate(2px, 2px);

        box-shadow: 2px 2px 0px black;
    }

    div[data-testid="radiogroup"] label:has(input:checked)
    [data-testid="stMarkdownContainer"] {
        background: #4F73D1 !important;
        color: white !important;
        background: #4F73D1 !important;
    }

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
            //display: none;
        }
        </style>
        """, unsafe_allow_html=True)
    
    
    b64_systox = img_to_base64("img/logo_systox.png")
    st.markdown(f"""
                                    <div style="display:flex; justify-content:flex-end;">
                                        <img src="data:image/png;base64,{b64_systox}" style="width:50px;">
                                    </div>
                                    """, unsafe_allow_html=True) 
    lang = st.radio("", ["🇫🇷 FR",'🇬🇧 EN'], horizontal=True,label_visibility="collapsed")
    st.session_state["langue"] = lang
    if lang == "🇫🇷 FR":
        title_site = "SysTox Game"
        subheader_title = "Alerte au laboratoire !"
        intro_equipe = "Cet escape game pédagogique a été conçu et développé par l'équipe SysTox de l'INSERM à l'Université Paris Cité (https://systox.u-paris-sciences.fr/)"
        text_intro ="<strong>Bienvenue dans votre mission !</strong><br> Vous incarnez un stagiaire dans un laboratoire universitaire.<br> <strong> À 16 h 15…</strong> Alors que vous êtes seul dans le laboratoire lorsque,…<br> <strong>BIP ! BIP ! BIP !</strong><br> Une alarme retentit. Un flacon contenant un produit toxique vient s'est renversé sur la paillasse de la salle de chimie analytique.<br><br> Le temps presse. Vous devez analyser la situation, sécuriser les lieux et agir sans mettre votre santé ni celle des autres en danger.<br><br> <strong> Attention !</strong> Chaque décision vous révélera un chiffre ou une lettre du <strong>code final</strong>. Une erreur pourrait aggraver l'incident... </strong><br><br> Saurez-vous garder votre sang-froid ?"
        #text_intro = "<strong>Bonjour !</strong><br><br> Vous êtes dans la peau d’un stagiaire en laboratoire universitaire."
        warning_time = "Cela fait plus de 1 minutes."
        initialisation_button = "C'est parti !"
        validermesreponses = "Valider mes réponses"
        felicitationcode = ":sparkles: Félicitations !:sparkles:" 
        text_felicitation = "Vous avez trouvé un code"
        #niveau1
        mission_1 = "Mission 1 !"
        mission_2 = "Mission 2 !"
        mission_3 = "Mission 3 !"
        mission_4 = "Mission 4 !"
        mission_5 = "Mission 5 !"
        mission_6 = "Mission 6 !"
        mission_7 = "Mission 7 !"
        text_bulle_mission1 = "VITE! Un flacon contenant une poudre toxique s'est renversé sur la paillasse. Réagissez rapidement!"
        text_question1 = "Mission 1 : Quels sont vos premiers réflexes ?"
        question1A = "A. Ramasser immédiatement le flacon"
        question1B = "B. Quitter la pièce"
        question1C = "C. Identifier le produit"
        question1D = "D. Nettoyer avec du papier absorbant puis de l’eau distillée"
        question1E = "E. Continuer vos manipulations"
        text_bulle_mission2= "L'alarme retentit toujours.\
        Une forte odeur se répand dans le laboratoire.La ventilation est insuffisante et un étudiant est encore présent à proximité."
        text_question2 = "Même sans symptôme, cela signifie:"
        question2A = "A. Il n'a pas été exposé"
        question2B = "B. Exposition impossible ! Son EPI (équipement de protection individuelle) empêche toute exposition."
        question2C = "C. L'exposition est possible avec des effets retardés."
        question2D = "D. La substance est inoffensive"
        question2E = "E. Aucune de ces réponses"
        text_bulle_mission3 = "L’étiquette du flacon est illisible, mais les pictogrammes de danger restent visibles."
        text_question3 = "Que vous indiquent-ils ?"
        question3A = "A. CMR (Cancérogène, Mutagène, Reprotoxique), nocif/irritant, corrosif"
        question3B = "B. Explosif, corrosion/irritation cutanée, toxicité aiguë"
        question3C = "C. Danger pour le milieu aquatique et l’homme, irritant cutané, toxicité aiguë"
        question3D = "D. Gaz inflammable, irritant cutané, CMR (Cancérogène, Mutagène, Reprotoxique)"
        question3E = "E. Aucune de ces réponses "
        text_bulle_mission4= "La nomenclature de l'IUPAC et donc la structure chimique du produit est encore visible. À l’aide du catalogue du laboratoire, identifiez la substance."
        text_question4 = "Quelle molécule correspond à cette structure ?"
        question4A = "A.  Acide pentadécafluorooctanoïque (PFOA)"
        question4B = "B.  Acide perfluorononanoïque (PFNA)"
        question4C = "C.  Acide heptafluorobutanoïque (PFBA)"
        question4D = "D.  Acide perfluorodécanoïque (PFDA)"
        question4E = "E.  Acide perfluoroheptanoïque (PFHpA)"
        question4F = "F.  Aucune de ces réponses"
        text_bulle_mission5 = "La substance est identifiée. Consultez sa fiche de données de sécurité : <br>H318 : provoque des lésions oculaires graves. <br>H351 : susceptible de provoquer le cancer. <br>H315 : provoque une irritation cutanée."
        text_question5 = "Quels équipements de protection individuelle (EPI) devez-vous choisir avant toute intervention ?"
        question5A ="A. Lunettes de protection"
        question5B ="B. Gants nitrile adaptés"
        question5C ="C. Gants de vaisselle en latex"
        question5D ="D. Masque de protection respiratoire adapté"
        question5E ="E. Respirateur à cartouche"
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
        question7E = "E. Aucune de ces réponses  "
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
                                    "\
                                    
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
        initialisation_button = "Go!"
        validermesreponses = "Submit my answers!"
        felicitationcode = ":sparkles: Congrats :sparkles: "
        text_felicitation = "You found a code"
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
        text_question2 = "Even if the student doesn’t have any symptoms, this means:"
        question2A = "A. He has not been exposed."
        question2B = "B. Its PPE completely prevents exposure."
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
        text_bulle_mission5 = "The substance has now been identified. Consult its Safety Data Sheet (SDS):<br/>\
H318: Causes serious eye damage.<br/>\
H332: Harmful if inhaled.<br/>\
H351: Suspected of causing cancer.<br/>\
H372 - Causes damage to organs through prolonged or repeated exposure."       
        text_question5 = "Which personal protective equipment (PPE) should you wear before doing any expriment ?"
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
        text_bulle_mission7 = "Well done! The incident is under control. You have followed the appropriate safety measures."
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
    st.title(title_site)
    st.subheader(subheader_title)
    st.write(intro_equipe) 
    temps_choisi = 10 
    init_state()
    if st.session_state.etape >= 0 and "end" not in st.session_state and st.session_state.etape <9:
        with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
            st.markdown(text_intro, unsafe_allow_html=True)
            if st.button(initialisation_button):
                if "debut" not in st.session_state:
                    st.session_state.debut =datetime.now()
                    etape_suivante()
                    st.session_state.scroll_flag_init = True
                    if st.session_state.get("scroll_flag_init"):
                        components.html(
                            """
                            <script>
                                window.parent.document.getElementById('ancre-mission1')
                                    .scrollIntoView({behavior: 'smooth', block: 'start'});
                            </script>
                            """,
                            height=0,
                        )
                        st.session_state.scroll_flag_init = False
    if "debut" in st.session_state:
        if datetime.now() - st.session_state.debut > timedelta(minutes=temps_choisi):
            st.session_state.end = True
            st.badge(warning_time, color="red")
            st.image("img/mascotte_gameover.png")
            st.session_state.end = True
        else:
            if st.session_state.etape >=1 and st.session_state.etape <9:
                st.markdown('<div id="ancre-mission1"></div>', unsafe_allow_html=True)
                st.subheader(mission_1)
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission1, unsafe_allow_html=True)
                st.write(text_question1)
                selectionreflex = []
                res_reflexes = [question1C]
                if st.checkbox(question1A):
                    selectionreflex.append(question1A)
                if st.checkbox(question1B):
                    selectionreflex.append(question1B)
                if st.checkbox(question1C):
                    selectionreflex.append(question1C)
                if st.checkbox(question1D):
                    selectionreflex.append(question1D)
                if st.checkbox(question1E):
                    selectionreflex.append(question1E)
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button = st.button(validermesreponses, key ="reflexes")
                    if test_button:
                        if "buttonreflex" not in st.session_state:
                            st.session_state.buttonreflex=True
                    if "buttonreflex" in st.session_state:
                        if set(selectionreflex) == set(res_reflexes):
                            st.markdown('<div id="ancre-mission2"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": 5")
                            b64_1_1 = img_to_base64("img/mascotte_5.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_1_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission2"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": 0")
                            #st.badge(felicitationcode + ": 0 ", color = "blue")
                            b64_1_2 = img_to_base64("img/mascotte_0.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_1_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape2" not in st.session_state:
                            st.session_state.etape2 = True
                            etape_suivante()
                            st.session_state.scroll_flag_mission1 = True
                            if st.session_state.get("scroll_flag_mission1"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission2')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission1 = False                            
            if st.session_state.etape >=2 and st.session_state.etape <9:
                st.subheader(mission_2)
                st.markdown('<div id="ancre-mission2"></div>', unsafe_allow_html=True)
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission2, unsafe_allow_html=True)
                st.write(text_question2)                  
                selectionexpo = []
                res_expo = [question2C]
                if st.checkbox(question2A):
                    selectionexpo.append(question2A)
                if st.checkbox(question2B):
                    selectionexpo.append(question2B)
                if st.checkbox(question2C):
                    selectionexpo.append(question2C)
                if st.checkbox(question2D):
                    selectionexpo.append(question2D)
                if st.checkbox(question2E):
                    selectionexpo.append(question2E)           
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button2 = st.button(validermesreponses, key ="expo")
                    if test_button2:
                        if "buttonexpo" not in st.session_state:
                            st.session_state.buttonexpo=True
                    if "buttonexpo" in st.session_state:
                        if set(selectionexpo) == set(res_expo):
                            st.markdown('<div id="ancre-mission3"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": Y")
                            #st.badge(felicitationcode +": Y", color = "blue")
                            b64_2_1 = img_to_base64("img/mascotte_Y.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_2_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission3"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": T")
                            #st.badge(felicitationcode + ": T", color = "blue")
                            b64_2_2 = img_to_base64("img/mascotte_T.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_2_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape3" not in st.session_state:
                            st.session_state.etape3 = True
                            etape_suivante()
                            st.session_state.scroll_flag_mission2 = True
                            if st.session_state.get("scroll_flag_mission2"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission3')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission2 = False
                        
        if st.session_state.etape >=3 and st.session_state.etape <9:
                st.subheader(mission_3)
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission3, unsafe_allow_html=True)
                combined = merge_images_side_by_side(["img/unnamed.jpg", "img/unnamed-2.png", "img/unnamed.png"])
                combined.save("img/combined.png")
                st.image("img/combined.png", use_container_width=True)
                st.write(text_question3)                  
                selectioninfo= []
                res_info = [question3A]
                if st.checkbox(question3A):
                    selectioninfo.append(question3A)
                if st.checkbox(question3B):
                    selectioninfo.append(question3B)
                if st.checkbox(question3C):
                    selectioninfo.append(question3C)
                if st.checkbox(question3D):
                    selectioninfo.append(question3D)
                if st.checkbox(question3E):
                    selectioninfo.append(question3E)           
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button3 = st.button(validermesreponses, key ="info")
                    if test_button3:
                        if "buttoninfo" not in st.session_state:
                            st.session_state.buttoninfo=True
                    if "buttoninfo" in st.session_state:
                        if set(selectioninfo) == set(res_info):
                            st.markdown('<div id="ancre-mission4"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": 5")
                            
                            #st.badge(felicitationcode+ ": 5", color = "blue")
                            b64_3_1 = img_to_base64("img/mascotte_5.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_3_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission4"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": !")

#                            st.badge(felicitationcode + ": !", color = "blue")
                            b64_3_2 = img_to_base64("img/mascotte_pointexc.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_3_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape4" not in st.session_state:
                            st.session_state.etape4 = True
                            etape_suivante()
                            st.session_state.scroll_flag_mission3 = True
                            if st.session_state.get("scroll_flag_mission3"):
                                components.html(
                                        """
                                        <script>
                                            window.parent.document.getElementById('ancre-mission4')
                                                .scrollIntoView({behavior: 'smooth', block: 'start'});
                                        </script>
                                        """,
                                        height=0,
                                    )
                                st.session_state.scroll_flag_mission3 = False
                           
        if st.session_state.etape >=4 and st.session_state.etape <9:
                st.subheader(mission_4)
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission4, unsafe_allow_html=True)
                _, col_img4, _=st.columns([1,1,1])
                with col_img4:
                    st.image("img/unnamed-4.png")
                st.write(text_question4)                  
                selectionstrag = []
                res_strag = [question4A]
                if st.checkbox(question4A):
                    selectionstrag.append(question4A)
                if st.checkbox(question4B):
                    selectionstrag.append(question4B)
                if st.checkbox(question4C):
                    selectionstrag.append(question4C)
                if st.checkbox(question4D):
                    selectionstrag.append(question4D)
                if st.checkbox(question4E):
                    selectionstrag.append(question4E)           
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button4 = st.button(validermesreponses, key ="strag")
                    if test_button4:
                        if "buttonstrag" not in st.session_state:
                            st.session_state.buttonstrag=True
                    if "buttonstrag" in st.session_state:
                        if set(selectionstrag) == set(res_strag):
                            st.markdown('<div id="ancre-mission5"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.markdown(text_felicitation +":T")
                            b64_4_1 = img_to_base64("img/mascotte_T.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_4_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission5"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": Y")
                            
                            #st.badge(felicitationcode+ ": Y", color = "blue")
                            b64_4_2 = img_to_base64("img/mascotte_Y.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_4_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape5" not in st.session_state:
                            st.session_state.etape5 = True
                            etape_suivante()
                            st.session_state.scroll_flag_mission4 = True
                            if st.session_state.get("scroll_flag_mission4"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission5')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission4 = False
                             
        if st.session_state.etape >=5 and st.session_state.etape <9:
                st.subheader(mission_5)                            
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission5, unsafe_allow_html=True)
                st.write(text_question5)                  
                selectionepi = []
                res_epi = [question5A, question5F, question5B, question5G]
                if st.checkbox(question5A):
                    selectionepi.append(question5A)
                if st.checkbox(question5B):
                    selectionepi.append(question5B)
                if st.checkbox(question5C):
                    selectionepi.append(question5C)
                if st.checkbox(question5D):
                    selectionepi.append(question5D)
                if st.checkbox(question5E):
                    selectionepi.append(question5E)
                if st.checkbox(question5F):
                    selectionepi.append(question5F) 
                if st.checkbox(question5G):
                    selectionepi.append(question5G)           
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button5 = st.button(validermesreponses, key ="epi")
                    if test_button5:
                        if "buttonepi" not in st.session_state:
                            st.session_state.buttonepi=True
                    if "buttonepi" in st.session_state:
                        if set(selectionepi) == set(res_epi):
                            st.markdown('<div id="ancre-mission6"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": 0")
                            
                            #st.badge(felicitationcode +": 0", color = "blue")
                            b64_5_1 = img_to_base64("img/mascotte_0.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_5_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission6"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": 5")                           
                            #st.badge(felicitationcode +": 5", color = "blue")
                            b64_5_2 = img_to_base64("img/mascotte_5.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_5_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape6" not in st.session_state:
                            etape_suivante()
                            st.session_state.etape6 = True
                            st.session_state.scroll_flag_mission5 = True
                            if st.session_state.get("scroll_flag_mission5"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission6')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission5 = False                            
        if st.session_state.etape >=6 and st.session_state.etape <9:
                st.subheader(mission_6)              
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission6, unsafe_allow_html=True)
                st.write(text_question6)                  
                selection_pfas = []
                res_pfas = [question6A, question6C, question6D, question6E]
                if st.checkbox(question6A):
                    selection_pfas.append(question6A)
                if st.checkbox(question6B):
                    selection_pfas.append(question6B)
                if st.checkbox(question6C):
                    selection_pfas.append(question6C)
                if st.checkbox(question6D):
                    selection_pfas.append(question6D)
                if st.checkbox(question6E):
                    selection_pfas.append(question6E)        
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button6 = st.button(validermesreponses, key ="pfas")
                    if test_button6:
                        if "buttonpfas" not in st.session_state:
                            st.session_state.buttonpfas=True
                    if "buttonpfas" in st.session_state:
                        if set(selection_pfas) == set(res_pfas):
                            st.markdown('<div id="ancre-mission7"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": X")
                            #st.badge(felicitationcode + ": X", color = "blue")
                            b64_6_1 = img_to_base64("img/mascotte_X.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_6_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission7"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": T")
#                            st.badge(felicitationcode + ": T", color = "blue")
                            b64_6_2 = img_to_base64("img/mascotte_T.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_6_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape7" not in st.session_state:
                            etape_suivante()
                            st.session_state.etape7 = True
                            if st.session_state.get("scroll_flag_mission6"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission7')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission6 = False                            
        if st.session_state.etape >=7 and st.session_state.etape <9:
                st.subheader(mission_7)
                with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
                    st.markdown(text_bulle_mission7, unsafe_allow_html=True)
                st.write(text_question7)                  
                selection_prevention = []
                res_prevention = [question7A, question7C, question7B]
                if st.checkbox(question7A):
                    selection_prevention.append(question7A)
                if st.checkbox(question7B):
                    selection_prevention.append(question7B)
                if st.checkbox(question7C):
                    selection_prevention.append(question7C)
                if st.checkbox(question7D):
                    selection_prevention.append(question7D)
                if st.checkbox(question7E):
                    selection_prevention.append(question7E)        
                _,centrebutton,_ = st.columns(3)
                with centrebutton:
                    test_button7 = st.button(validermesreponses, key ="prevention")
                    if test_button7:
                        if "buttonprevention" not in st.session_state:
                            st.session_state.buttonprevention=True
                    if "buttonprevention" in st.session_state:
                        if set(selection_prevention) == set(res_prevention):
                            st.markdown('<div id="ancre-mission8"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": !")

#                            st.badge(felicitationcode + ": !", color = "blue")
                            b64_7_1 = img_to_base64("img/mascotte_pointexc.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_7_1}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown('<div id="ancre-mission8"></div>', unsafe_allow_html=True)
                            st.badge(felicitationcode, color = "blue")
                            st.write(text_felicitation + ": Y")

#                            st.badge(felicitationcode + ": Y", color = "blue")
                            b64_7_2 = img_to_base64("img/mascotte_Y.png")
                            st.markdown(f"""
                            <div style="display:flex; justify-content:center;">
                                <img src="data:image/png;base64,{b64_7_2}" style="width:250px;">
                            </div>
                            """, unsafe_allow_html=True)
                        if "etape8" not in st.session_state:
                            etape_suivante()
                            st.session_state.etape8 = True
                            st.session_state.scroll_flag_mission7 = True
                            if st.session_state.get("scroll_flag_mission7"):
                                components.html(
                                    """
                                    <script>
                                        window.parent.document.getElementById('ancre-mission8')
                                            .scrollIntoView({behavior: 'smooth', block: 'start'});
                                    </script>
                                    """,
                                    height=0,
                                )
                                st.session_state.scroll_flag_mission7 = False
                            
        if st.session_state.etape >= 8:
            st.write(text_avant_code)
            reponse_utilisateur = st.text_input(text_input_code)
            if reponse_utilisateur =="":
                st.write("")
            elif reponse_utilisateur == "5Y5T0X!":
                st.session_state.reussite = True
                st.switch_page("resultat_mobile.py")
            else:
                st.session_state.reussite = False
                st.switch_page("resultat_mobile.py")
            # if reponse_utilisateur =="":
            #     st.write("")
            # elif reponse_utilisateur == "5Y5T0X!":
            #     etape_suivante()
            #     st.badge(text_bravo_code, color = "green")
            #     st.image("img/mascotte_reussite.png")
            #     with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
            #         st.markdown(text_bulle_fin, unsafe_allow_html=True)
            #     temps_choisi = 10000000000000             
            # else:
            #     etape_suivante()
            #     st.badge(text_erreur_code, color = "red")
            #     st.image("img/mascotte_gameover.png")
            #     with st.chat_message("SysTox", avatar="img/avatar_mascotte-aquarelle.png"):
            #         st.markdown(text_bulle_fin_echec, unsafe_allow_html=True)
            #     temps_choisi = 10000000000000 
                
#show_escape_mobile()