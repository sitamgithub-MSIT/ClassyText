# Necessary imports
import sys
from typing import Dict
from src.logger import logging
from src.exception import CustomExceptionHandling
from transformers import pipeline
import gradio as gr


# Load the zero-shot classification model
classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/ModernBERT-large-zeroshot-v2.0",
)


def ZeroShotTextClassification(
    text_input: str, candidate_labels: str, multi_label: bool
) -> Dict[str, float]:
    """
    Performs zero-shot classification on the given text input.

    Args:
        - text_input: The input text to classify.
        - candidate_labels: A comma-separated string of candidate labels.
        - multi_label: A boolean indicating whether to allow the model to choose multiple classes.

    Returns:
        Dictionary containing label-score pairs.
    """
    try:
        # Check if the input and candidate labels are valid
        if not text_input or not candidate_labels:
            gr.Warning("Please provide valid input and candidate labels")

        # Split and clean the candidate labels
        labels = [label.strip() for label in candidate_labels.split(",")]

        # Log the classification attempt
        logging.info(f"Attempting classification with {len(labels)} labels")

        # Perform zero-shot classification
        hypothesis_template = "This text is about {}"
        prediction = classifier(
            text_input,
            labels,
            hypothesis_template=hypothesis_template,
            multi_label=multi_label,
        )

        # Return the classification results
        logging.info("Classification completed successfully")
        return {
            prediction["labels"][i]: prediction["scores"][i]
            for i in range(len(prediction["labels"]))
        }

    # Handle exceptions that may occur during the process
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
