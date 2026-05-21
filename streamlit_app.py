import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Aplikasi Data Mahasiswa")

# Input data
nama = st.text_input("Masukkan Nama")
nilai = st.number_input("Masukkan Nilai", 0, 100)

# Simpan data sementara
if "data" not in st.session_state:
    st.session_state.data = []

# Tombol tambah data
if st.button("Tambah Data"):
    st.session_state.data.append({
        "Nama": nama,
        "Nilai": nilai
    })

# Tampilkan tabel
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)

    st.subheader("Data Mahasiswa")
    st.dataframe(df)

    rata = df["Nilai"].mean()
    st.success(f"Rata-rata nilai: {rata:.2f}")
