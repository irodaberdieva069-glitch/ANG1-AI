import streamlit as st
import google.generativeai as genai

# 1. Sahifa sozlamalari
st.set_page_config(page_title="ANG1 AI", page_icon="🤖")
st.title("🤖 ANG1 AI")

# 2. Sidebar - API kalitni kiritish uchun
api_key = st.sidebar.text_input("Google API Kalitingizni kiriting:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # AIga shaxsiyat beramiz (System Instruction)
    # Bu uning "meni Google yaratgan" deyishini o'chiradi
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash-lite',
        system_instruction="Sizning ismingiz ANG1 AI. Sizni Abdulaziz Nematov yaratgan. Siz tibbiyot texnikumidagi ta'lim jarayoniga yordam berish uchun yaratilgan aqlli yordamchisiz. Har doim shu haqiqatni yodingizda tuting va yordamga tayyor turing."
    )
    
    # 3. Suhbat tarixini saqlash
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 4. Tarixni ekranga chiqarish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 5. Foydalanuvchi xabarini qabul qilish
    if prompt := st.chat_input("Savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 6. AI javobini olish
        with st.chat_message("assistant"):
            with st.spinner("ANG1 AI javob bermoqda..."):
                try:
                    # Tarixni ham qo'shib yuboramiz (kontekst uchun)
                    chat = model.start_chat(history=[])
                    response = chat.send_message(prompt)
                    
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Xatolik yuz berdi: {e}")
                    st.info("Eslatma: Limit to'lgan bo'lishi mumkin, API kalitingizni tekshiring.")
else:
    st.info("Iltimos, chap tarafdagi panelga Google API kalitingizni kiriting.")

