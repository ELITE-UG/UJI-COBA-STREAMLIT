import streamlit as st

# Judul aplikasi
st.title("Aplikasi Sederhana Streamlit")

# Input nama
nama = st.text_input("Masukkan nama kamu:")

# Tombol
if st.button("Tampilkan"):
    st.success(f"Halo, {nama}! Selamat belajar Streamlit 🚀")
