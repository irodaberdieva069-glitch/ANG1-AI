import streamlit as st
import google.generativeai as genai

# 1. Sahifa sozlamalari
st.set_page_config(page_title="ANG1 AI", page_icon="🤖")

# Yon menyuga logotip va sarlavha qo'yish
with st.sidebar:
    st.image("logo.png", use_container_width=True) # Fayl nomi 'logo.png' ekanligiga ishonch hosil qiling
    st.title("ANG1 AI")
    st.write("Innovatsion tibbiy texnik tizim")
    
    # 2. API kalitini kiritish
    api_key = st.text_input("Google API Kalitingizni kiriting:", type="password")

# 3. Asosiy sahifa
st.title("🤖 ANG1 AI")

if api_key:
    genai.configure(api_key=api_key)
    
    # Modelni sozlash
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash-lite',
        system_instruction="Sizning ismingiz ANG1 AI. Sizni Abdulaziz Nematov yaratgan. Siz tibbiyot texnikumidagi ta'lim jarayonida yordam berasiz."
    )

    # 4. Suhbat tarixini saqlash
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tarixni ekranga chiqarish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Foydalanuvchi kiritgan matnni qayta ishlash
    if prompt := st.chat_input("Savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI javobi
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Iltimos, chap tarafdagi menyuda API kalitingizni kiriting.")
