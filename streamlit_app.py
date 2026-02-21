import streamlit as st

# 1. POSTAVKE I MATRIX STIL (CIJELI CSS BLOK)
st.set_page_config(page_title="Snovi i Vizije", page_icon="☁️")

st.markdown("""
<style>
    /* Glavna pozadina aplikacije */
    .stApp { 
        background-color: #000000; 
        color: #00FF41; 
        font-family: 'Courier New', monospace;
    }
    
    /* BIJELA SLOVA DOK TIPKAŠ I VIDLJIV OKVIR */
    input {
        color: #FFFFFF !important; 
        background-color: #111111 !important;
        border: 2px solid #00FF41 !important;
        caret-color: #00FF41 !important;
        font-size: 1.2rem !important;
        padding: 10px !important;
    }

    /* Boja teksta iznad polja (label) */
    .stTextInput label {
        color: #00FF41 !important;
        font-weight: bold !important;
    }

    /* Gumb stil (Zelena pozadina, crna slova) */
    .stButton>button {
        background-color: #00FF41;
        color: #000000;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    
    /* Info poruke (vizije) neka budu u zelenom okviru */
    .stAlert {
        background-color: #000000;
        color: #00FF41;
        border: 1px solid #00FF41;
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
            st.markdown("[Preuzmi knjigu DOI](https://doi.org)")
        else:
            st.error("Odgovori nisu točni. Pokušaj ponovno.")
