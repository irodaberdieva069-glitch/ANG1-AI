import streamlit as st
import google.generativeai as genai

# Sahifa sozlamalari
st.set_page_config(page_title="AN1 AI Pro", page_icon="🤖")

# API kalitni yuklash
try:
    # Streamlit Secrets dan kalitni olish
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API kalit topilmadi! Streamlit Settings -> Secrets ga GEMINI_API_KEY ni qo'sh.")
    st.stop()

# Sarlavha
st.title("🤖 AN1 AI Pro") 

# Model: 'gemini-pro' (Bu 1.5-flash dan ko'ra barqaror ishlaydi)
# Agar bu ham xato bersa, demak kalitingda muammo bor.
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat tarixini chiqarish
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Foydalanuvchi xabari
if prompt := st.chat_input("Savolingni yoz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Javobni kutish
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
