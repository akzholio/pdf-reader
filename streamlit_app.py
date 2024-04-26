import streamlit as st  # type: ignore
from poppler import load_from_data

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    pdf_document = load_from_data(bytes_data)
    page_1 = pdf_document.create_page(0)
    page_1_text = page_1.text()
    st.write(page_1_text)
