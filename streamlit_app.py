import streamlit as st

# 1. POSTAVKE I MATRIX STIL
st.set_page_config(page_title="Snovi i Vizije", page_icon="☁️")

st.markdown("""
<style>
    /* Glavna pozadina aplikacije */
    .stApp { 
        background-color: #000000; 
        color: #00FF41; 
        font-family: 'Courier New', monospace;
    }
    
    /* BIJELA SLOVA ZA UNOS (Input fields) */
    input {
        color: #FFFFFF !important; 
        background-color: #111111 !important;
        border: 1px solid #00FF41 !important;
        caret-color: #00FF41; /* Zeleni kursor koji treperi */
    }

    /* Boja teksta iznad polja za unos */
    .stTextInput label {
        color: #00FF41 !important;
    }
</style>
""", unsafe_allow_html=True)

# Ostatak koda ide ovdje...


st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

# 2. SVE VIZIJE (1-19)
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

# 3. LOGIKA IGRE
if 'otkljucano' not in st.session_state:
    st.session_state.otkljucano = set()

preostalo = 19 - len(st.session_state.otkljucano)

if preostalo > 0:
    st.info(f"🔓 Otključano vizija: {len(st.session_state.otkljucano)}/19")
    broj = st.text_input("Unesi broj vizije (1-19):")
    
    if broj in vizije:
        st.markdown(f"### VIZIJA {broj}")
        st.info(vizije[broj])
        if st.button("Zabilježi viziju"):
            st.session_state.otkljucano.add(broj)
            st.rerun()
    elif broj != "":
        st.error("Unesi važeći broj između 1 i 19.")
else:
    st.success("✅ SVIH 19 VIZIJA JE PRIKUPLJENO.")
    ime = st.text_input("Tko je vođa anđela?")
    pravilo = st.text_input("Zlatno pravilo?")
    
    if st.button("POTVRDI"):
        # Provjera točnih odgovora
        if "mihael" in ime.lower() and "ne čini drugima" in pravilo.lower():
            st.balloons()
            st.title("🏆 USPJELI STE!")
            st.markdown("Hvala vam na putovanju kroz vizije.")
            # Ovdje možeš dodati pravi link na knjigu
            st.markdown("[Preuzmi knjigu DOI](https://doi.org)")
        else:
            st.error("Odgovori nisu točni. Pokušaj ponovno.")
