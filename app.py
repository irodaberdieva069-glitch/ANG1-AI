import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Sahifa sozlamalari
st.set_page_config(page_title="AN1 AI", layout="wide")

# API Kalitini o'rnatish
# GitHub Secrets'dan kalitni olish
api_key = st.secrets.get("GEMINI_API_KEY") 
genai.configure(api_key=api_key)

def main():
    # Banner rasmi
    image_url = "https://github.com/irodaberdieva069-glitch/ANG1-AI/blob/main/IMG_1541.png?raw=true"
    st.image(image_url, use_container_width=True)

    # Sarlavha
    st.title("AN1 AI - Innovatsion Tibbiy Texnik Tizim")
    st.markdown("---")
    
    # Asosiy sahifa tarkibi
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bo'limlar")
        st.write("✅ Farmatsiya")
        st.write("✅ Hamshiralik ishi")
        st.write("✅ Klinik fanlar")
        st.write("✅ Laboratoriya diagnostikasi")
        
    with col2:
        st.subheader("Tizim holati")
        st.success("Tizim faol ✅")
        st.info("Boshqaruvchi: Nematov Abdulaziz")

    # Chatbot qismi
    st.markdown("---")
    st.subheader("🤖 AN1 AI Chatbot (Gemini 2.0 Pro)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat tarixini chiqarish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Foydalanuvchi xabari
    if prompt := st.chat_input("Tibbiy texnikum bo'yicha savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI javobi (Gemini 2.0 Pro modeli)
        with st.chat_message("assistant"):
            try:
                # Model nomi 2.0 Pro ga yangilandi
                model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("API kalitni yoki model nomini tekshiring.")

if __name__ == "__main__":
    main()
