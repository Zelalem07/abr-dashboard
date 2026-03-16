import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title('Auto MPG Dashboard')

df = pd.read_csv("clean_auto_mpg.csv", index_col=0)
# st.write(df)
# print(df.columns)
# print(df.info())

unique_origion = df["origin"].unique()
# to see unique_origion as a list
unique_origion = list(unique_origion)
unique_origion.sort()

unique_origion_str = ["Origin:" + str(origin) for origin in unique_origion]

# st.write(unique_origion)
# print(unique_origion)
# print(unique_origion_str)

# add tabs
tab1,tab2,tab3 = st.tabs([unique_origion_str[0],
                          unique_origion_str[1],
                          unique_origion_str[2]])
with tab1:
    st.subheader(f"I am a tab 1 {unique_origion_str[0]}")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")
    df_tab = df[df["origin"] == unique_origion[0]]
    avg_mpg = round(df_tab["mpg"].mean(), 1)
    avg_disp = round(df_tab["displacement"].mean(), 1)
    avg_hp = round(df_tab["horsepower"].mean(), 1)
    avg_wt = round(df_tab["weight"].mean(), 1)
    col1.metric(label="Avg MPG", value=avg_mpg)
    col2.metric(label="Avg Disp", value=avg_disp)
    col3.metric(label="Avg Hsp", value=avg_hp)
    col4.metric(label="Avg Weight", value=avg_wt)

    col5, col6 = st.columns([4, 1])
    sctter_plt = px.scatter(data_frame=df_tab,
                            x="weight",
                            y="horsepower",
                            size="displacement",
                            hover_name="car name",
                            color="cylinders",
                            title=f"Weight vs HP for cars from {unique_origion[0]}"
                            )
    histogram_plt = px.histogram(data_frame=df_tab,
                                 x="mpg",
                                 title="MPG Distribution")
    col5.plotly_chart(sctter_plt)
    col6.plotly_chart((histogram_plt))

with tab2:
    st.subheader(f"I am a tab 2 {unique_origion_str[1]}")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")
    df_tab = df[df["origin"] == unique_origion[1]]
    avg_mpg = round(df_tab["mpg"].mean(), 1)
    avg_disp = round(df_tab["displacement"].mean(), 1)
    avg_hp = round(df_tab["horsepower"].mean(), 1)
    avg_wt = round(df_tab["weight"].mean(), 1)
    col1.metric(label="Avg MPG", value=avg_mpg)
    col2.metric(label="Avg Disp", value=avg_disp)
    col3.metric(label="Avg Hsp", value=avg_hp)
    col4.metric(label="Avg Weight", value=avg_wt)

    col5, col6 = st.columns([4, 1])
    sctter_plt = px.scatter(data_frame=df_tab,
                            x="weight",
                            y="horsepower",
                            size="displacement",
                            hover_name="car name",
                            color="cylinders",
                            title=f"Weight vs HP for cars from {unique_origion[1]}"
                            )
    histogram_plt = px.histogram(data_frame=df_tab,
                                 x="mpg",
                                 title="MPG Distribution")
    col5.plotly_chart(sctter_plt)
    col6.plotly_chart((histogram_plt))
with tab3:
    st.subheader(f"I am a tab 3 {unique_origion_str[2]}")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")
    df_tab = df[df["origin"] == unique_origion[2]]
    avg_mpg = round(df_tab["mpg"].mean(), 1)
    avg_disp = round(df_tab["displacement"].mean(), 1)
    avg_hp = round(df_tab["horsepower"].mean(), 1)
    avg_wt = round(df_tab["weight"].mean(), 1)
    col1.metric(label="Avg MPG", value=avg_mpg)
    col2.metric(label="Avg Disp", value=avg_disp)
    col3.metric(label="Avg Hsp", value=avg_hp)
    col4.metric(label="Avg Weight", value=avg_wt)

    col5, col6 = st.columns([4, 1])
    sctter_plt = px.scatter(data_frame=df_tab,
                            x="weight",
                            y="horsepower",
                            size="displacement",
                            hover_name="car name",
                            color="cylinders",
                            title=f"Weight vs HP for cars from {unique_origion[2]}"
                            )
    histogram_plt = px.histogram(data_frame=df_tab,
                                 x="mpg",
                                 title="MPG Distribution")
    col5.plotly_chart(sctter_plt)
    col6.plotly_chart((histogram_plt))
