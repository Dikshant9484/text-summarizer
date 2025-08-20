🧠 GEN AI Text Summarizer

An AI-powered text summarization web app built with Hugging Face Transformers and Gradio.
It uses the DistilBART (distilbart-cnn-12-6) model to generate concise summaries of long paragraphs.

🚀 Features

Summarizes long text into short, meaningful content.

Built with Transformers pipeline (BART).

Clean Gradio Blocks UI.

Public sharing enabled (share=True).

📂 Project Structure
├── app.py              # Main script for the summarizer
├── requirements.txt    # Dependencies
└── README.md           # Documentation

⚙️ Installation
1️⃣ Clone the repo
git clone https://github.com/your-username/genai-text-summarizer.git
cd genai-text-summarizer

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, create one like:

torch
transformers
gradio
