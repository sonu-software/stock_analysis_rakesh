

import streamlit as st
import requests

API_KEY = "3dd9352c1f42423388bb8e4e1a337e44"
query = "recent stock market news"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}&pageSize=30"

response = requests.get(url).json()

st.title(f"Latest news about {query}")

for article in response.get("articles", []):
    st.markdown(f"### [{article['title']}]({article['url']})")
    if article.get("urlToImage"):
        st.image(article["urlToImage"], width=200)
    st.write(article.get("description", ""))
    st.markdown("---")

