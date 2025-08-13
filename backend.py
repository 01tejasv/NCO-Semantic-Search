from utils.text_utils import extract_text

# In-memory index: {filename: full_text}
document_index = {}

def index_documents(uploaded_files):
    """
    Extract text from uploaded files and store in document_index
    """
    global document_index
    document_index = {}  # reset index

    for file in uploaded_files:
        text = extract_text(file)
        if text:
            document_index[file.name] = text

    return document_index

def get_snippet(text, query, length=100):
    """
    Return a small snippet around the first occurrence of query
    """
    idx = text.lower().find(query.lower())
    if idx == -1:
        return ""
    start = max(idx - length, 0)
    end = min(idx + length + len(query), len(text))
    return "..." + text[start:end] + "..."

def search_query(query):
    """
    Search the indexed documents and return only unique documents with snippet
    """
    results = []
    for doc_name, text in document_index.items():
        snippet = get_snippet(text, query)
        if snippet:  # only add if snippet is found
            results.append({"document": doc_name, "snippet": snippet})
    return results
