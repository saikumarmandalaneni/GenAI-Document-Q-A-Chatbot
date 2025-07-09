import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import google.generativeai as genai
import os

# ──────────────────────── CONFIG ─────────────────────────
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="📄 GenAI DocuBot", page_icon="🤖", layout="wide")

# ──────────────────────── STYLING ─────────────────────────
st.markdown("""
    <style>
    html, body, [class*="View"]  {
        background-color: #0F1117;
        color: #F4F6FC;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4, strong {
        color: #F4F6FC;
    }
    .stButton > button {
        color: white;
        background-color: #3B82F6;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stTextInput > div > div > input {
        background-color: #1C1F26;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ──────────────────────── UI HEADER ───────────────────────
st.title("📄 GenAI Document Assistant")
st.caption("Upload a PDF, summarize its content, and chat with it using Gemini ✨")

# ──────────────────────── CHAT HISTORY ────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ──────────────────────── FILE UPLOAD ─────────────────────
uploaded_files = st.file_uploader("📤 Upload one or more PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    full_text = ""
    all_docs = []

    for file in uploaded_files:
        pdf_reader = PdfReader(file)
        text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
        full_text += text

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(text)
        docs = [Document(page_content=chunk) for chunk in chunks]
        all_docs.extend(docs)

    temp_dir = "./temp_chroma_db"
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
    vectordb = Chroma.from_documents(all_docs, embedding=embeddings, persist_directory=temp_dir)
    vectordb.persist()
    retriever = vectordb.as_retriever()

    # ──────────────── DOCUMENT SUMMARY ────────────────
    with st.expander("🧠 Summarize Document(s)"):
        if st.button("Generate Summary"):
            model = genai.GenerativeModel("gemini-1.5-flash")
            summary = model.generate_content(f"Summarize this document:\n{full_text}").text
            st.success("✅ Summary Generated")
            st.write(summary)
            st.download_button("📥 Download Summary", summary, file_name="summary.txt")

    # ──────────────── Q&A SECTION ────────────────
    question = st.text_input("💬 Ask something about the documents:")
    if question:
        docs = retriever.get_relevant_documents(question)
        context = "\n\n".join([doc.page_content for doc in docs]) if docs else ""

        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = [f"Context:\n{context}", f"Question: {question}"] if context else f"General Question: {question}"
        response = model.generate_content(prompt)
        answer = response.text

        st.write("💬", answer)
        st.download_button("📥 Download Answer", answer, file_name="answer.txt", key=question)

        st.session_state.chat_history.append((question, answer))

    # ──────────────── CHAT HISTORY ────────────────
    if st.session_state.chat_history:
        st.markdown("---")
        st.subheader("📝 Chat History")
        for q, a in st.session_state.chat_history:
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**A:** {a}")

