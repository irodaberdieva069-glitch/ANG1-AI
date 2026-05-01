import streamlit as st
import google.generativeai as genai
import os

# --- SAZLAMA ---
# Streamlit Secrets dan kalitni o'qiydi
# Agar kalit topilmasa, xato beradi
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Xatolik: API kalit topilmadi. Streamlit 'Secrets' qismiga 'GEMINI_API_KEY' ni qo'shing.")
    st.stop()

# Sahifa nomi va sozlamalari
st.set_page_config(page_title="AN1 AI - Pro Chatbot", page_icon="🤖")
st.title("🤖 AN1 AI - Gemini 1.5 Pro")
st.subheader("Boshqaruvchi: Nematov Abdulaziz")

# Chat tarixini boshqarish (boshlang'ich holat)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tarixni ekranga chiqarish
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Foydalanuvchi inputi
if prompt := st.chat_input("Tibbiy savolingizni yozing..."):
    # Foydalanuvchi xabarini qo'shish
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI javobi
    with st.chat_message("assistant"):
        try:
            # Model 1.5 Pro
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(prompt)
            
            # Javobni chiqarish
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
            st.warning("Eslatma: Agar '403' yoki 'Permission denied' chiqsa, API kalitingiz Pro modelni qo'llab-quvvatlamasligi mumkin.")
