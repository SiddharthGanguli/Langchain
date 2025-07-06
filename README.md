=> Use **Ollama** to run open-source LLMs locally (like `gemma`, `llama2`, etc.)
- Use **LangChain** to interact with the LLM in an easy and structured way
- Pass a text prompt and get a smart response from the model

- Use **LLM** to generate text, code, or even images

It's lightweight, works on a **Mac M1** or any other machine that supports Ollama, and doesn't require an internet connection once the model is downloaded.


## => Tools Used

| Tool          | Purpose                                      |
|---------------|----------------------------------------------|
| ** Ollama     | Run open-source LLMs on your local machine   |
| ** LangChain  | Simplifies working with LLMs via Python      |
| ** Python     | Programming language for this project        |

## => How to Set It Up
1. Install Ollama and LangChain using pip:
brew install ollama

2. ollama run gemma:2b
3. Install LangChain using pip:
pip install langchain
pip install langchain-community


## Create a Python Virtual Environment (optional but recommended)
python3 -m venv langchain_env
source langchain_env/bin/activate (for mac users)

then instal  Python Packages (optional but recommended)

