import streamlit as st

#Page Setup#
analysis_page=st.Page(
  page="stock_analysis.py",
  title=" STOCK ANALYSIS",
  icon=":material/finance_mode:",
  default=True,
)

news_page=st.Page(
  page="page2.py",
  title=" NEWS",
  icon=":material/breaking_news:"
)

pg= st.navigation({"MENU":[analysis_page, news_page]})

pg.run()









