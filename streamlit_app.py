import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Forecasting Penjualan Sederhana")

# Upload file
uploaded_file = st.file_uploader(
    "Upload File Excel",
    type=["xlsx"]
)

if uploaded_file is not None:

    # Baca excel
    df = pd.read_excel(uploaded_file)

    st.subheader("Data Awal")
    st.dataframe(df)

    # Pastikan ada kolom Penjualan
    if "Penjualan" in df.columns:

        # Moving Average Forecast
        df["Forecast"] = (
            df["Penjualan"]
            .rolling(window=3)
            .mean()
        )

        st.subheader("Hasil Forecast")
        st.dataframe(df)

        # Grafik
        fig, ax = plt.subplots(figsize=(10,5))

        ax.plot(
            df.index,
            df["Penjualan"],
            label="Actual",
            marker="o"
        )

        ax.plot(
            df.index,
            df["Forecast"],
            label="Forecast",
            marker="o"
        )

        ax.set_title("Grafik Forecasting")
        ax.set_xlabel("Periode")
        ax.set_ylabel("Penjualan")
        ax.legend()

        st.pyplot(fig)

    else:
        st.error(
            "Kolom 'Penjualan' tidak ditemukan"
        )
