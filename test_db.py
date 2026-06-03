import psycopg2

conn = psycopg2.connect(
    host="news-db.cirma8a8kvzz.us-east-1.rds.amazonaws.com",
    database="newsdb",
    user="postgres",
    password="alnarajeevan",
    port="5432"
)

print("Database connected successfully")

cur = conn.cursor()



cur.execute("""
CREATE TABLE IF NOT EXISTS news_data (
    id SERIAL PRIMARY KEY,
    news_date DATE,
    source_name VARCHAR(255),
    title TEXT,
    sentiment_score FLOAT,
    sentiment_label VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

