import json
import os
import requests

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Initialize the Llama model
local_llm = "llama3.1"
llm = ChatOllama(model=local_llm, temperature=0)
llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")

# Schibsted News Archive API endpoint and API key
SCHIBSTED_API_ENDPOINT = "https://newsapi.org/v2/everything?"
API_KEY = "API_KEY"

def fetch_news_articles(query):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "q": query,
        "pageSize": 5
    }
    response = requests.get(SCHIBSTED_API_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["articles"]

def summarize_articles(articles):
    summaries = []
    for article in articles:
        summary = llama_model.summarize(article["content"])
        summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"]
        })
    return summaries

def main():
    user_query = input("Enter the topic you want news about: ")
    articles = fetch_news_articles(user_query)
    summarized_articles = summarize_articles(articles)
    
    for i, article in enumerate(summarized_articles, 1):
        print(f"Article {i}: {article['title']}")
        print(f"Summary: {article['summary']}")
        print(f"Read more: {article['url']}\n")

if __name__ == "__main__":
    main()
