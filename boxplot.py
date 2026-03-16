import pandas as pd
import plotly.express as px

df_master = pd.read_csv("Master_infraction_data__.csv")
print(df_master.head())


df = pd.read_csv("iris.csv")
print(df.columns)
# print(df.head(3))

# plot = px.box(data_frame=df, x="species", y="petal_width", title='Title')
# plot.show()

plot = px.box(data_frame=df_master, x="Grade",
              y="Total_Infractions", color="Grade",
              title='Title')
plot.show()

plot = px.violin(data_frame=df_master, x="Grade",
              y="Total_Infractions", color="Grade",box=True,
              title='Title')
plot.show()
