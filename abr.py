import pandas as pd
import streamlit as st
import plotly.express as px
import datetime
from streamlit import title

url = ("https://docs.google.com/spreadsheets/d/"
       "1FnnGXPKVAi5pKRR5mvhFoUlSqN6pIsqTwU80xykvUJA/export?format=csv")
df_abr = pd.read_csv(url)
print(df_abr)
# st.write(df_abr)

unique_day = df_abr["Infraction_Date"].unique()

# add dropdown
selected_date = st.selectbox(label="Infraction_Date",
                             options=unique_day)

df_plot = df_abr[df_abr["Infraction_Date"]==selected_date]
st.write(df_plot)
st.write(f"Number of infracation on {selected_date} is: {len(df_plot)}")


title = f"Plot of Grade vs Total infraction of day {selected_date}"
scatter_plot_ = px.scatter(data_frame=df_abr,
                           x="Grade",
                           y="Total_Infractions",
                           title=title,
                           color="Grade")
st.plotly_chart(scatter_plot_)
# fig2 = px.treemap(df_abr, path=["Grade", "Section", "Gender", "Student Name",
#                                 "Total_Infractions", "Infraction_Date", "Infraction", "Staff Name"])
# tab1,tab2 = st.tabs(["std","std2"])
# with tab1:
#     st.subheader("test")
# with tab2:
#     fig2.show()

