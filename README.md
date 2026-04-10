# 🤖 AI Chatbot & Research Tool (LangChain + HuggingFace)

## 📌 Overview

This project contains multiple mini AI applications built using **LangChain**, **HuggingFace**, and **Streamlit**.
It demonstrates how to integrate Large Language Models (LLMs) into real-world applications like chatbots and research assistants.

---

## 🚀 Features

### 🔬 Research Tool

* Select research papers like:

  * *Attention Is All You Need*
  * *Diffusion Models Beat GANs*
* Choose explanation style:

  * Beginner-friendly
  * Technical
  * Code-oriented
  * Mathematical
* Select response length (Short / Medium / Long)
* Generates explanations using HuggingFace LLM

---

### 💬 AI Chatbot

* Clean modern UI built with Streamlit
* Chat history support (memory)
* Uses LangChain message system:

  * SystemMessage
  * HumanMessage
  * AIMessage
* Powered by HuggingFace models (Qwen)

---

### ⚡ Simple LLM Scripts

* Basic LLM invocation
* Message-based conversation handling
* Pipeline-based local model usage (TinyLlama)

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* LangChain 🔗
* HuggingFace 🤗
* dotenv (for API keys)

---

## 📂 Project Structure

```
project/
│── research_tool/
│   └── app.py
│
│── chatbot/
│   └── app.py
│
│── simple_llm/
│   └── main.py
│
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Add environment variables

Create a `.env` file and add:

```
HUGGINGFACEHUB_ACCESS_TOKEN=your_token_here
```

---

## ▶️ Run the Applications

### Run Research Tool

```
streamlit run research_tool/app.py
```

### Run Chatbot

```
streamlit run chatbot/app.py
```

---

## 🎯 Learning Outcomes

* Learned how to use LangChain with HuggingFace models
* Built real-world AI apps with UI
* Implemented chat memory and prompt engineering
* Integrated APIs securely using environment variables



## 📌 Future Improvements

* Add RAG (Retrieval-Augmented Generation)
* Deploy on Streamlit Cloud
* Add voice input/output
* Improve UI/UX

---

## 👨‍💻 Author

**Hritik Harsh**
MCA Student, Jain University

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
