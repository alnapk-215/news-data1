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