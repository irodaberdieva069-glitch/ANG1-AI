import streamlit as st
import google.generativeai as genai

# Sahifa nomi
st.set_page_config(page_title="AN1 AI Pro", page_icon="🤖")
st.title("🤖 AN1 AI Pro")

# API Kalitni tekshirish
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Xatolik: GEMINI_API_KEY topilmadi. Settings -> Secrets ga qo'shing!")
    st.stop()

# Model: gemini-1.5-pro (Eng kuchlisi)
model = genai.GenerativeModel('gemini-1.5-pro')

if prompt := st.chat_input("Savolingni yoz..."):
    st.chat_message("user").markdown(prompt)
    with st.chat_message("assistant"):
        try:
            # Pro model javobi
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Pro model xatosi: {e}")
