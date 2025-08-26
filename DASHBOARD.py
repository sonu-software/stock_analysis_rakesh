import streamlit as st

#Page Setup#
about_page=st.Page(
  page="stock_analysis.py",
  title="MAIN PAGE",
  default=True,
)

pg= st.navigation(pages=[about_page])

pg.run

st.title("🏠 Home Page")
st.write("Welcome to the Stock Diary App!")

