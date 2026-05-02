import streamlit as st
import google.generativeai as genai

# API kalitni to'g'ridan-to'g'ri chaqirish
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🤖 AN1 AI va Tibbiyot")

# Modelni to'g'ridan-to'g'ri chaqirish (transport='rest' v1beta xatosini o'ldiradi)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

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
            # Modelni to'g'ridan-to'g'ri chaqirish
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik: {e}")
