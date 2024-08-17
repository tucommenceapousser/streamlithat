import streamlit as st
import openai
import os
from dotenv import load_dotenv
import html
import time

# Charger les variables d'environnement
load_dotenv()

# Récupérer les clés API depuis les variables d'environnement
API_KEYS = [
    os.getenv("OPENAI_API_KEY"),
    os.getenv("OPENAI_API_KEY1"),
    os.getenv("OPENAI_API_KEY2"),
    os.getenv("OPENAI_API_KEY3")
]

# Fonction pour obtenir la clé API disponible
def get_available_api_key():
    for key in API_KEYS:
        if key:
            return key
    raise ValueError("Aucune clé API OpenAI valide trouvée.")

# Configurer OpenAI avec la clé API disponible
def configure_openai():
    openai.api_key = get_available_api_key()

# Contexte sur Anonymous, l'anarchisme, et la lutte mondiale
CONTEXT = """
Anonymous est une idée globale, une voix pour les sans-voix, luttant contre l'oppression sous toutes ses formes. L'anarchisme, comme philosophie politique, rejette toutes formes de hiérarchie et prône l'autonomie. Récemment, des anarchistes du monde entier, notamment en France, en Allemagne, et en Italie, se sont joints aux Ukrainiens et aux forces au Rojava pour défendre l'autonomie et la justice sociale.
"""

# Fonction pour appeler l'API OpenAI avec le modèle de chat
def query_openai(prompt):
    configure_openai()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": CONTEXT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erreur lors de l'appel à l'API OpenAI: {e}"

# Fonction pour échapper les entrées HTML
def escape_html(text):
    return html.escape(text)

# Titre principal
st.markdown('<div class="title">J\'ai mal à mon chapeau</div>', unsafe_allow_html=True)

# Modifier le titre de la page et favicon
st.markdown("""
    <script>
        document.title = "J'ai mal à mon chapeau";
        var link = document.createElement('link');
        link.rel = 'icon';
        link.href = 'https://d.top4top.io/p_314462a0r0.png';  // Use your favicon URL
        document.head.appendChild(link);
    </script>
""", unsafe_allow_html=True)

# Image principale
st.image("https://d.top4top.io/p_314462a0r0.png", caption="Anonymous")

# Définir le CSS personnalisé pour le style
st.markdown("""
    <style>
        .title {
            margin-bottom: 30px;
            color: #00ff00; /* Couleur du texte */
            font-family: 'Roboto', sans-serif;
            font-size: 36px; /* Taille de la police */
            font-weight: bold; /* Gras */
            text-align: center; /* Alignement du texte */
            background-color: #000000; /* Couleur de fond */
            padding: 20px; /* Espacement autour du texte */
            border-radius: 10px; /* Bords arrondis */
        }
        .caption {
            font-size: 18px; /* Taille de la police de la légende */
            color: #ffffff; /* Couleur de la légende */
            text-align: center; /* Alignement de la légende */
        }

        .section-header {
            color: #ff00ff; /* Neon pink */
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
        .content {
            color: #00ffff; /* Cyan */
            font-size: 18px;
            background-color: #222222; /* Dark gray background */
            padding: 15px;
            border-radius: 8px;
        }
        .button {
            background-color: #ff00ff; /* Neon pink */
            color: #ffffff; /* White text */
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #ff99ff; /* Light pink on hover */
        }
        footer[class*="st-emotion-cache"] {
            display: none;
        }
        .custom-footer {
            background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
            color: #fff;
            text-align: center;
            padding: 30px 20px;
            position: relative;
            box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.7);
            margin-top: 50px;
        }

        .custom-footer .footer-content h2 {
            font-family: 'Courier New', Courier, monospace;
            font-size: 2.5rem;
            color: #00ff99;
            text-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99;
            margin: 0 0 10px;
            animation: neon 1.5s ease-in-out infinite alternate;
        }

        .custom-footer .footer-content p {
            font-size: 1rem;
            color: #ccc;
            margin: 0 0 20px;
            font-style: italic;
        }

        .custom-footer .social-icons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .custom-footer .social-icon {
            display: inline-block;
            width: 40px;
            height: 40px;
            line-height: 40px;
            background-color: #00ff99;
            color: #1a1a1a;
            font-size: 1.5rem;
            border-radius: 50%;
            transition: all 0.3s ease;
            text-align: center;
            text-decoration: none;
            box-shadow: 0 0 10px #00ff99;
        }

        .custom-footer .social-icon:hover {
            background-color: #fff;
            color: #00ff99;
            box-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99;
        }

        @keyframes neon {
            from {
                text-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99;
            }
            to {
                text-shadow: 0 0 20px #00ff99, 0 0 30px #00ff99;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Introduction
st.markdown('<div class="section-header">Introduction</div>', unsafe_allow_html=True)
st.markdown('<div class="content">"J\'ai mal à mon chapeau" est une métaphore pour la douleur collective des luttes. Anonymous, symbole de résistance mondiale, incarne cette douleur partagée en se dressant contre les oppressions, tout en étant un vecteur d\'espoir pour ceux qui se battent pour la liberté.</div>', unsafe_allow_html=True)

# Section de requête utilisateur

# Soutien aux Causes
st.markdown('<div class="section-header">Soutien aux Causes</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Anonymous et les anarchistes se sont engagés aux côtés de nombreuses causes, de la Palestine à l\'Ukraine, en passant par le Rojava. Leur soutien prend la forme d\'actions directes, de sensibilisation numérique, et de résistance contre les régimes oppressifs.</div>', unsafe_allow_html=True)
st.markdown('<div class="content"><ul><li><a href="https://anonops.com/" style="color:#00ffff;">Anonymous Operations</a></li><li><a href="https://supportukrainenow.org/" style="color:#00ffff;">Support Ukraine Now</a></li><li><a href="https://rojavainformationcenter.com/" style="color:#00ffff;">Rojava Information Center</a></li></ul></div>', unsafe_allow_html=True)


# Combattants internationaux au Rojava avec les YPG
st.markdown('<div class="section-header">Combattants Internationaux au Rojava</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Depuis le début de la guerre en Syrie, de nombreux combattants internationaux ont rejoint les rangs des Unités de Protection du Peuple (YPG) au Rojava. Ces combattants, venus du monde entier, partagent une vision commune de la lutte contre le fascisme et pour l\'autonomie des peuples. Le Rojava, avec son modèle de confédéralisme démocratique, attire des anarchistes, socialistes et militants des droits humains, tous désireux de défendre l\'égalité, la justice sociale et l\'émancipation des peuples opprimés.</div>', unsafe_allow_html=True)

# Combattants internationaux en Ukraine
st.markdown('<div class="section-header">Combattants Internationaux en Ukraine</div>', unsafe_allow_html=True)
st.markdown('<div class="content">En Ukraine, depuis l\'invasion russe de 2022, des combattants internationaux, principalement de France, d\'Allemagne, et d\'Italie, ont rejoint les forces ukrainiennes pour défendre la liberté et l\'autodétermination. Beaucoup de ces combattants se considèrent anarchistes, partageant une opposition aux régimes autoritaires et un désir de justice sociale. Leur présence aux côtés des Ukrainiens symbolise la solidarité internationale face à l\'impérialisme et la lutte continue pour l\'autonomie des peuples à travers le monde.</div>', unsafe_allow_html=True)
# Combattants et humanitaires à Gaza (Palestine)
st.markdown('<div class="section-header">Solidarité avec Gaza (Palestine)</div>', unsafe_allow_html=True)
st.markdown('<div class="content">À Gaza, la résistance palestinienne face à l\'oppression israélienne continue d\'attirer des combattants et humanitaires internationaux. Avec le soutien militaire des États-Unis, Israël intensifie ses attaques, semant la mort et la destruction parmi la population palestinienne. Face à cette escalade, des activistes, humanitaires, et volontaires du monde entier se mobilisent pour soutenir la cause palestinienne, dénoncer l\'apartheid israélien, et offrir de l\'aide aux civils en détresse. La solidarité internationale est plus que jamais nécessaire pour faire face à cette situation humanitaire catastrophique.</div>', unsafe_allow_html=True)
st.markdown('<div class="content"><ul><li><a href="https://anonops.com/contact/" style="color:#00ffff;">Contactez Anonymous Operations</a></li><li><a href="https://supportukrainenow.org/contact/" style="color:#00ffff;">Contactez Support Ukraine Now</a></li><li><a href="https://rojavainformationcenter.com/contact/" style="color:#00ffff;">Contactez le Centre d\'Information du Rojava</a></li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">Interrogez l\'IA</div>', unsafe_allow_html=True)
user_query = st.text_input('Posez une question sur Anonymous, l\'anarchisme, ou la solidarité internationale:', '')

if st.button('Obtenir Réponse'):
    if user_query:
        # Échapper les entrées pour éviter XSS
        safe_query = escape_html(user_query)
        result = query_openai(f"Répondez à cette question sur Anonymous et l'anarchisme : {safe_query}")
        if result:
            st.markdown(f'<div class="content">{result}</div>', unsafe_allow_html=True)
        else:
            st.error("Erreur lors de la récupération de la réponse.")
    else:
        st.error("Veuillez entrer une question.")

# Paragraphe avec bouton flashy menant à la page de présentation

st.markdown('<div class="section-header">Découvrir le Profil de TRHACKNON</div>', unsafe_allow_html=True)

if st.button('Découvrir mon Profil'):
    # Afficher un message flamboyant
    st.markdown("""
        <div style='
            font-size: 22px; 
            font-weight: bold; 
            color: #ff6600; 
            text-align: center; 
            text-shadow: 2px 2px 8px rgba(255, 102, 0, 0.8); 
            animation: pulsate 1.5s infinite;
            margin-top: 50px;'>
            Explorez ma page de présentation pour en savoir plus sur moi, mes projets, et mes actions.
        </div>
        <style>
        @keyframes pulsate {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        </style>
    """, unsafe_allow_html=True)

    # Attendre 3 secondes avant d'afficher le lien de redirection
    time.sleep(3)

    # Afficher le bouton de redirection avec style dynamique
    st.markdown("""
        <style>
            .glow-button {
                display: inline-block;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                color: #fff;
                background: linear-gradient(45deg, #ff00ff, #00ffff, #ff9900);
                background-size: 400% 400%;
                border: 4px solid transparent;
                border-radius: 12px;
                text-decoration: none;
                text-align: center;
                animation: gradientAnimation 5s ease infinite, glowAnimation 1.5s ease-in-out infinite alternate;
                transition: all 0.3s ease-in-out;
                box-shadow: 0 0 20px #ff00ff, 0 0 30px #00ffff, 0 0 40px #ff9900;
            }
            .glow-button:hover {
                border-image: linear-gradient(45deg, #ff00ff, #00ffff, #ff9900) 1;
                box-shadow: 0 0 30px #ff00ff, 0 0 40px #00ffff, 0 0 50px #ff9900;
            }
            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            @keyframes glowAnimation {
                from {
                    box-shadow: 0 0 20px #ff00ff, 0 0 30px #00ffff, 0 0 40px #ff9900;
                }
                to {
                    box-shadow: 0 0 30px #ff00ff, 0 0 40px #00ffff, 0 0 50px #ff9900;
                }
            }
        </style>

        <div style='text-align: center; margin-top: 20px;'>
            <a href="https://trhacknon-profile.onrender.com/" class="glow-button" target="_blank">Cliquez ici pour voir mon profil</a>
        </div>
    """, unsafe_allow_html=True)

# Informations de contact
st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Pour en savoir plus ou pour nous contacter, veuillez consulter les liens ci-dessous :</div>', unsafe_allow_html=True)

# Pied de page personnalisé
st.markdown("""
    <footer class="custom-footer">
        <div class="footer-content">
            <h2>Nous Sommes Anonymous</h2>
            <p>"Nous sommes légion. Nous ne pardonnons pas. Nous n'oublions pas. Redoutez-nous."</p>
        </div>
        <div class="social-icons">
            <a href="https://twitter.com/YourAnonymousNews" class="social-icon" target="_blank" title="Twitter">&#x1F426;</a>
            <a href="https://github.com/tucommenceapousser" class="social-icon" target="_blank" title="GitHub">&#x1F4BB;</a>
            <a href="https://trhacknon-profile.onrender.com/" class="social-icon" target="_blank" title="Site Web">&#x1F4F1;</a>
        </div>
    </footer>
""", unsafe_allow_html=True)
