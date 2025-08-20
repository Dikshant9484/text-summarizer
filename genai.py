import torch
import gradio as gr
from transformers import pipeline

# Create the summarization pipeline
textsummary = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

# Define the summary function
def summarytext(input):
    output = textsummary(input)
    return output[0]['summary_text']

# Close previous Gradio interfaces if any
gr.close_all()

# Use Blocks for a custom UI layout
with gr.Blocks(title="@GEN AI TEXT SUMMARIZATION") as demo:
    gr.Markdown(
        """
        # 🧠 GEN AI Text Summarizer
        Welcome to the AI-powered text summarization tool using a BART-based transformer model.  
        Paste any lengthy paragraph or content, and get a concise summary in seconds!
        """
    )

    with gr.Row():
        input_text = gr.Textbox(
            label="📥 Input Text",
            placeholder="Paste your text here...",
            lines=8
        )

    with gr.Row():
        summarize_btn = gr.Button("🔍 Summarize")
    
    with gr.Row():
        output_text = gr.Textbox(
            label="📄 Summarized Text",
            lines=4,
            interactive=False
        )

    summarize_btn.click(fn=summarytext, inputs=input_text, outputs=output_text)

# Launch the app with sharing enabled
demo.launch(share=True)
