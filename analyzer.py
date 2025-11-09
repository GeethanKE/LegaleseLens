import fitz  # PyMuPDF
from model import query_model

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def analyze_legal_text(text):
    """Send text to model for analysis."""
    prompt = f"""
You are a legal assistant AI analyzing an NDA or contract.
Read the following text and output a structured summary:

1. **Key Clauses**
2. **Pros & Cons**
3. **Potential Loopholes**
4. **Plain English Summary**

Text:
{text[:6000]}  # limit to keep response short
    """
    return query_model(prompt)
