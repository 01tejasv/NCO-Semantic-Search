import os
from utils.text_utils import extract_text
import numpy as np

# Simple in-memory "index"
DOCUMENTS = []
DOCUMENT_TEXTS = []

def index_documents(files):
    global DOCUMENTS, DOCUMENT_TEXTS
    for file in files:
        text = extract_text(file)
        DOCUMENTS.append(file.name)
        DOCUMENT_TEXTS.append(text)

def search_query(query, top_k=5):
    # Dummy search: return first top_k documents containing any query word
    query_words = query.lower().split()
    results = []
    for doc_name, text in zip(DOCUMENTS, DOCUMENT_TEXTS):
        if any(word in text.lower() for word in query_words):
            results.append(doc_name)
    return results[:top_k]

