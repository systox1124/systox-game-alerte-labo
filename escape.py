import streamlit as st
import time  
from datetime import datetime, timedelta
import streamlit.components.v1 as components

from streamlit_autorefresh import st_autorefresh

def init_state():   
        if "etape" not in st.session_state:
            st.session_state.etape = 0

def etape_suivante():
    st.session_state.etape +=1

def create_bulle(text):
    placeholder = st.empty()
    texte_complet = ""
    for mot in text.split():
        texte_complet += mot + " "
        placeholder.markdown(
            f"""
            <div class="speech-bubble">
                {texte_complet}
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.04)

def affiche(id_bulle, texte):
    if id_bulle not in st.session_state:
        create_bulle(texte)
        st.session_state[id_bulle] = 1
    else:
        st.markdown(
        f"""
        <div class="speech-bubble">
            {texte}
        </div>
        """,
        unsafe_allow_html=True)
        
def create_bulle_droite(text):
    placeholder = st.empty()
    texte_complet = ""
    for mot in text.split():
        texte_complet += mot + " "
        placeholder.markdown(
        f"""
        <div class="speech-bubble-right">
            {texte_complet}
        </div>
        """,
        unsafe_allow_html=True
    )
        time.sleep(0.04)

def affiche_droite(id_bulle, texte):
    if id_bulle not in st.session_state:
        create_bulle_droite(texte)
        st.session_state[id_bulle] = 1
    else:
        st.markdown(
        f"""
        <div class="speech-bubble-right">
            {texte}
        </div>
        """,
        unsafe_allow_html=True)  
def escape():

    st_autorefresh(interval=15000, key="refresh")
    st.set_page_config(layout="wide")
    # CSS bulle gauche et droite   
              
    st.markdown(
        """
        <style>
        .speech-bubble {
            position: relative;
            background: white!important;
            border: 4px solid #222;
            border-radius: 25px;
            padding: 25px;
            margin-top: 0px;
            margin-bottom: 20px;
            line-height: 1.6;
            color: #000000 !important;
            box-shadow: 4px 4px 10px rgba(0,0,0,0.15);
            width: 70%;
            max-width: 650px;
            min-height: 180px;
            font-size: 1.1rem;
        }

        /* Contour noir de la queue */
        .speech-bubble:before {
            content: "";
            position: absolute;
            left: -32px;
            top: 70px;
            width: 0;
            height: 0;
            border-top: 18px solid transparent;
            border-bottom: 18px solid transparent;
            border-right: 32px solid #14203E;
        }

        /* Intérieur blanc de la queue */
        .speech-bubble:after {
            content: "";
            position: absolute;
            left: -26px;
            top: 72px;
            width: 0;
            height: 0;
            border-top: 16px solid transparent;
            border-bottom: 16px solid transparent;
            border-right: 28px solid white;
        }
        
        .speech-bubble-right {
        position: relative;
        background: white;
        border: 4px solid #222;
        border-radius: 25px;
        padding: 25px;
        margin-top: 40px;
        margin-bottom: 20px;
        width: 70%;
        max-width: 650px;
        min-height: 180px;
        font-size: 1.1rem;
    }

    /* contour noir */
    .speech-bubble-right:before {
        content: "";
        position: absolute;
        right: -32px;
        top: 70px;

        width: 0;
        height: 0;

        border-top: 18px solid transparent;
        border-bottom: 18px solid transparent;
        border-left: 32px solid #222;
    }

    /* intérieur blanc */
    .speech-bubble-right:after {
        content: "";
        position: absolute;
        right: -26px;
        top: 72px;

        width: 0;
        height: 0;

        border-top: 16px solid transparent;
        border-bottom: 16px solid transparent;
        border-left: 28px solid white;
    }


    /* Bouton principal */
    .stButton > button {
        background-color:  #FCA616;
        color: white;

        border: 3px solid #14203E;
        border-radius: 20px;

        padding: 0.6rem 1.4rem;

        font-size: 1rem;
        font-weight: bold;

        transition: all 0.15s ease;

        box-shadow: 4px 4px 0px #14203E;
    }

    /* Survol */
    .stButton > button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #14203E;
    }

    /* Clic */
    .stButton > button:active {
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px #14203E;
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

        margin-bottom: 12px;

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


    /* Cache la checkbox native */
    input[type="checkbox"] {
        display: none;
    }
div[data-testid="stCheckbox"] label > div:first-of-type {
    display: none !important;
}
    /* Carte */
    div[data-testid="stCheckbox"] label {

        background: white;

        border: 3px solid black;

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

        box-shadow: 6px 6px 0px black;
    }

    /* Sélectionné */
    div[data-testid="stCheckbox"] label:has(input:checked) {

        background: #4F73D1 !important;
        color: white !important;
        transform: translate(2px,2px);

        box-shadow: 2px 2px 0px black;
    }
    div[data-testid="stCheckbox"] label:has(input:checked)
    [data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    div[data-testid="stCheckbox"] label span:first-child {
        display: none;
    }

    /* Conteneur extérieur */
    div[data-testid="stTextInputRootElement"]{
        background: white !important;

        border: 3px solid black !important;
        border-radius: 22px !important;

        box-shadow: 4px 4px 0 black !important;

        overflow: hidden;

        transition: all .15s;
    }

    /* Conteneur intérieur */
    div[data-testid="stTextInputRootElement"] > div{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Le vrai input */
    div[data-testid="stTextInputRootElement"] input{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: black !important;
    }

    /* Focus */
    div[data-testid="stTextInputRootElement"]:focus-within{
        box-shadow: 6px 6px 0 black !important;
        transform: translate(-2px,-2px);
    }
    /* Conteneur du champ */
    div[data-testid="stTextInput"] > div > div {
        background: white !important;
        border: 3px solid black !important;
        border-radius: 20px !important;
        box-shadow: 4px 4px 0px black !important;
    }

    /* Le vrai input */
    div[data-testid="stTextInput"] input {
        background: transparent !important;
        color: black !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Placeholder */
    div[data-testid="stTextInput"] input::placeholder {
        color: #777 !important;
    }

    /* Quand le champ est sélectionné */
    div[data-testid="stTextInput"] > div > div:focus-within {
        border: 3px solid black !important;
        box-shadow: 6px 6px 0px black !important;
    }

    .block-container {
        max-width: 95%;
        padding-top: 0rem !important;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    </style>
    """, unsafe_allow_html=True)
    temps_choisi = 1000000000
    langue,vide, coltitre, vide,collogo = st.columns([1,2,3,1,2])
    
    with langue:
        lang = st.radio("", ["🇫🇷 FR",'🇬🇧 EN'], horizontal=True)
    st.session_state["langue"] = lang
    with collogo:
        st.image("img/logo_systox.png")
    if lang == "🇫🇷 FR":
        title_site = "SysTox Game"
        subheader_title = "Alerte au laboratoire !"
        intro_equipe = "Cet escape game pédagogique a été conçu et développé par l'équipe SysTox à l' INSERM - Université Paris Cité UMRS1124 (https://systox.u-paris-sciences.fr/)"
        text_intro ="<strong>Bienvenue dans votre mission !</strong><br><br> Vous incarnez un stagiaire dans un laboratoire universitaire.<br><br> <strong>A 16 h 15…</strong>  alors que vous êtes seul <br><br> <strong>BIP ! BIP ! BIP !</strong><br><br> Une alarme retentit. Un flacon contenant un produit toxique s'est renversé sur la paillasse dans la salle de chimie analytique.<br><br> Le temps presse. Vous ne disposez que de quelques minutes pour analyser une telle situation et agir prudemment.<br><br> <strong> Attention !</strong> Chaque décision vous permettra d'obtenir un chiffre du <strong>code final</strong>. Une erreur pourrait aggraver l'incident et mettre en danger votre sécurité et celle des autres occupants du bâtiment. Chaque étape vous révèlera un élément du code final qui permettra de résoudre l'enquête. <strong>Le compte à rebours est lancé…</strong><br><br> Saurez-vous garder votre sang-froid, sécuriser les lieux et quitter le laboratoire en toute sécurité ? <br/><br/> <i> A travers 7 missions, vous pourrez tester vos connaissances sur la sécurité dans la laboratoire (pictogramme, EPI), la toxicité de composés chimiques ou encore de structure chimique. </i>"
        #text_intro = "<strong>Bonjour !</strong><br><br> Vous êtes dans la peau d’un stagiaire en laboratoire universitaire."
        warning_time = "Oh non ! le temps est écoulé !"
        choix_temps = "Choisi le temps imparti (en minutes)"
        initialisation_button = "C'est parti !"
        validermesreponses = "Valider mes réponses"
        felicitationcode = ":sparkles: félicitations vous avez trouvé un code : :sparkles:"
        mission_1 = "Mission 1 !"
        text_bulle_mission1 = "VITE! Un flacon contenant une poudre toxique s'est renversée sur la paillasse dans la salle de chimie analytique ! Réagissez rapidement !"
        text_question1 = "Quel est votre premier réflexe ?"
        question1A = "A. Ramasser immédiatement le flacon"
        question1B = "B. Quitter la pièce"
        question1C = "C. Identifier le produit"
        question1D = "D. Nettoyer avec du papier absorbant puis de l’eau distillée"
        question1E = "E. Je continue mes manipulations"
        mission_2 = "Mission 2 !"
        text_bulle_mission2= "L'alarme continue de retentir dans le laboratoire.<br/><br/>\
       Vous savez qu'un flacon contenant une poudre toxique s'est renversé dans la salle de chimie analytique. En vous approchant prudemment de la paillasse, vous remarquez qu'une <strong>forte odeur</strong> se répand dans le laboratoire. Les fenêtres sont fermées et la <strong>ventilation semble insuffisante</strong>.<br/><br/> À quelques mètres de la zone contaminée, un étudiant est toujours présent. Évaluez la situation."
        text_question2 = "L'étudiant qui est dans le laboratoire avec vous est potentiellement exposé à la substance. Pour l'instant, il ne présente aucun symptôme visible. Cela signifie :"
        question2A = "A. Absence d’exposition : Il n'a pas été exposé, puisqu'il ne manipulait pas le flacon."
        question2B = "B. Exposition impossible : Il ne peut pas avoir été exposé, car il porte un équipement de protection individuelle (EPI)."
        question2C = "C. Exposition possible : Il a pu être exposé, mais les effets peuvent apparaître de façon retardée."
        question2D = "D. La substance est inoffensive puisqu'il ne ressent rien."
        question2E = "E. Aucune de ces réponses"
        mission_3 = "Mission 3 !"
        text_bulle_mission3 = "En vous approchant avec précaution de la paillasse, vous observez que le flacon à l’origine de l’incident est toujours renversé. L'étiquette est partiellement endommangée et <strong>le nom de la substance est malheureusement illisible</strong>.<br/><br/> Heureusement, plusieurs pictogrammes de danger sont encore visibles."
        text_question3 = "Observez attentivement les pictogrammes de danger présents sur le flacon. Que vous indiquent-ils sur les risques liés à cette substance ?"
        question3A = "A. CMR (Cancérogène, Mutagène, Reprotoxique), nocif/irritant, corrosif"
        question3B = "B. Explosif, corrosion/irritation cutanée, toxicité aiguë"
        question3C = "C. Danger pour le milieu aquatique et l’homme, irritant cutané, toxicité aiguë"
        question3D = "D. Gaz inflammable, irritant cutané, CMR (Cancérogène, Mutagène, Reprotoxique)"
        question3E = "E. Aucune de ces réponses "
        mission_4 = "Mission 4 !"
        text_bulle_mission4= "Les indices s'accumulent ! Sur le flacon la <strong>structure chimique de la substance est encore visible.</strong> <br/> Le laboratoire met à votre disposition un catalogue des produits chimiques. Celui-ci répertorie les substances avec leur nom, leur nomenclature et leur structure moléculaire. Retrouvez dans le catalogue la molécule correspondante à la structure représentée sur le flacon afin d'identifier la substance impliquée dans l'accident."
        text_question4 = "En comparant la structure chimique figurant sur le flacon avec les nomenclatures du catalogue, quel est le nom de la substance renversée ?"
        question4A = "A.  Acide perfluorooctanoïque (PFOA)"
        question4B = "B. Acide perfluorononanoïque (PFNA)"
        question4C = "C. Acide heptafluorobutanoïque (PFBA)"
        question4D = "D. Acide perfluorodécanoïque (PFDA)"
        question4E = "E. Acide perfluoroheptanoïque (PFHpA)"
        question4F = "F. Aucune de ces réponses"
        mission_5 = "Mission 5 !"
        text_bulle_mission5 = "Vous avez à présent identifié la molécule. Dès lors, vous consultez la fiche de données de sécurité afin d’identifier les dangers liés à cette substance. Elle montre qu’elle a été classé  <br>→ H318 : provoque des lésions oculaires graves<br>→ H332 : nocif par inhalation <br>→ H351 : susceptible de provoquer le cancer <br>→ H372 : Risque avéré d'effets graves pour les organes à la suite d'expositions répétées ou d'une exposition prolongée."
        text_question5 = "Quels équipements de protection individuelle (EPI) devez-vous choisir avant toute intervention afin de limiter les risques d'exposition ?"
        question5A = "A. Lunettes de protection"
        question5B ="B. Gants adaptés en nitrile"
        question5C = "C. Gants de vaisselle en latex"
        question5D = "D. Masque chirurgical"
        question5E = "E. Respirateur à cartouche"
        question5F = "F. Blouse de laboratoire"
        question5G = "G. Masque FFP3"
        text_bulle_mission6 = "On avance ! L’incident est désormais maîtrisé, mais il vous reste à comprendre les <strong>impacts à long terme</strong> de la substance identifiée. En tant qu’expert du laboratoire, vous devez déterminer les propriétés générales des PFAS (substances per- et polyfluoroalkylées), aussi appelés « polluants éternels ». <br/><br/>Identifiez les bonnes réponses pour valider vos connaissances sur ces substances et comprendre pourquoi leur gestion représente un enjeu majeur pour la sécurité chimique et environnementale."
        mission_6 =" Mission 6 !"
        text_question6 = "Parmi les propositions suivantes, quelles sont les caractéristiques des PFAS ?"
        question6A = "A. Ils peuvent présenter des effets toxiques, certains étant associés à des risques chroniques pour la santé humaine."
        question6B ="B. Ce sont des molécules qui se dégradent rapidement lorsqu’elles sont exposées à la lumière."
        question6C = "C. Ils possèdent une grande stabilité chimique, ce qui les rend très persistants dans l’environnement."
        question6D = "D. Ils peuvent se déplacer sur de longues distances dans l’environnement et contaminer les sols ainsi que les ressources en eau."
        question6E = "E. Ce sont des polluants persistants capables de s’accumuler dans les organismes vivants (bioaccumulation)."
        mission_7 = "Mission 7 !"
        text_bulle_mission7 = "L'incident est désormais terminé ! <br/><br/> Vous avez analysé la situation et agit comme cela vous semblait pertinent en essayant de garder tout le monde en sécurité. <br/> Le directeur du laboratoire a été informé et grâce à votre réactivité, l’incident a pu être maîtrisé et signalé dans le registre SST. Cependant, cet événement rappelle l’importance de rester vigilant au quotidien : une bonne organisation, le respect des consignes de sécurité et une manipulation rigoureuse des produits chimiques sont essentiels pour prévenir les accidents."
        text_question7 = "Quelles bonnes pratiques à appliquer au quotidien dans le laboratoire pourriez-vous mettre en place à l'avenir ?"
        question7A = "A. Toujours maintenir une étiquette lisible sur les flacons et la remplacer dès qu’elle est endommagée."
        question7B = "B. Ranger correctement les produits non utilisés dans une armoire."
        question7C = "C. Afficher une signalisation claire sur les murs du laboratoire indiquant la présence de substances toxiques."
        question7D = "D. Placer une caméra dans le laboratoire."
        question7E = "E. Aucune de ces réponses."
        text_avant_code ="Ca y est. Vous y êtes presque. Ecrivez maintenant les lettres et chiffres que vous avez obtenu afin de vérifier vos reponses !"
        text_input_code = "Votre code :"
        text_erreur_code = "Oh non ! Vous avez fait au moins une erreur !"
        text_bravo_code = "BRAVO :sparkles:"
        text_bulle_reussite = "Ouah Bravo ! <br/> <br/>À savoir!\
                            Les PFOA, des substances préoccupantes pour la santé et l’environnement !<br/>\
                            Ils appartiennent à la famille des PFAS, surnommés « polluants éternels » en raison de leur extrême résistance à la dégradation. Ils peuvent persister longtemps dans l’environnement, contaminer les sols, les eaux et s’accumuler dans les organismes vivants. <br/>\
                            Chez l’homme, une exposition prolongée ou répétée aux PFOA a été associée à plusieurs effets préoccupants sur la santé. Des études scientifiques ont notamment mis en évidence des liens possibles avec une augmentation du taux de cholestérol, des perturbations du fonctionnement du foie, des effets sur le système immunitaire, ainsi que des impacts sur le développement du fœtus et la fertilité. Le PFOA est également classé comme cancérogène (CIRC, groupe 1) en raison d’un lien établi avec certains cancers, notamment le cancer du rein et des testicules.<br/>\
                            Face à ces risques, l’utilisation des PFOA est aujourd’hui fortement limitée. Le PFOA est inscrit à la Convention de Stockholm sur les polluants organiques persistants, ce qui entraîne son interdiction ou sa restriction à l’échelle internationale, avec quelques exceptions spécifiques. En Europe, sa fabrication et son utilisation sont également très encadrées dans le cadre de la réglementation REACH. <br/>\
                            À retenir : même lorsqu’un produit n’entraîne pas d’effet immédiat visible, une exposition répétée peut avoir des conséquences à long terme. La connaissance des dangers, le respect des procédures de sécurité et la réduction des expositions sont essentielles pour protéger la santé humaine et l’environnement.<br/>\
                            <strong>Pour en savoir plus:</strong><br/>\
                            <a href='https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/'>https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/ </a> <br/>\
                            <a href='https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes'>https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes </a>\
                            "
        text_bulle_echec = "oh non, tu as échoué.. <br/> <br/>À savoir!\
                            Les PFOA, des substances préoccupantes pour la santé et l’environnement !<br/>\
                            Ils appartiennent à la famille des PFAS, surnommés « polluants éternels » en raison de leur extrême résistance à la dégradation. Ils peuvent persister longtemps dans l’environnement, contaminer les sols, les eaux et s’accumuler dans les organismes vivants. <br/>\
                            Chez l’homme, une exposition prolongée ou répétée aux PFOA a été associée à plusieurs effets préoccupants sur la santé. Des études scientifiques ont notamment mis en évidence des liens possibles avec une augmentation du taux de cholestérol, des perturbations du fonctionnement du foie, des effets sur le système immunitaire, ainsi que des impacts sur le développement du fœtus et la fertilité. Le PFOA est également classé comme cancérogène (CIRC, groupe 1) en raison d’un lien établi avec certains cancers, notamment le cancer du rein et des testicules.<br/>\
                            Face à ces risques, l’utilisation des PFOA est aujourd’hui fortement limitée. Le PFOA est inscrit à la Convention de Stockholm sur les polluants organiques persistants, ce qui entraîne son interdiction ou sa restriction à l’échelle internationale, avec quelques exceptions spécifiques. En Europe, sa fabrication et son utilisation sont également très encadrées dans le cadre de la réglementation REACH. <br/>\
                            À retenir : même lorsqu’un produit n’entraîne pas d’effet immédiat visible, une exposition répétée peut avoir des conséquences à long terme. La connaissance des dangers, le respect des procédures de sécurité et la réduction des expositions sont essentielles pour protéger la santé humaine et l’environnement.<br/>\
                            <strong>Pour en savoir plus:</strong><br/>\
                            <a href='https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/'>https://www.inserm.fr/c-est-quoi/polluants-eternels-cest-quoi-les-pfas/ </a> <br/>\
                            <a href='https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes'>https://www.anses.fr/fr/content/pfas-substances-chimiques-persistantes </a>\
                            "
        text_correction = "<strong> Correction </strong> <br/> <br/> <strong>" + text_question1 + " :</strong> " + question1C + "<br/><br/> <strong>" + text_question2 + " </strong> " + question2C + "<br/><br/> <strong>" + text_question3 +  " </strong> : " + question3A + "<br/> <br/> <strong>" + text_question4 +  "</strong> : " + question4A + "<br/> <br/> <strong>" + text_question5 +  " </strong> : " + question5A +", "+ question5B +", "+ question5F +", "+ question5G + "<br/><br/><strong>" + text_question6 +  "</strong> : " + question6A +", "+ question6C +", "+ question6D + ", "+ question6E + "<br/><br/><strong>"+ text_question7 +  " </strong>: " + question7A +", "+ question7B +", "+ question7C
    else:
        title_site = "SysTox Game"
        subheader_title = "Alert in labs !"
        intro_equipe = "This educational escape game was developed by the SysTox  team at the INSERM Université Paris Cité UMRS1124, France (https://systox.u-paris-sciences.fr/ )."
        text_intro ="<strong>Welcome to your mission!</strong><br><br> You are a student in a university laboratory. <strong> At 4:15 p.m.</strong>, while you are alone… <strong> BEEP! BEEP! BEEP!</strong> An alarm suddenly goes off. A vial containing a toxic substance has been knocked over on the laboratory bench in the analytical chemistry laboratory. Time is running out. <br> <br> You only have a few minutes to stabilize the situation and act carefully. <br> <br> <strong>Warning!</strong> Each good decision will allow you to obtain a digit of the final code. A wrong decision could worsen the incident and put your safety, as well as the safety of other people in the building, at risk. Each successfully completed task will reveal one digit of the secret code needed to solve the investigation. <br> <br>The countdown has started… Will you be able to stay calm, secure the area, and leave the laboratory safely?"
        warning_time = "Oh no ! Time is out !"
        initialisation_button = "Let's go !"
        validermesreponses = "Validate my answers"
        choix_temps = "Choose your time (in minutes)"
        felicitationcode = ":sparkles: Congrats you find a code : :sparkles:"
        mission_1 = "Task 1!"
        text_bulle_mission1 ="Quick! A vial containing a toxic powder has been knocked over on the laboratory bench in the analytical chemistry laboratory! React quickly!"
        text_question1 = "What is your first priority?"
        question1A = "A. Pick up the vial immediately"
        question1B = "B. Leave the room"
        question1C = "C. Identify the substance"
        question1D = "D. Clean it up with absorbent paper and distilled water"
        question1E = "E. Continue with your experiment"
        mission_2 = "Task 2!"
        text_bulle_mission2= "The alarm is still sounding in the laboratory. <br/><br/>You know that a vial containing a toxic powder has been spilled in the analytical chemistry laboratory. As you carefully and cautiously approach the bench, you notice a <strong>strong smell</strong> spreading throughout the room. The windows are closed, and the <strong>ventilation appears inadequate</strong>. A student is still standing a few metres away from the contaminated area. You need to assess the situation."
        text_question2 = "The student in the lab may have been exposed to the substance. At present, he/she doesn’t show any  visible symptoms. This indicates that:"
        question2A = "A. No exposure: He/she was not exposed because he/she was not handling the vial."
        question2B = "B. Exposure is impossible: He/she cannot have been exposed as he/she is wearing personal protective equipment (PPE)."
        question2C = "C. Exposure is possible, but the effects may appear later."
        question2D = "D. The substance is harmless because he/she does not feel unwell."
        question2E = "E. None of the above."
        mission_3 = "Task 3!"
        text_bulle_mission3 ="As you carefully approach the laboratory bench, you observe that the vial responsible for the incident is still lying on its side. The label has been partially damaged by the spill. The name of the substance has <strong>faded significantly and is now difficult,—or even impossible,—to read it with certainty</strong>.<br/><br/> Fortunately, several hazard pictograms on the vial are still visible."        
        text_question3 = "You need to carefully identify the hazard pictograms on the vial. What do they tell you about the hazards associated with this substance?"
        question3A =  "A. Acute toxicity, skin corrosion/irritation, respiratory sensitization"
        question3B = "B. Explosive, skin corrosion/irritation, acute toxicity"
        question3C = "C. Hazardous to the aquatic environment and human health, skin irritant, acute toxicity"
        question3D = "D. Flammable gas, skin irritant, CMR (Carcinogenic, Mutagenic, Reprotoxic)"
        question3E = "E. None of the above"
        mission_4 = "Task 4!"
        text_bulle_mission4= "The clues are falling into place (adding-up)! The chemical structure of the substance is still visible on the vial.<br/><br/> The laboratory provides you with a catalogue of chemical products listing each substance along with its name and nomenclature of IUPAC (International Union of Pure and Applied Chemistry and molecular structure). Use the catalogue to match the structure shown on the vial and identify the substance involved in the incident."
        text_question4 = "By comparing the chemical structure on the vial with the catalogue, what is the name of the spilled substance?"
        question4A = "A. Perfluorooctanoic acid (PFOA)"
        question4B = "B. Perfluorononanoic acid (PFNA) (PFNA)"
        question4C = "C. Perfluorobutanoic acid (PFBA)"
        question4D = "D. Perfluorodecanoic acid (PFDA)"
        question4E = "E. Perfluoroheptanoic acid (PFHpA)"
        question4F = "F. None of the above"
        mission_5 = "Task 5!"
        text_bulle_mission5 = "You have now identified the molecule. You consult the Safety Data Sheet (SDS) to determine the hazards associated with this substance. The SDS indicates the following hazard classifications: <br>→ H318: Causes serious eye damage. <br>→ H332: Harmful if inhaled.<br> → H351: Suspected of causing cancer.<br>→ H372 : Causes damage to organs through prolonged or repeated exposure.H315: Causes skin irritation."
        text_question5 = "Which items of personal protective equipment (PPE) should you wear before intervening in order to minimise the risk of exposure?"
        question5A = "A. Safety goggles"
        question5B ="B. Suitable nitrile gloves"
        question5C = "C. Household latex gloves"
        question5D = "D. protective mask"
        question5E = "E. Cartridge respirator"
        question5F = "F. Laboratory coat"
        question5G = "G. FFP3 respirator"
        text_bulle_mission6 = "Well done! The incident is now under control, but you still need to understand the <strong>long-term impacts</strong> of the identified substance. As the laboratory expert, your task is to identify the general properties of PFAS (per- and polyfluoroalkyl substances), also known as \"forever chemicals\".<br/><br/> Select the correct statements to demonstrate your understanding of these substances and why they represent a major challenge for chemical safety and environmental protection."        
        mission_6 =" Task 6!"
        text_question6 = "Which of the following are characteristics of PFAS?"
        question6A = "A. They may have toxic effects, with some being associated with long-term health risks."
        question6B ="B. They degrade rapidly when exposed to sunlight."
        question6C = "C. They have exceptional chemical stability, making them highly persistent in the environment."
        question6D = "D.  They can travel long distances in the environment and contaminate soil and water resources."
        question6E = "E. They are persistent pollutants capable of accumulating in living organisms (bioaccumulation)."
        mission_7 = "Task 7!"
        text_bulle_mission7 = "Congratulations! Mission accomplished! You successfully analysed the situation, made the right (???) decisions, and applied the appropriate safety measures. The laboratory director has been informed, and nobody is in danger. Thanks to your prompt response, the incident has been brought under control and recorded in the Occupational Health and Safety (OHS) register. However, this incident serves as an important reminder that constant vigilance is essential. Good organisation, strict compliance with safety procedures, and careful handling of chemicals are key to preventing laboratory accidents."
        text_question7 = "Which of the following good laboratory practices should be applied on a daily basis?"
        question7A = "A. Always ensure that chemical containers have clearly legible labels and replace any damaged labels immediately."
        question7B = "B. Store unused chemicals correctly in an appropriate storage cabinet."
        question7C = "C. Display clear warning signs throughout the laboratory indicating the presence of hazardous substances."
        question7D = "D. Install a surveillance camera in the laboratory.."
        question7E = "E. None of the above. "
        text_avant_code ="That's it. You're almost there. Now write down the letters and numbers you got to check your answers!"
        text_input_code = "Your code :"
        text_erreur_code = "oh no, you failed.."
        text_bravo_code = "BRAVO :sparkles:"
        text_bulle_reussite = "Bravo ! Great job ! <br/> <br/>\
                            Did you know? <br/> <br/>\
                            PFOA: A Chemical of Concern for Human Health and the Environment <br/> \
                            Perfluorooctanoic acid (PFOA) belongs to the PFAS family, commonly known as \"forever chemicals\" because of their exceptional resistance to degradation. These substances can persist in the environment for decades, contaminating soil, groundwater, surface water, and living organisms.<br/> \
                            In humans, repeated or long-term exposure to PFOA has been associated with several adverse health effects. Scientific studies have reported possible links with increased cholesterol levels, liver dysfunction, impaired immune response, developmental effects in fetuses, and reduced fertility. PFOA has also been classified as carcinogenic to humans (IARC Group 1) due to sufficient evidence linking exposure to cancers, particularly kidney and testicular cancer.<br/> \
                            Because of these risks, the use of PFOA is now strictly regulated worldwide. It is listed under the Stockholm Convention on Persistent Organic Pollutants, resulting in international bans or restrictions with only limited exemptions. Within the European Union, its manufacture and use are also tightly regulated under the REACH Regulation.<br/><br/> \
                            <strong>Key Takeaway</strong><br/> \
                            Even when no immediate symptoms are observed, repeated exposure to hazardous chemicals may have long-term health consequences. Understanding chemical hazards, following laboratory safety procedures, and minimizing exposure are essential for protecting both human health and the environment.<br/> \
                            Learn more: <br/> \
                            <a href='https://www.anses.fr/en/content/pfass-very-persistent-chemicals'> https://www.anses.fr/en/content/pfass-very-persistent-chemicals</a><br/> \
                            <a href ='https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas'> https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas</a>"
        text_bulle_echec = "oh no ! You failed ...<br/> <br/>Did you know?\
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
     
    with coltitre:
        st.title(title_site)
        st.subheader(subheader_title)
    _,col_centre_general,_ = st.columns([2,15,2])
    with col_centre_general:
        _,col_phrase_equipe,_ = st.columns([2,5,2])
        with col_phrase_equipe:
            st.markdown("*"+intro_equipe+"*")
        col_mascotte, col_bulle = st.columns([1, 3])
        init_state()
        if st.session_state.etape >= 0 and "end" not in st.session_state and st.session_state.etape <9 :
            with col_mascotte:
                st.image("img/mascotte_aquarelle.PNG")  # Remplace par ton imagewidth=250)
            with col_bulle:
                affiche(0,text_intro)
                _, btn_col, _ = st.columns([1, 4,1])
                with btn_col:
                    col_g, col_d = st.columns(2)
                    with col_g:
                        temps_choisi = st.radio(choix_temps, [5,10, 15], horizontal=True)
                    with col_d:
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
                st.badge(warning_time, color="red")
                st.image("img/mascotte_gameover.png")
                st.session_state.end = True
            else:
                st.markdown('<div id="ancre-mission1"></div>', unsafe_allow_html=True)
                col_gauche, col_droite,vide = st.columns([2.5,1,0.5])
                if st.session_state.etape >=1 and st.session_state.etape <9:
                    _,centresubheader,_ = st.columns(3)
                    with centresubheader:
                        st.subheader(mission_1)
                    col_bulle1, col_mascotte1,_ = st.columns([2.5,1,0.5])
                    with col_mascotte1:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle1:
                        affiche_droite(1,text_bulle_mission1)
                        st.write(text_question1)
                        col_qgauche, col_qdroite = st.columns(2)
                        selectionreflex = []
                        res_reflexes = [question1C]
                        with col_qgauche:
                            if st.checkbox(question1A):
                                selectionreflex.append(question1A)
                            if st.checkbox(question1B):
                                selectionreflex.append(question1B)
                            if st.checkbox(question1C):
                                selectionreflex.append(question1C)
                        with col_qdroite:
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
                    _, centreimage,_ = st.columns(3)
                    with centreimage:
                        if "buttonreflex" in st.session_state:
                            if set(selectionreflex) == set(res_reflexes):
                                st.badge(felicitationcode +" : 5", color = "blue")
                                st.image("img/mascotte_5.png",width=400)
                            else:
                                st.badge(felicitationcode+" : 0", color = "blue")
                                st.image("img/mascotte_0.png",width=400)
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
                    st.markdown('<div id="ancre-mission2"></div>', unsafe_allow_html=True)
                    _,centresubheader2,_ = st.columns(3)
                    with centresubheader2:
                        st.subheader(mission_2)
                    col_mascotte2, col_bulle2 = st.columns([1,3])
                    with col_mascotte2:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle2:
                        affiche(2, text_bulle_mission2)
                        st.write(text_question2)
                        col_qgauche, col_qdroite = st.columns(2)
                        selectionexpo = []
                        res_expo = [question2C]
                        with col_qgauche:
                            if st.checkbox(question2A):
                                selectionexpo.append(question2A)
                            if st.checkbox(question2B):
                                selectionexpo.append(question2B)
                            if st.checkbox(question2C):
                                selectionexpo.append(question2C)
                        with col_qdroite:
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
                    _, centreimage2,_ = st.columns(3)
                    with centreimage2:
                        if "buttonexpo" in st.session_state:
                            if set(selectionexpo) == set(res_expo):
                                st.badge(felicitationcode+" : Y", color = "blue")
                                st.image("img/mascotte_Y.png",width=400)
                            else:
                                st.badge(felicitationcode+" : T", color = "blue")
                                st.image("img/mascotte_T.png",width=400)
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
                                
                if st.session_state.etape >=3 and st.session_state.etape < 9:
                    st.markdown('<div id="ancre-mission3"></div>', unsafe_allow_html=True)
                    _,centresubheader3,_ = st.columns(3)
                    with centresubheader3:
                        st.subheader(mission_3)
                    col_bulle3, col_mascotte3,_ = st.columns([2.5,1,0.5])
                    with col_mascotte3:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle3:
                        affiche_droite(3,text_bulle_mission3)
                        _, col_img1, col_img2,col_img3, _=st.columns([1,1,1,1,1])
                        with col_img1:
                            st.image("img/unnamed.jpg")
                        with col_img2:
                            st.image("img/unnamed-2.png")
                        with col_img3:
                            st.image("img/unnamed.png")
                        st.write(text_question3)
                        col_qgauche, col_qdroite = st.columns(2)
                        selectioninfo = []
                        res_info = [question3A]
                        with col_qgauche:
                            if st.checkbox(question3A):
                                selectioninfo.append(question3A)
                            if st.checkbox(question3B):
                                selectioninfo.append(question3B)
                            if st.checkbox(question3C):
                                selectioninfo.append(question3C)
                        with col_qdroite:
                            if st.checkbox(question3D):
                                selectioninfo.append(question3D)
                            if st.checkbox(question3E):
                                selectioninfo.append(question3E)
                        _,centrebutton3,_ = st.columns(3)
                        with centrebutton3:
                            test_button3 = st.button(validermesreponses, key ="info")
                            if test_button3:
                                if "buttoninfo" not in st.session_state:
                                    st.session_state.buttoninfo=True
                    _, centreimage3,_ = st.columns(3)
                    with centreimage3:
                        if "buttoninfo" in st.session_state:
                            if set(selectioninfo) == set(res_info):
                                st.badge(felicitationcode +" : 5", color="blue")
                                st.image("img/mascotte_5.png",width=400)
                            else:
                                st.badge(felicitationcode +" : !", color = "blue")
                                st.image("img/mascotte_pointexc.png",width=400)
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
                    st.markdown('<div id="ancre-mission4"></div>', unsafe_allow_html=True)
                    _,centresubheader4,_ = st.columns(3)
                    with centresubheader4:
                        st.subheader(mission_4)
                    col_mascotte4,col_bulle4 = st.columns([1,3])
                    with col_mascotte4:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle4:
                        affiche(4, text_bulle_mission4)
                        st.write(text_question4)
                        colimg1,colimg4,colimg3 = st.columns(3)
                        with colimg4:
                            st.image("img/unnamed-42.png")
                        col_qgauche, col_qdroite = st.columns(2)
                        selectionstrag = []
                        res_strag = [question4A]
                    with col_qgauche:
                        if st.checkbox(question4A):
                            selectionstrag.append(question4A)
                        if st.checkbox(question4B):
                            selectionstrag.append(question4B)
                        if st.checkbox(question4C):
                            selectionstrag.append(question4C)
                    with col_qdroite:
                        if st.checkbox(question4D):
                            selectionstrag.append(question4D)
                        if st.checkbox(question4E):
                            selectionstrag.append(question4E)
                        if st.checkbox(question4F):
                            selectionstrag.append(question4F)
                    with col_bulle4:        
                        _,centrebutton,_ = st.columns(3)
                        with centrebutton:
                            test_button4 = st.button(validermesreponses, key ="rrag")
                            if test_button4:
                                if "buttonstrag" not in st.session_state:
                                    st.session_state.buttonstrag=True
                    _, centreimage4,_ = st.columns(3)
                    with centreimage4:
                        if "buttonstrag" in st.session_state:
                            if set(selectionstrag) == set(res_strag):
                                st.badge(felicitationcode+" : T", color = "blue")
                                st.image("img/mascotte_T.png",width=400)
                            else:
                                st.badge(felicitationcode +" : Y", color = "blue")
                                st.image("img/mascotte_Y.png",width=400)
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
                                
                if st.session_state.etape >= 5 and st.session_state.etape <9:
                    _,centresubheader5,_ = st.columns(3)
                    with centresubheader5:
                        st.subheader(mission_5)
                    st.markdown('<div id="ancre-mission5"></div>', unsafe_allow_html=True)
                    col_bulle5, col_mascotte5,col_img4_ = st.columns([2.5,1,0.5])
                    with col_mascotte5:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle5:
                        affiche_droite(5, text_bulle_mission5)
                        st.write(text_question5)
                        col_qgauche5, col_qdroite5 = st.columns(2)
                        selection_epi = []
                        res_epi = [question5G, question5F, question5A, question5B]
                        col_qgauche6, col_qdroite6 = st.columns(2)
                        with col_qgauche6:
                            if st.checkbox(question5A):
                                selection_epi.append(question5A)
                            if st.checkbox(question5B):
                                selection_epi.append(question5B)
                            if st.checkbox(question5C):
                                selection_epi.append(question5C)
                            if st.checkbox(question5D):
                                selection_epi.append(question5D)
                        with col_qdroite6:
                            if st.checkbox(question5E):
                                selection_epi.append(question5E)
                            if st.checkbox(question5F):
                                selection_epi.append(question5F)
                            if st.checkbox(question5G):
                                selection_epi.append(question5G)
                        _,centrebutton5,_ = st.columns(3)
                        with centrebutton5:
                            test_button5 = st.button(validermesreponses, key ="epi")
                            if test_button5:
                                if "buttonepi" not in st.session_state:
                                    st.session_state.buttonepi=True
                    _, centreimage5,_ = st.columns(3)
                    with centreimage5:
                        if "buttonepi" in st.session_state:
                            if set(selection_epi) == set(res_epi):
                                st.badge(felicitationcode +" : 0", color = "blue")
                                st.image("img/mascotte_0.png",width=400)
                            else:
                                st.badge(felicitationcode +" : 5", color = "blue")
                                st.image("img/mascotte_5.png",width=400)
                            if "etape6" not in st.session_state:
                                st.session_state.etape6 = True
                                etape_suivante()
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

                if st.session_state.etape >= 6 and st.session_state.etape <9:
                    _,centresubheader6,_ = st.columns(3)
                    with centresubheader6:
                        st.subheader(mission_6)
                    st.markdown('<div id="ancre-mission6"></div>', unsafe_allow_html=True)
                    col_mascotte6, col_bulle6 = st.columns([1,3])
                    with col_mascotte6:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle6:
                        affiche(6, text_bulle_mission6)
                        selection_epi = []
                        st.write(text_question6)
                        col_qgauche5, col_qdroite5 = st.columns(2)
                        selection_pfas = []
                        res_pfas = [question6A, question6C, question6D, question6E]
                        col_qgauche6, col_qdroite6 = st.columns(2)
                        with col_qgauche6:
                            if st.checkbox(question6A):
                                selection_pfas.append(question6A)
                            if st.checkbox(question6B):
                                selection_pfas.append(question6B)
                            if st.checkbox(question6C):
                                selection_pfas.append(question6C)
                        with col_qdroite6:
                            if st.checkbox(question6D):
                                selection_pfas.append(question6D)
                            if st.checkbox(question6E):
                                selection_pfas.append(question6E)
                        _,centrebutton6,_ = st.columns(3)
                        with centrebutton6:
                            test_button6 = st.button(validermesreponses, key ="pfas")
                            if test_button6:
                                if "buttonpfas" not in st.session_state:
                                    st.session_state.buttonpfas=True
                    _, centreimage6,_ = st.columns(3)
                    with centreimage6:
                        if "buttonpfas" in st.session_state:
                            if set(selection_pfas) == set(res_pfas):
                                st.badge(felicitationcode +" : X", color = "blue")
                                st.image("img/mascotte_X.png",width=400)
                            else:
                                st.badge(felicitationcode +" : T", color = "blue")
                                st.image("img/mascotte_T.png",width=400)
                            if "etape7" not in st.session_state:
                                st.session_state.etape7 = True
                                etape_suivante()
                                st.session_state.scroll_flag_mission6 = True
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
                if st.session_state.etape >= 7 and st.session_state.etape < 8:
                    _,centresubheader7,_ = st.columns(3)
                    with centresubheader7:
                        st.subheader(mission_7)
                    st.markdown('<div id="ancre-mission7"></div>', unsafe_allow_html=True)
                    col_bulle7, col_mascotte7,col_img4_ = st.columns([2.5,1,0.5])
                    with col_mascotte7:
                        st.image("img/mascotte_aquarelle.PNG")
                    with col_bulle7:
                        affiche_droite(7,text_bulle_mission7)
                        selection_prevention = []
                        res_prevention = [question7B, question7A, question7C]
                        st.write(text_question7)
                        col_qgauche7, col_qdroite7 = st.columns(2)
                        with col_qgauche7:
                            if st.checkbox(question7A):
                                selection_prevention.append(question7A)
                            if st.checkbox(question7B):
                                selection_prevention.append(question7B)
                            if st.checkbox(question7C):
                                selection_prevention.append(question7C)
                        with col_qdroite7:
                            if st.checkbox(question7D):
                                selection_prevention.append(question7D)
                            if st.checkbox(question7E):
                                selection_prevention.append(question7E)
                        _,centrebutton7,_ = st.columns(3)
                        with centrebutton7:
                            test_button7 = st.button(validermesreponses, key ="prevention")
                            if test_button7:
                                if "buttonprevention" not in st.session_state:
                                    st.session_state.buttonprevention=True
                    _, centreimage7,_ = st.columns(3)
                    with centreimage7:
                        if "buttonprevention" in st.session_state:
                            if set(selection_prevention) == set(res_prevention):
                                st.badge(felicitationcode +" : !", color = "blue")
                                st.image("img/mascotte_pointexc.png",width=400)
                            else:
                                st.badge(felicitationcode +" : Y", color = "blue")
                                st.image("img/mascotte_Y.png",width=400)
                            if "etape8" not in st.session_state:
                                st.session_state.etape8 = True
                                etape_suivante()
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
                    st.markdown('<div id="ancre-mission8"></div>', unsafe_allow_html=True)
                    st.write(text_avant_code)
                    reponse_utilisateur = st.text_input(text_input_code)
                    if reponse_utilisateur =="":
                        st.write("")
                    elif reponse_utilisateur == "5Y5T0X!":
                        st.session_state.reussite = True
                        st.switch_page("resultat.py")
                    else:
                        st.session_state.reussite = False
                        st.switch_page("resultat.py")
                    #     etape_suivante() 
                    #     st.badge(text_bravo_code, color = "green")
                    #     col_bullereussite, col_mascottereussite,col_img4_ = st.columns([2.5,1,0.5])
                    #     with col_mascottereussite:
                    #         st.image("img/mascotte_reussite.png")
                    #     with col_bullereussite:
                    #         affiche_droite(8,text_bulle_reussite)
                    #     temps_choisi = 10000000000000
                    #     col_mascotteecheccorrection, col_bulleecheccorrection = st.columns([1,3])
                    #     with col_mascotteecheccorrection:
                    #         st.image("img/mascotte_prof.png")
                    #     with col_bulleecheccorrection:
                    #         affiche(10,text_correction)
                    #     if not st.session_state.get("deja_fait", False):
                    #         st.session_state.deja_fait = True
                    #         st.rerun()            
                    # else:
                    #     etape_suivante()
                    #     if not st.session_state.get("deja_fait", False):
                    #         st.session_state.deja_fait = True
                    #         st.rerun()
                    #         time.sleep(3)
                    #     st.badge(text_erreur_code, color = "red")
                    #     col_bulleechec, col_mascotteechec,col_img4_ = st.columns([2.5,1,0.5])
                    #     with col_mascotteechec:
                    #         st.image("img/mascotte_gameover.png")
                    #     with col_bulleechec:
                    #         affiche_droite(9,text_bulle_echec)
                    #     col_mascotteecheccorrection, col_bulleecheccorrection = st.columns([1,3])
                    #     with col_mascotteecheccorrection:
                    #         st.image("img/mascotte_prof.png")
                    #     with col_bulleecheccorrection:
                    #         affiche(10,text_correction)
                    #     temps_choisi = 10000000000000
                    #     if not st.session_state.get("deja_fait", False):
                    #         st.session_state.deja_fait = True
                    #         st.rerun()

#escape()