import requests
import psycopg2
from textblob import TextBlob
from datetime import datetime

API_KEY = "9937956bd25b4d39a610bafcaa761aa4"

conn = psycopg2.connect(
    host="news-db.cirma8a8kvzz.us-east-1.rds.amazonaws.com",
    database="newsdb",
    user="postgres",
    password="alnarajeevan",
    port="5432"
)

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "category": "technology",
    "apiKey": API_KEY
}

print(response.json())

articles = response.json().get("articles", [])

cur = conn.cursor()

for article in articles:
    title = article.get("title")
    source_name = article.get("source", {}).get("name")
    published_at = article.get("publishedAt")

    news_date = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").date()
