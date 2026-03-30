# 🥗 Vegetarian Recipe RAG Bot

Python | LlamaIndex | OpenAI | Groq | HuggingFace Embeddings | Gradio 
---

A Retrieval-Augmented Generation (RAG) system for answering vegetarian cooking questions using external recipe sources.

This project combines modern LLMs with a structured retrieval pipeline to provide context-aware answers about vegetarian meals, ingredients, and cooking techniques.

## 🔍 Project Overview

This project demonstrates the use of retrieval-augmented generation (RAG) to answer vegetarian cooking questions using structured recipe data.
Users can ask queries such as:

* “What can I cook with chickpeas and spinach?”
* “Give me a quick high-protein vegetarian dinner”
* “How do I make a basic tomato sauce?”

Recipes are represented as text embeddings generated from HuggingFace models, which are stored in a vector database you build locally. The RAG pipeline retrieves relevant recipes and passes them to an LLM (OpenAI GPT) to generate context-aware answers.

The project showcases how machine learning can support recipe discovery and dietary guidance.

## ⚙️ How it works

1. **Document ingestion**
   Recipe PDFs are processed and converted into structured text.

2. **Embedding & indexing**
   Each text chunk is converted into vector embeddings using a HuggingFace model and stored in a local vector database for semantic search.

3. **Retrieval + generation**
   When a user submits a query, relevant recipe chunks are retrieved from the vector database and passed to an LLM (OpenAI GPT) to generate a context-aware answer.

4. **Hosting with Gradio**
    The RAG bot is deployed using Gradio, creating a simple web interface where users can input queries and receive recipe answers in real time. This allows the bot to be accessed online without needing to run the notebook locally.

## 📚 Data sources

This repository does **not include the original PDF files or vector database** due to copyright considerations.

Instead, it provides:

* Links to publicly available sources
* Scripts to process and index the data locally

**Users are responsible for ensuring they have the right to use any external content.**

Example PDFs can be found at the following URLs:
* [Emma’s Vegetarian Cookbook](https://www.lem.lu/pdf/trape/2021/Holzapfel,%20Emma%20(6C2)%20-%20Emma%27s%20Vegetarian%20Cookbook.pdf)
* [Low-Budget Vegetarian Ebook](https://www.lowbudgetvegetarian.com/wp-content/uploads/2021/09/Low-Budget-Vegetarian-Ebook.pdf)
* [Complete Vegetarian Book](https://completevegetarianbook2015.files.wordpress.com/2015/02/complete-vegetarian-blad.pdf)
* [Veggie Happy Recipe Ebook](https://www.wreckingroutine.com/wp-content/uploads/2021/01/Veggie-Happy-Recipe-Ebook.pdf)
* [Creative Vegetarian Cooking](https://rssb.org/pdfs/Creative%20Vegetarian%20Cooking.pdf)

*These PDFs are provided for testing and educational purposes only. Please respect copyright laws when using them.*

## 🛠️ Tools & Libraries

* Python
* LlamaIndex – document indexing and retrieval
* HuggingFace Embeddings – vectorizing recipe text
* Gradio / FastAPI – optional web interface
* pandas, numpy – data handling
* Jupyter Notebook – prototyping

**LLM for answer generation** — queries are answered using an LLM. The project supports multiple backends including:
- OpenAI GPT
- Groq LLMs (e.g., `llama-3.3-70b-versatile`)
- Open-source HuggingFace models (e.g., `openai/gpt-oss-120b`)
- Qwen LLMs (`qwen/qwen3-32b`)


## 📝 Evaluation

* Manual testing with sample queries
* Check that answers are accurate, relevant, and vegetarian-friendly
* Evaluate semantic similarity and quality of retrieved chunks


## 🚀 How to use the RAG bot

Clone the repository and install dependencies:

``` bash
git clone https://github.com/yourusername/vegetarian-rag-bot.git
cd vegetarian-rag-bot
pip install -r requirements.txt
```

Open and run the notebook

`gradio_RAG.ipynb`


## 📊 Results

* Queries return context-aware vegetarian recipes using HuggingFace embeddings and an LLM
* System supports ingredient-based and dietary queries
* Flexible pipeline allows scaling with more recipes or additional features like nutrition tracking or meal planning

## ⚠️ Disclaimer

This project is for educational and experimental purposes.
All recipe content belongs to its respective owners.
