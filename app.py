import streamlit as st
import google.generativeai as genai

# API kalit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API kalit topilmadi!")
    st.stop()

st.title("🤖 AN1 AI Pro") 

# MODELNI O'ZGARTIRDIK: 
# gemini-1.5-flash-latest deb yozamiz, bu eng yangi versiya
model = genai.GenerativeModel('gemini-1.5-flash-latest')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Savolingni yoz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # generate_content qismi
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # Agar yana xato bersa, xatoni to'liq ko'rsat
            st.error(f"Xatolik: {e}")
