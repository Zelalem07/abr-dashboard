import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Title
# -----------------------------
st.title("Student Behavior Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("Master_infraction_data__.csv")

# Convert date columns
df["Infraction_Date"] = pd.to_datetime(df["Infraction_Date"])
df["Date of Infraction"] = pd.to_datetime(df["Date of Infraction"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

# Grade filter
grade = st.sidebar.multiselect(
    "Select Grade",
    options=df["Grade"].unique(),
    default=df["Grade"].unique()
)

# Section filter
section = st.sidebar.multiselect(
    "Select Section",
    options=df["Section"].unique(),
    default=df["Section"].unique()
)

# Date filter type
date_filter_option = st.sidebar.radio(
    "Filter by Date:",
    options=["Single Date", "Date Range"]
)

if date_filter_option == "Single Date":
    selected_date = st.sidebar.date_input(
        "Select Infraction Date",
        value=df["Infraction_Date"].min(),
        min_value=df["Infraction_Date"].min(),
        max_value=df["Infraction_Date"].max()
    )
else:  # Date Range
    selected_date = st.sidebar.date_input(
        "Select Date Range",
        value=[df["Infraction_Date"].min(), df["Infraction_Date"].max()],
        min_value=df["Infraction_Date"].min(),
        max_value=df["Infraction_Date"].max()
    )

# -----------------------------
# Apply Filters
# -----------------------------
if date_filter_option == "Single Date":
    df_filtered = df[
        (df["Grade"].isin(grade)) &
        (df["Section"].isin(section)) &
        (df["Infraction_Date"] == pd.to_datetime(selected_date))
    ]
else:
    start_date, end_date = selected_date
    df_filtered = df[
        (df["Grade"].isin(grade)) &
        (df["Section"].isin(section)) &
        (df["Infraction_Date"] >= pd.to_datetime(start_date)) &
        (df["Infraction_Date"] <= pd.to_datetime(end_date))
    ]

# -----------------------------
# KPIs
# -----------------------------
total_infractions = df_filtered["Infraction"].count()
total_students = df_filtered["Student Name"].nunique()
total_staff = df_filtered["Staff Name"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Infractions", total_infractions)
col2.metric("Total Students", total_students)
col3.metric("Staff Reporting", total_staff)

# -----------------------------
# Bar Chart: Infractions by Grade
# -----------------------------

fig1 = px.scatter(\
    df_filtered,
    x="Grade",
    y="Total_Infractions",
    title="Infractions by Grade",
    color="Grade"
)
st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Treemap: Infractions Hierarchy
# -----------------------------
fig2 = px.treemap(
    df_filtered,
    path=["Grade","Section","Gender","Student Name","Total_Infractions","Infraction","Infraction_Date","Staff Name"],
    color="Grade"
)
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Filtered Data Table
# -----------------------------
st.subheader("Filtered Data")
st.dataframe(df_filtered.sort_values("Grade"))