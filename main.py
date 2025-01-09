import json
import os
import requests

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from datetime import datetime, timedelta

load_dotenv()

# Initialize the Llama model
local_llm = "llama3.1"
llm = ChatOllama(model=local_llm, temperature=0)
llm_json_mode = ChatOllama(model=local_llm, temperature=0, format="json")

# Set correct date for API search
current_date = datetime.now()
date_29_days_ago = current_date - timedelta(days=29)
formatted_date = date_29_days_ago.strftime("%Y-%m-%d")

def fetch_news_articles(query):
    try:
        API_KEY = os.getenv("API_KEY")
        API = f"https://newsapi.org/v2/everything?q={query}&from={formatted_date}&sortBy=popularity&apiKey={API_KEY}"

        params = {
            "q": query,
            "pageSize": 5
        }
        response = requests.get(API)
        response.raise_for_status()
        data = response.json()["articles"]
        print(data)
    except Exception as e:
        print(f"Error fetching news articles: {e}")
        return None
    return data

prompt = PromptTemplate(
    input_variables=["user_query"],
    template="Could you find some news articles on: {user_query}"
)

chain = prompt | llm | StrOutputParser()

user_query = input("Please enter the topic you want news about: ")

def summarize_articles(articles):
    summaries = []
    for article in articles:
        summary = llm.summarize(article["content"])
        summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["url"]
        })
    return summaries

def main():
    result = llm.invoke(user_query)
    articles = fetch_news_articles(user_query)
    summarized_articles = summarize_articles(articles)
    
    for i, article in enumerate(summarized_articles, 1):
        print(f"Article {i}: {article['title']}")
        print(f"Summary: {article['summary']}")
        print(f"Read more: {article['url']}\n")

if __name__ == "__main__":
    main()