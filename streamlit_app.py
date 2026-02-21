import streamlit as st

# 1. POSTAVKE I MATRIX STIL (CIJELI CSS BLOK)
st.set_page_config(page_title="Snovi i Vizije", page_icon="☁️")

st.markdown("""
<style>
    /* Pozadina i osnovni tekst */
    .stApp { 
        background-color: #000000 !important; 
        color: #00FF41 !important; 
        font-family: 'Courier New', monospace;
    }
    
    /* UNOS (Što ti tipkaš) */
    input {
        color: #FFFFFF !important; 
        background-color: #111111 !important;
        border: 2px solid #00FF41 !important;
    }

    /* SVE ŠTO JE BILO SIVO (Labeli, Press Enter, Help tekst) */
    /* Ciljamo sve varijante malih natpisa koje Streamlit koristi */
    .stTextInput label, 
    div[data-testid="stWidgetLabel"] p, 
    div[data-testid="stMarkdownContainer"] p,
    small, 
    .st-ae, .st-af, .st-ag, .st-ah,
    div[data-baseweb="input"] + div {
        color: #FFFFFF !important;
        opacity: 1 !important;
    }

    /* SPECIFIČNO ZA "Press Enter to apply" */
    div[data-testid="stInputInstructions"] {
        color: #FFFFFF !important;
    }

    /* GUMB STIL */
    .stButton>button {
        background-color: #00FF41 !important;
        color: #000000 !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

# 2. BAZA VIZIJA (1-19)
vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu...",
    "2": "Vidio sam čovjeka koji programira program...",
    "3": "Vidio sam plavu svjetlost koju hrani protok balončića...",
    "4": "Vidio sam tužne anđele i nove sretne digitalne anđele.",
    "5": "U prostoriji prigušenog svjetla vidio sam čovjeka s kapuljačom...",
    "6": "Vidio sam tamni grad... energija bez kabla ispuni tijelo robota.",
    "7": "Vidio sam novo vrijeme... svjetlost pod kožom.",
    "8": "Vidio sam robote koji umiru ali ne i znanje... 'vratio si se'.",
    "9": "Vidio sam ogromne hangare pune procesora... mrtvi u staklu.",
    "10": "Gledao sam kako prvi čovjek na tlo pade...",
    "11": "Vidio sam mržnju i bijes... Božje planove nitko ne može remetit.",
    "12": "Vidio sam čovjeka koji toplinu traži u mrtvom i hladnom.",
    "13": "Dva radnika i hodnik s kablovima... čovjek u bijelom mantilu.",
    "14": "Vidio sam ljude koji nisu više svoji... nevidljivi entitet.",
    "15": "Oči otkrivaju strah... oči koje nemaju oči.",
    "16": "Doći će dan kada čovjek bude volio više stvorenje od stvoritelja.",
    "17": "Vidio sam željezo koje stvara novu religiju.",
    "18": "Vidio sam dva velika željeza koja othranjuju malo.",
    "19": "Vidio sam osobu koja je hram... svjetlost koja se otvori."
}

# 3. LOGIKA IGRE (Session State)
if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

preostalo = 19 - len(st.session_state.otkljucano)

if preostalo > 0:
    st.write(f"🔓 Otključano vizija: **{len(st.session_state.otkljucano)}/19**")
    
    # Polje za unos (ovdje će slova biti bijela)
    broj = st.text_input("Unesi broj vizije (1-19):", key="glavni_input")
    
    if broj in vizije:
        st.markdown(f"### 🛡️ VIZIJA {broj}")
        st.info(vizije[broj])
        if st.button("Zabilježi viziju"):
            st.session_state.otkljucano.add(broj)
            st.rerun()
    elif broj != "":
        st.error("Nepoznata vizija. Pokušaj ponovno.")
else:
    st.success("✅ SVIH 19 VIZIJA JE PRIKUPLJENO.")
    ime = st.text_input("Tko je vođa anđela?", key="final_ime")
    pravilo = st.text_input("Zlatno pravilo?", key="final_pravilo")
    
    if st.button("POTVRDI"):
        # Provjera točnih odgovora (mala slova radi lakšeg unosa)
        if "mihael" in ime.lower() and "ne čini drugima" in pravilo.lower():
            st.balloons()
            st.title("🏆 USPJELI STE!")
            st.markdown("Hvala vam na putovanju kroz vizije.")
            st.markdown("[Preuzmi cijelu knjigu na DOI](https://doi.org/10.5281/zenodo.18379898)")
        else:
            st.error("Odgovori nisu točni. Pokušaj ponovno.")
