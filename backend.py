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
            # Join chunks if extract_text returns a list
            if isinstance(text, list):
                text = " ".join(text)
            elif not isinstance(text, str):
                text = str(text)
            document_index[file.name] = text
    return document_index

def get_snippet(text, query, length=100):
    """
    Return the first snippet containing the query
    """
    if not text:
        return ""
    # Normalize for case-insensitive search
    text_lower = text.lower()
    query_lower = query.lower()
    idx = text_lower.find(query_lower)
    if idx == -1:
        return ""
    start = max(idx - length, 0)
    end = min(idx + length + len(query), len(text))
    return "..." + text[start:end] + "..."

def search_query(query):
    """
    Return a unique document result per file with a snippet
    """
    results = []
    for doc_name, text in document_index.items():
        snippet = get_snippet(text, query)
        if snippet:
            results.append({
                "document": doc_name,
                "snippet": snippet
            })
    # Ensure only one entry per document
    unique_results = {}
    for res in results:
        unique_results[res["document"]] = res
    return list(unique_results.values())
