import pandas as pd
import plotly.express as px

df_master = pd.read_csv("Master_infraction_data__.csv")
print(df_master.columns)


df = pd.read_csv("iris.csv")
print(df.columns)

plot = px.histogram(data_frame=df_master, x="Grade",
              y="Total_Infractions", color="Grade",
              title='Title')
plot.show()