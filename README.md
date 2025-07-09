# 📄 GenAI Document Q&A Chatbot

A modern, Streamlit-powered GenAI assistant for exploring PDF documents. Upload documents, get instant summaries, and chat with their contents using Gemini AI + LangChain.

![App Screenshot](Screenshot%20(20).png)

---

## 🧪 Demo
> 🔗 [Live App Link](https://saikumarmandalaneni-genai-document-q-a-chatbot.streamlit.app) – Instantly chat with your PDFs.

---

## 📌 Updates
We’re actively improving the chatbot experience:
- ✅ Streamlined deployment
- ✅ Improved UI styling (dark mode)
- 🧠 Image & document Q&A coming soon

Stay tuned for more AI assistant features!

---

## 🌐 Official Hosted Version
You can use the app without downloading anything:
👉 [Streamlit Cloud App](https://saikumarmandalaneni-genai-document-q-a-chatbot.streamlit.app)

---

## ❤️ Sponsor
If this project helped you, consider ⭐️ starring the repo or [buying me a coffee](https://www.buymeacoffee.com/) to support open-source development!

---

## 📂 Issues
Please only open **actual bug reports**. For general help, use GitHub **Discussions**.

---

## 💬 Discussions
Use the [Discussions tab](https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot/discussions) for questions, help, or feature ideas. Chances are others have the same question.

---

## ⚡ Quickstart (Local)
### 1. Clone the Repo
```bash
git clone https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot.git
cd GenAI-Document-Q-A-Chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Key
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_key_here
```

### 4. Run the App
```bash
streamlit run app_with_addons.py
```

---

## 📦 Tech Stack
| Component      | Description                              |
|----------------|------------------------------------------|
| Streamlit      | Interactive web UI                       |
| LangChain      | Document parsing, embeddings, retrieval  |
| ChromaDB       | Vector database                          |
| HuggingFace    | Embedding model (MiniLM-L6-v2)           |
| Google Gemini  | Large Language Model (LLM)               |
| PyPDF2         | PDF text extraction                      |

---

## 📸 Screenshot
> ![Screenshot](Screenshot%20(20).png)

---

## 🚀 Deployment (Streamlit Cloud)
1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud and log in with GitHub
3. Click "New App" → Select this repo → Set `app_with_addons.py` as the entry point
4. In **App Settings > Secrets**, add your API key:
```
GEMINI_API_KEY=your_gemini_key_here
```
5. Deploy and enjoy 🎉

---

## ✨ Credits
Built by [Saikumarmandalaneni](https://github.com/saikumarmandalaneni)

---

## 📈 Stats
[![Stars](https://img.shields.io/github/stars/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot?style=social)](https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot/stargazers)
[![Forks](https://img.shields.io/github/forks/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot?style=social)](https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot/fork)
[![Last Commit](https://img.shields.io/github/last-commit/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot?color=blue)](https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot/commits/main)
[![Repo Views](https://komarev.com/ghpvc/?username=saikumarmandalaneni&label=Repo%20views&color=0e75b6&style=flat)](https://github.com/saikumarmandalaneni/GenAI-Document-Q-A-Chatbot)

---

_This is a non-commercial, open-source research project for AI and NLP exploration._
