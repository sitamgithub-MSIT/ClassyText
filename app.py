# Necessary imports
import gradio as gr
from src.modernbert.classifier import ZeroShotTextClassification


# Examples to display in the interface
examples = [
    [
        "I have a problem with my iPhone that needs to be resolved asap!",
        "urgent, not urgent, phone, tablet, computer",
        False,
    ],
    [
        "Angela Merkel is a politician in Germany and leader of the CDU",
        "politics, economy, entertainment, environment",
        False,
    ],
    [
        "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!",
        "refund, legal, faq",
        True,
    ],
]

# Title and description and article for the interface
title = "Zero Shot Text Classification"
description = "Classify text using zero-shot classification with ModernBERT-large zeroshot model! Provide a text input and a list of candidate labels separated by commas. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2412.13663' target='_blank'>Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference</a> | <a href='https://huggingface.co/MoritzLaurer/ModernBERT-large-zeroshot-v2.0' target='_blank'>Model Page</a></p>"


# Launch the interface
demo = gr.Interface(
    fn=ZeroShotTextClassification,
    inputs=[
        gr.Textbox(label="Input", placeholder="Enter text to classify"),
        gr.Textbox(
            label="Candidate Labels",
            placeholder="Enter candidate labels separated by commas",
        ),
        gr.Checkbox(label="Multi-Label", value=False),
    ],
    outputs=gr.Label(label="Classification"),
    title=title,
    description=description,
    article=article,
    examples=examples,
    cache_examples=True,
    cache_mode="lazy",
    theme="Soft",
    flagging_mode="never",
)
demo.launch(debug=False)
