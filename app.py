import streamlit as st
from backend import index_documents, search_query

st.set_page_config(page_title="NCO Semantic Search Engine", layout="wide")

st.title("🕵️‍♂️ NCO Semantic Search Engine")
st.markdown("Upload PDF, DOCX, or TXT documents. Search will return relevant snippets.")

uploaded_files = st.file_uploader(
    "Choose files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Indexing documents..."):
        index_documents(uploaded_files)
    st.success("✅ Documents indexed successfully!")

query = st.text_input("Enter your search query:")

if query:
    results = search_query(query)
    if results:
        st.subheader("Search Results:")
        for res in results:
            st.markdown(f"**📄 {res['document']}**")
            st.info(res['snippet'])
    else:
        st.warning("No results found.")
