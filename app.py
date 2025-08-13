import streamlit as st
from backend import index_documents, search_query

st.set_page_config(page_title="NCO Semantic Search Engine", layout="wide")

st.title("🕵️‍♂️ NCO Semantic Search Engine")
st.markdown("Upload PDF, DOCX, or TXT documents. Search will return relevant snippets.")

# File upload
uploaded_files = st.file_uploader(
    "Choose files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    # Deduplicate uploaded files by filename
    unique_files = []
    seen = set()
    for file in uploaded_files:
        if file.name not in seen:
            unique_files.append(file)
            seen.add(file.name)

    with st.spinner("Indexing documents..."):
        index_documents(unique_files)
    st.success("✅ Documents indexed successfully!")

# Search input
query = st.text_input("Enter your search query:")

if query:
    results = search_query(query)

    # Ensure unique results at display stage
    unique_results = []
    seen_docs = set()
    for res in results:
        if res['document'] not in seen_docs:
            unique_results.append(res)
            seen_docs.add(res['document'])

    if unique_results:
        st.subheader("Search Results:")
        for res in unique_results:
            st.markdown(f"### 📄 {res['document']}")
            st.markdown(f"_{res['snippet']}_")
    else:
        st.warning("No results found.")
