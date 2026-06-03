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
