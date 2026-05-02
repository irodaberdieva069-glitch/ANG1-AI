import streamlit as st
import google.generativeai as genai

# API kalitni sozlash
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"API kalit xatosi: {e}")
    st.stop()

st.title("🤖 AN1 AI va Tibbiyot") 

# MODELNI O'ZGARTIRDIK: 
# 'gemini-1.5-flash' - bu eng ishonchli nom.
model = genai.GenerativeModel('gemini-1.5-flash')

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
            # generate_content
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik: {e}. Iltimos, API kalitingiz Google AI Studio-da to'g'ri yaratilganiga ishonch hosil qiling.")
