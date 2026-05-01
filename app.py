import streamlit as st
import google.generativeai as genai

# 1. Sahifa sozlamalari
st.set_page_config(page_title="ANG1 AI", page_icon="🤖")

# 2. Yon menyuga rasm va ma'lumot qo'yish
with st.sidebar:
    # GitHub'dagi rasm nomiga moslab yozildi
    st.image("IMG_1530.png", use_container_width=True) 
    st.title("ANG1 AI")
    st.write("Innovatsion tibbiy texnik tizim")
    
    # API kaliti
    api_key = st.text_input("Google API Kalitingizni kiriting:", type="password")

# 3. Asosiy sahifa
st.title("🤖 ANG1 AI")

if api_key:
    genai.configure(api_key=api_key)
    
    # AI Modelini sozlash
    model = genai.GenerativeModel(
        model_name='gemini-2.0-flash', # Model nomini yangiladim
        system_instruction="Sizning ismingiz ANG1 AI. Sizni Abdulaziz Nematov yaratgan. Siz tibbiyot texnikumidagi ta'lim jarayonida yordam berasiz."
    )

    # 4. Suhbat tarixini saqlash
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tarixni ekranga chiqarish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Foydalanuvchi inputi
    if prompt := st.chat_input("Savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI javobi
        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Xatolik yuz berdi: {e}")
else:
    st.info("Iltimos, chap tarafdagi menyuda API kalitingizni kiriting.")
