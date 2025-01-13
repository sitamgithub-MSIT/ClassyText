# ClassyText

Zero-shot classification is a transfer learning method that uses a pre-trained language model to predict a class not seen during training. This project uses a new promising zero-shot text classification model [ModernBERT-large-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/ModernBERT-large-zeroshot-v2.0) from the Hugging Face model hub to classify text into different classes. Models in this series are designed for efficient zero-shot classification with the Hugging Face pipeline. These models can classify without training data and run on both GPUs and CPUs.

## Project Structure

The project is structured as follows:

- `src\`: The folder that contains the source code for the project.

  - `modernbert\classifier.py`: The file that contains the function for classifying text into different classes using the ModernBERT zero-shot text classification model.

  - `config.py`: This file contains the configuration for the used model.
  - `logger.py`: This file contains the project's logging configuration.
  - `exception.py`: This file contains the exception handling for the project.

- `app.py`: This file contains the code for the Gradio application.
- `requirements.txt`: This file contains the required dependencies for the project.
- `LICENSE`: This file contains the license information for the project.
- `README.md`: This file contains the information about the project.
- `assets`: This folder contains the screenshots for working on the application.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the zero-shot text classification model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/ClassyText.git`
2. Change the directory: `cd ClassyText`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment: `tutorial-env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `python app.py`

Now, open up your local host and you should see the web application running. For more information, refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/ClassyText).

## Usage

Once the application is up and running, you can interact with the interface to classify text into different classes of your choice. The model used in this project is a zero-shot text classification model, meaning it can classify text it has not seen during training. This is a powerful feature that can be used in a variety of applications, such as content moderation, sentiment analysis of new product reviews, topic classification of news articles, identifying the intent of customer support queries, and classifying social media posts based on their subject matter; essentially any situation where you want to quickly categorize text into predefined classes without a large labeled training dataset for each class.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
