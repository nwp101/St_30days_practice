import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

st.header("Profiling Report")

df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

report = ProfileReport(df, title="Penguins Profiling Report", minimal=True)
html = report.to_html()

components.html(html, height=800, scrolling=True)