import streamlit as st
from PIL import Image

# 1. Sahifa sozlamalari
st.set_page_config(page_title="AN1 AI", layout="wide")

# 2. Banner (Hero Section) funksiyasi
def render_banner():
    st.markdown(
        """
        <style>
        .banner-img {
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    try:
        # Rasmni yuklash
        image = Image.open('IMG_1530.jpg')
        st.image(image, use_container_width=True)
    except FileNotFoundError:
        st.error("Xatolik: 'IMG_1530.jpg' fayli topilmadi.")

# 3. Asosiy dastur qismi
def main():
    render_banner()
    
    # Loyiha nomi endi AN1 AI
    st.title("AN1 AI - Innovatsion Tibbiy Texnik Tizim")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bo'limlar")
        st.write("• Farmatsiya")
        st.write("• Hamshiralik ishi")
        st.write("• Klinik fanlar")
        
    with col2:
        st.subheader("Tizim holati")
        st.success("Tizim faol")
        st.info("AN1 AI boshqaruv paneli - 2026")

if __name__ == "__main__":
    main()
