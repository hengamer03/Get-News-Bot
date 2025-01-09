# Get News Bot

This program uses the NewsAPI to find news articles based on a topic you enter. Then, a Language Learning Model (LLM) processes the JSON response, looks through the articles, and provides a summary of the top 5 articles from the list.

## Features

- Fetches news articles from NewsAPI based on user input.
- Summarizes the top 5 articles using an LLM.
- Automatically sets the date to 29 days ago to comply with NewsAPI's free plan limitations.

## Requirements

- Python 3.13
- Langchain as the framework
- [Ollama](https://ollama.com/) with Llama 3.1 model
- NewsAPI API key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Get-News-Bot.git
    cd Get-News-Bot
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your NewsAPI API key:
    ```env
    API_KEY=your_newsapi_key
    ```

## Usage

1. Activate the virtual environment:
    ```sh
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Follow the prompt to enter the topic you want news about. The program will fetch and summarize the top 5 news articles for the given topic.


## Notes

- NewsAPI's free plan has a limit to viewing articles up to 30 days ago. The code includes a function to set the date to 29 days ago to make it easier to use.
- This project uses Ollama with the Llama 3.1 model, but you can connect it to any local or public LLM of your choosing.
