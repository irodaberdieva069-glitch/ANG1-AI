import streamlit as st
import google.generativeai as genai

# API kalitni to'g'ridan-to'g'ri o'zgaruvchiga olamiz
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Secrets-da GEMINI_API_KEY topilmadi!")
    st.stop()

genai.configure(api_key=api_key)

# Modelni chaqirish
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AN1 AI Pro")

if prompt := st.chat_input("Savolingni yoz..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Xatolik: {e}")
