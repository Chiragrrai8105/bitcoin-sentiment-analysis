import streamlit as st
import pandas as pd
import pickle

st.title("Bitcoin Sentiment Analysis")

st.header("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Dataset Preview")
    st.dataframe(df.head())

st.header("Prediction")

value = st.number_input("Sentiment Value")
size = st.number_input("Trade Size USD")
price = st.number_input("Execution Price")
fee = st.number_input("Fee")

if st.button("Predict"):

    # Example dummy prediction
    if value > 50:
        st.success("Likely Profit")
    else:
        st.error("Likely Loss")