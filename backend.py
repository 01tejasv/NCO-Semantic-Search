from utils.text_utils import extract_text

# Global index: stores full text for each document
document_index = {}

def index_documents(uploaded_files):
    """
    Extract full text from uploaded files and store in document_index
    """
    global document_index
    document_index = {}  # reset index

    for file in uploaded_files:
        if file.name not in document_index:
            text = extract_text(file)
            # Join chunks into one string if needed
            if isinstance(text, list):
                text = " ".join(text)
            document_index[file.name] = text
    return document_index

def get_snippet(text, query, length=100):
    """
    Return a snippet around the first occurrence of query
    """
    if not text:
        return ""
    idx = text.lower().find(query.lower())
    if idx == -1:
        return ""
    start = max(idx - length, 0)
    end = min(idx + length + len(query), len(text))
    return "..." + text[start:end] + "..."

def search_query(query):
    """
    Return unique documents with a single snippet
    """
    results = []
    for doc_name, text in document_index.items():
        snippet = get_snippet(text, query)
        if snippet:
            results.append({"document": doc_name, "snippet": snippet})
    return results
