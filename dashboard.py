import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="News Analytics Dashboard",
    layout="wide"
)
DATABASE_URL = "postgresql://postgres:alnarajeevan@news-db.cirma8a8kvzz.us-east-1.rds.amazonaws.com:5432/newsdb"

engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM news_data ORDER BY created_at DESC", engine)
