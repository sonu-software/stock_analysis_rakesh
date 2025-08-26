import streamlit as st

#Page Setup#
analysis_page=st.Page(
  page="stock_analysis.py",
  title=" STOCK ANALYSIS",
  icon=":material/finance_mode:",
  default=True,
)

news_page=st.Page(
  page="news.py",
  title=" NEWS",
  icon=":material/breaking_news:"
)


pg= st.navigation({"MENU":[analysis_page, news_page]})

st.sidebar.markdown("Your Personal Trade Diary")
st.logo("stock-logo.png")


pg.run()












