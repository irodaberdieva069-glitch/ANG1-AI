import streamlit as st
import google.generativeai as genai

# API kalitni yuklash
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("🤖 AN1 AI va Tibbiyot") 

# MODELNI O'ZGARTIRDIK: gemini-1.5-flash o'rniga "gemini-pro"
# Bu nom barcha kutubxona versiyalarida 100% ishlaydi.
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Savolingni yoz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # generate_content usuli
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik: {e}")
