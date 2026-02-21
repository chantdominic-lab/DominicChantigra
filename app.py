import streamlit as st

# 1. Postavke
st.set_page_config(page_title="Snovi i Vizije", page_icon="☁️")
st.markdown("<style>.stApp { background-color: #000; color: #00FF41; }</style>", unsafe_allow_html=True)

# 2. Naslovi
st.title("☁️ Snovi i Vizije")
st.subheader("by Dominic Chant")

# 3. Vizije (Kratki popis za test)
vizije = {
    "1": "U snu sam vidio strašno vrijeme i tužni pogled ljudi kroz žicu...",
    "19": "Vidio sam osobu koja je hram... svjetlost koja se otvori."
}

# 4. Unos
broj = st.text_input("Unesi broj vizije (1-19):")
if broj in vizije:
    st.success(f"VIZIJA {broj}: {vizije[broj]}")
else:
    st.info("Unesite 1 ili 19 za test.")

st.write("---")
st.write("Ako vidite ovaj tekst, vasa aplikacija je ZIVA!")
