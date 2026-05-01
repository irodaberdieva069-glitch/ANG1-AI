import streamlit as st
import google.generativeai as genai

# Sahifa nomi va sozlamalari
st.set_page_config(page_title="ANG1 AI", page_icon="🤖")

st.title("🤖 ANG1 AI - Raqamli hamkor")

# Yon panelda API kalitni so'rash
api_key = st.sidebar.text_input("Google API Kalitingizni kiriting:", type="password")

if api_key:
    try:
        # API konfiguratsiyasi
        genai.configure(api_key=api_key)
        
        # Modelni to'g'ri chaqirish (Siz yuborgan ro'yxatda bor model)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Suhbat tarixini saqlash
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Tarixni ekranga chiqarish
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Foydalanuvchi xabarini qabul qilish
        if prompt := st.chat_input("Salom, aka! Nima yordam bera olaman?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI dan javob olish
            with st.chat_message("assistant"):
                try:
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Javob olishda xatolik: {e}")
                
    except Exception as e:
        st.error(f"Ulanishda xatolik: {e}")
else:
    st.info("Iltimos, chap tarafdagi panelga Google API kalitingizni kiriting.")
