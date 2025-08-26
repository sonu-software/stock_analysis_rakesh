import streamlit as st

#Page Setup#
about_page=st.Page(
  page="stock_analysis.py",
  title="MAIN PAGE",
  default=True,
)

about_page1=st.Page(
  page="page2.py",
  title="PAGE 2-",
)

pg= st.navigation(pages=[about_page, about_page1])

pg.run()


