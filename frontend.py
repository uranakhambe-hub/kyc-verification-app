import streamlit as st
import requests

st.title("KYC Verification App")

uploaded_file = st.file_uploader("Upload Document", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file)

    if st.button("Process"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post("http://127.0.0.1:5000/process", files=files)
        result = response.json()

        if result["status"] == "success":
            st.success("Data Extracted")
            st.json(result["data"])
        else:
            st.error(result)