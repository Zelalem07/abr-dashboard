import  pandas as pd
import plotly.express as px
import streamlit as st
import datetime

st.set_page_config(layout="wide")

# Page title
st.markdown("# Gapmider Dashbord")

df = pd.read_csv("dataset/gapminder.csv/gapminder.csv")

# Computation
unique_years = df["year"].unique()
print(unique_years)
print(df.columns)
# add dropdown
selected_year = st.selectbox(label="Years",
                             options=unique_years)

df_plot = df[df["year"]==selected_year]
# st.write(df_plot)

average_gdp = round(df_plot["gdpPercap"].mean(),2)
average_lifeExp = round(df_plot["lifeExp"].mean(),2)
average_centroid_lat = round(df_plot["centroid_lat"].mean(),2)

# add 3 columns and metric widget
col1, col2, col3 = st.columns(3, gap="small",vertical_alignment="top")
col1.text('average_gdp')
col1.subheader(average_gdp)

col2.text("average_lifeExp")
col2.subheader(average_lifeExp)

col3.text("average_centroid_lat")
col3.subheader(average_centroid_lat)
st.write("..........................................................................................................."
         ".................")
# OR

col1, col2, col3 = st.columns([1,1,1])
col1.metric(label="average_gdp", value=average_gdp)
col2.metric(label="average_lifeExp", value=average_lifeExp)
col3.metric(label="average_centroid_lat", value=average_centroid_lat)

# add scatterplot
# title = "plot of GDP vs life expectancy for year {}".format(selected_year)
title_ = f"plot of GDP vs life expectancy for year {selected_year}"
scatter_plot = px.scatter(data_frame=df_plot,
                          x="gdpPercap",
                          y="lifeExp",
                          color="continent",title=title_
                          )
st.plotly_chart(scatter_plot)

#add boxplot
    # first we have tocreat a columns


col4,col5 = st.columns(2)
box_plot = px.box(data_frame=df_plot,
                      x="continent",
                      y="gdpPercap",
                      title=f"Distribution of GDP across the different continents for year {selected_year}")
histo_gdp = px.histogram(data_frame=df_plot,
                      x="continent",
                      title=f"Distribution of GDP across the different continents for year {selected_year}")

col4.plotly_chart(box_plot)
col5.plotly_chart(histo_gdp)

box_plot_2 = px.box(data_frame=df_plot,
                      x="continent",
                      y="lifeExp",
                      title=f"Distribution of lifeExp the different continents for year {selected_year}")
histo_lif = px.histogram(data_frame=df_plot,
                      x="lifeExp",
                      title=f"Distribution of lifeExp the different continents for year {selected_year}")
col4.plotly_chart(box_plot_2)
col5.plotly_chart(histo_lif)