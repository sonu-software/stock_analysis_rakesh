import streamlit as st

#Page Setup#
about_page=st.Page(
  page="stock_analysis.py",
  title="STOCK ANALYSIS",
  icon=":material/finance_mode:",
  default=True,
)

about_page1=st.Page(
  page="page2.py",
  title="STOCKS NEWS",
  icon=":material/breaking_news:"
)

pg= st.navigation(pages=[about_page, about_page1])

pg.run()







