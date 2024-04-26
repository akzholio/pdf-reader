import streamlit as st  # type: ignore
import poppler as pl

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    document = pl.load_from_data(bytes_data)
    for page in document.pages:
        st.write(page)
