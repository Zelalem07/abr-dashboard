import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(layout="wide")

df = pd.read_csv("iris.csv")
unique_species = df["species"].unique()

st.title("Iris Dahsbord")
print(df.columns)

col_a, col_b = st.columns([1,1])

selected_species = col_a.selectbox(label="Species",
                                   options=unique_species,
                                   label_visibility="collapsed")
show_histogram = col_b.checkbox(label='show histogram',)

# Subset of data
df_plot = df[df["species"]==selected_species]
# st.write(df_plot)

sl_mean = round(df_plot["sepal_length"].mean(),2)
sw_mean = round(df_plot["sepal_width"].mean(),2)
pl_mean = round(df_plot["petal_length"].mean(),2)
pw_mean = round(df_plot["petal_width"].mean(),2)

# define 4 columns
col1, col2, col3, col4 = st.columns([1,1,1,1])
col1.metric(label="Sepal length avg", value=sl_mean)
col2.metric(label="Sepal width avg", value=sw_mean)
col3.metric(label="Petal length avg", value=pl_mean)
col4.metric(label="Sepal width avg", value=pw_mean)

# color map dictionary
color_map = {"setosa": "gray",
             "versicolor": "blue",
             "virginica": "green"}

# add a scatter plot
scatter_plot = px.scatter(data_frame=df,
                          color_discrete_map=color_map,
                          x="sepal_length",
                          y="petal_width",
                          color="species",
                          title=f"Sepal lengh vd petal width for {selected_species}")
st.plotly_chart(scatter_plot)

# Create histograms

hist1= px.histogram(data_frame=df_plot,
                    color_discrete_map=color_map,
                    x='sepal_length',
                    color="species",
                    title="Distribution of sepal_length")
hist2= px.histogram(data_frame=df_plot,
                    color_discrete_map=color_map,
                    x='petal_width',
                    color="species",
                    title="Distribution of petal_width")
hist3= px.histogram(data_frame=df_plot,
                    color_discrete_map=color_map,
                    x='sepal_width',
                    color="species",
                    title="Distribution of sepal_width")
hist4= px.histogram(data_frame=df_plot,
                    color_discrete_map=color_map,
                    x='petal_length',
                    color="species",
                    title="Distribution of petal_length")

col5, col6, col7, col8 = st.columns(4, gap="small")

if show_histogram:
    col5.plotly_chart(hist1)
    col6.plotly_chart(hist2)
    col7.plotly_chart(hist3)
    col8.plotly_chart(hist4)