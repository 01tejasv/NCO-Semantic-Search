import streamlit as st
from backend import index_documents, search_query

st.set_page_config(
    page_title="NCO Semantic Search Engine",
    layout="wide"
)

st.title("🕵️‍♂️ NCO Semantic Search Engine")
st.markdown(
    """
Upload your documents below (PDF, DOCX, TXT).  
The search engine will index them and allow you to search for relevant content.
"""
)

# Upload documents
uploaded_files = st.file_uploader(
    "Choose your files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Indexing documents..."):
        index_documents(uploaded_files)
    st.success("✅ Documents indexed successfully!")

# Search query
query = st.text_input("Enter your search query:")

if query:
    results = search_query(query)
    if results:
        st.subheader("Search Results:")
        for res in results:
            st.markdown(f"**📄 {res['document']}**")
            st.info(res['snippet'])
    else:
        st.warning("No results found for your query.")
