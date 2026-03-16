import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("Abaarso Dashboard")
df = pd.read_csv("Master_infraction_data__.csv")
