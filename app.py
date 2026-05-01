import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ANG1 AI", page_icon="🤖")
st.title("🤖 ANG1 AI - Sinov rejimi")

api_key = st.sidebar.text_input("Google API Kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Sinov uchun yengilroq model
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tarixni boshqarish (limit to'lmasligi uchun oxirgi 5 ta xabarni saqlash)
    if len(st.session_state.messages) > 10:
        st.session_state.messages = st.session_state.messages[-10:]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sinov uchun biror narsa yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Limit to'ldi yoki xatolik: {e}")
else:
    st.info("Iltimos, API kalitingizni kiriting.")
