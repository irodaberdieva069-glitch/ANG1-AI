import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ANG1 AI", page_icon="🤖")
st.title("🤖 ANG1 AI - Sinov rejimi")

api_key = st.sidebar.text_input("Google API Kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Modelni yangiladik
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sinov uchun biror narsa yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Bu yerda AI javob berayotganini ko'rsatamiz
            with st.spinner("AI javob bermoqda..."):
                try:
                    response = model.generate_content(prompt)
                    if response.text:
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    else:
                        st.warning("AI javob qaytardi, lekin matn bo'sh.")
                except Exception as e:
                    st.error(f"Xatolik: {e}")
else:
    st.info("Iltimos, API kalitingizni kiriting.")

