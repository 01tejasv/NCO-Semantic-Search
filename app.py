import streamlit as st
from backend import index_documents, search_query

st.set_page_config(page_title="NCO Semantic Search", layout="wide")
st.title("NCO Semantic Search Engine")

# Upload documents
uploaded_files = st.file_uploader("Upload your documents", type=["pdf","docx","txt"], accept_multiple_files=True)

if uploaded_files:
    st.write("Indexing documents...")
    index_documents(uploaded_files)
    st.success("Documents indexed successfully!")

# Search
query = st.text_input("Enter your search query:")

if query:
    results = search_query(query)
    st.write("### Search Results:")
    for i, res in enumerate(results):
        st.write(f"{i+1}. {res}")

