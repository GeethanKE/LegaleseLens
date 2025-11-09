from model import run_model
from utils import extract_text_from_pdf

def analyze_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    prompt = f"""Analyze the following legal document and return four sections:
    1. Summary
    2. Pros (benefits to signer)
    3. Cons (potential downsides)
    4. Loopholes (possible risks or ambiguous terms)
    Document:
    {text[:4000]}"""
    response = run_model(prompt)
    try:
        parts = response.split("\n\n")
        return parts[0], parts[1], parts[2], parts[3]
    except:
        return response, "N/A", "N/A", "N/A"