import datetime

from email.policy import default

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Behavior Dashboard")

df = pd.read_csv("Master_infraction_data__.csv")

# st.dataframe(df)
print(df.columns)
#
# df["Infraction_Date"] = pd.to_datetime(df["Infraction_Date"])
# df["Date of Infraction"] = pd.to_datetime(df["Date of Infraction"])
#
# st.sidebar.header("Filters")
#
# grade = st.sidebar.multiselect(
#     "Select Grade",
#     options=df["Grade"].unique(),
#     default=df["Grade"].unique())
#
# section = st.sidebar.multiselect(
#     "Select Section",
#     options=df["Section"].unique(),
#     default=df["Section"].unique())
#
# infraction_date = st.sidebar.selectbox(label="select infraction_date",
#                                options=df["Infraction_Date"].unique())
#                                # placeholder=datetime.date.today())
#
# df_filtered = df[
#     (df["Grade"].isin(grade)) &
#     (df["Section"].isin(section))]
#
# st.write(df[df['Grade']=="grade"])
# total_infractions = df_filtered["Infraction"].count()
# total_students = df_filtered["Student Name"].nunique()
# total_staff = df_filtered["Staff Name"].nunique()
#
# col1, col2, col3 = st.columns(3)
#
# col1.metric("Total Infractions", total_infractions)
# col2.metric("Total Students", total_students)
# col3.metric("Staff Reporting", total_staff)
#
# fig1 = px.bar(
#     df_filtered,
#     x="Grade",
#     title="Infractions by Grade",
#     color="Grade")
#
# st.plotly_chart(fig1, use_container_width=True)
#
# fig2 = px.treemap(
#     df_filtered,
#     path=["Grade","Section","Gender","Student Name","Total_Infractions","Infraction","Infraction_Date","Staff Name"],
#     color="Grade")
#
# st.plotly_chart(fig2, use_container_width=True)
#
# st.subheader("Filtered Data")
#
# st.dataframe(df_filtered)

"""
df["Infraction_Date"] = pd.to_datetime(df["Infraction_Date"])

st.sidebar.header("Filters")

# Grade filter (already exists)
grade = st.sidebar.multiselect(
    "Select Grade",
    options=df["Grade"].unique(),
    default=df["Grade"].unique()
)

# Section filter (already exists)
section = st.sidebar.multiselect(
    "Select Section",
    options=df["Section"].unique(),
    default=df["Section"].unique()
)

# Infraction Date filter
infraction_date = st.sidebar.date_input(
    "Select Infraction Date",
    value=[df["Infraction_Date"].min(), df["Infraction_Date"].max()],
    min_value=df["Infraction_Date"].min(),
    max_value=df["Infraction_Date"].max()
)
# Make sure infraction_date is a list of two dates
start_date, end_date = infraction_date

df_filtered = df[
    (df["Grade"].isin(grade)) &
    (df["Section"].isin(section)) &
    (df["Infraction_Date"] >= pd.to_datetime(start_date)) &
    (df["Infraction_Date"] <= pd.to_datetime(end_date))
]

# KPIs
total_infractions = df_filtered["Infraction"].count()
total_students = df_filtered["Student Name"].nunique()
total_staff = df_filtered["Staff Name"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Infractions", total_infractions)
col2.metric("Total Students", total_students)
col3.metric("Staff Reporting", total_staff)

# Bar chart
fig1 = px.bar(
    df_filtered,
    x="Grade",
    title="Infractions by Grade",
    color="Grade"
)
st.plotly_chart(fig1, use_container_width=True)

# Treemap
fig2 = px.treemap(
    df_filtered,
    path=["Grade","Section","Gender","Student Name","Infraction"],
    color="Grade"
)
st.plotly_chart(fig2, use_container_width=True)

# Data table
st.subheader("Filtered Data")
st.dataframe(df_filtered)"""



