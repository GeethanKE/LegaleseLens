import streamlit as st
from analyzer import analyze_pdf
import tempfile

st.set_page_config(page_title="LegaleseLens", page_icon="⚖️", layout="centered")
st.title("⚖️ LegaleseLens")
st.caption("Analyze legal PDFs offline — powered by local LLMs via Ollama")

uploaded_file = st.file_uploader("Upload a legal PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("Analyzing your document..."):
        summary, pros, cons, loopholes = analyze_pdf(tmp_path)

    st.subheader("📜 Summary")
    st.write(summary)
    st.subheader("✅ Pros")
    st.write(pros)
    st.subheader("⚠️ Cons")
    st.write(cons)
    st.subheader("🕳️ Potential Loopholes")
    st.write(loopholes)