# Necessary imports
import gradio as gr
from transformers import pipeline

# Load the zero-shot classification model
classifier = pipeline(
    "zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
)


# Function to perform zero-shot classification
def ZeroShotTextClassification(text_input, candidate_labels):
    """
    Performs zero-shot classification on the given text input using the provided candidate labels.

    Args:
      text_input (str): The input text to classify.
      candidate_labels (str): A comma-separated string of candidate labels.

    Returns:
      dict: A dictionary containing the predicted labels as keys and their corresponding scores as values.
    """

    # Split the candidate labels
    labels = [label.strip(" ") for label in candidate_labels.split(",")]

    # Output dictionary to store the predicted labels and their scores
    output = {}

    # Perform zero-shot classification
    prediction = classifier(text_input, labels)

    # Create a dictionary with the predicted labels and their corresponding scores
    for i in range(len(prediction["labels"])):
        output[prediction["labels"][i]] = prediction["scores"][i]

    # Return the output
    return output


# Examples to display in the interface
examples = [
    ["I love to play the guitar", "music, artist, food, travel"],
    ["I am a software engineer at Google", "technology, engineering, art, science"],
    ["I am a professional basketball player", "sports, athlete, chef, politics"],
]

# Launch the interface
demo = gr.Interface(
    fn=ZeroShotTextClassification,
    inputs=[gr.Textbox(label="Input"), gr.Textbox(label="Candidate Labels")],
    outputs=gr.Label(label="Classification"),
    title="Zero Shot Text Classification",
    description="Classify text using zero-shot classification with DeBERTa-v3-large-zeroshot model! Provide a text input and a list of candidate labels separated by commas.",
    examples=examples,
    theme="Soft",
    allow_flagging="never",
)
demo.launch(debug=False)
