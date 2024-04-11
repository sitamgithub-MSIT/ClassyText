# ClassyText

This project uses a new promising zero-shot text classification model [deberta-v3-large-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/deberta-v3-large-zeroshot-v2.0) from the Hugging Face model hub to classify text into different classes. Such models are designed for efficient zeroshot classification with the Hugging Face pipeline. These models can do classification without training data and run on both GPUs and CPUs.

## Tech Stack

- Python (for the programming language)
- Hugging Face Transformers Library (for the zero shot text classification model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/ClassyText.git`
2. Create a virtual environment: `python -m venv tutorial-env`
3. Activate the virtual environment: `tutorial-env\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the Gradio application: `python app.py`

Now, open up your local host and you should see the web application running. For more information, refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/ClassyText).

## Usage

Once the application is up and running, you can interact with the interface to classify text into different classes of your choice. The model used in this project is a zero-shot text classification model, which means that it can classify text into classes that it has not seen during training. This is a powerful feature that can be used in a variety of applications.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
