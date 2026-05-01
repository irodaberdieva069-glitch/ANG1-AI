import streamlit as st
import google.generativeai as genai

st.title("🤖 ANG1 AI - Raqamli hamkor")

api_key = st.sidebar.text_input("Google API Kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Modelni avtomatik aniqlash uchun oddiyroq chaqiruv
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Nima yordam bera olaman?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # generate_content'ni ishlatamiz
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Xatolik: {e}. Iltimos, API kalitingizni va model nomini tekshiring.")
        # Mavjud modellarni ro'yxatini ko'rsatish
        st.write("Mavjud modellar:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                st.write(m.name)
