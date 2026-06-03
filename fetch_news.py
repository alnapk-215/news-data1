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

    sentiment_score = TextBlob(title).sentiment.polarity
    
    if sentiment_score > 0:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    cur.execute("""
        INSERT INTO news_data
        (news_date, source_name, title, sentiment_score, sentiment_label)
        VALUES (%s, %s, %s, %s, %s)
    """, (news_date, source_name, title, sentiment_score, sentiment_label))

conn.commit()