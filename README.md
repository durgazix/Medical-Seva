# Medical Chat Bot

MedicalGuru is an AI-powered health assistant web application that leverages generative AI and retrieval-augmented generation (RAG) to answer medical queries using a knowledge base and large language models.

## Features

- Chat interface for medical Q&A
- Retrieval-augmented generation using Pinecone vector store
- Integration with Google Gemini and Hugging Face embeddings
- Flask-based web server
- Customizable prompts and system instructions

## Project Structure

```
.env
.gitignore
app.py
LICENSE
requirements.txt
setup.py
store_index.py
templates.py
Data/
    Medical_book.pdf
medical_chatbot.egg-info/
    dependency_links.txt
    PKG-INFO
    SOURCES.txt
    top_level.txt
research/
    trials.ipynb
src/
    __init__.py
    helper.py
    prompt.py
    __pycache__/
        __init__.cpython-310.pyc
        __init__.cpython-313.pyc
        helper.cpython-310.pyc
        helper.cpython-313.pyc
        prompt.cpython-310.pyc
static/
    style.css
templates/
    chat.html
```

## Installation

1. Clone the repository.
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up environment variables in `.env`:
    ```
    PINECONE_API_KEY=your_pinecone_api_key
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Start the Flask server:
    ```sh
    python app.py
    ```
2. Open your browser and navigate to `http://localhost:5000` to access the chat interface.

## Main Files

- [`app.py`](app.py): Main Flask application and API endpoints.
- [`src/helper.py`](src/helper.py): Embedding download and utility functions.
- [`src/prompt.py`](src/prompt.py): Prompt templates for the chatbot.
- [`templates/chat.html`](templates/chat.html): Frontend chat interface.
- [`static/style.css`](static/style.css): Styles for the web interface.
- [`Data/Medical_book.pdf`](Data/Medical_book.pdf): Source medical knowledge base.
- [`research/trials.ipynb`](research/trials.ipynb): Experimental notebooks.

## License

See [`LICENSE`](LICENSE) for details.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)