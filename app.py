import streamlit as st
import google.generativeai as genai
import os

# Sahifa sarlavhasi
st.set_page_config(page_title="ANG1 AI", page_icon="🤖")
st.title("🤖 ANG1 AI - Raqamli hamkor")

# API kalitini xavfsiz qabul qilish
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = st.sidebar.text_input("API Kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Chat tarixini saqlash
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tarixni ko'rsatish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Foydalanuvchi so'rovi
    if prompt := st.chat_input("Salom, aka! Nima yordam bera olaman?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AIdan javob olish
        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Xatolik yuz berdi: {e}")
else:
    st.warning("Iltimos, chap menyuda API kalitingizni kiriting.")
