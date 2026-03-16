import pandas as pd
import plotly.express as px

df = pd.read_csv("dataset/iris.csv")
df1 = pd.read_csv("master_infraction_data.csv")

print(df.columns)
print(df.head())

print("**************************************************")

print(df1.columns)
print(df1.head())

df_grd = df1.groupby(["Grade"]).count().reset_index()
print(df_grd)
plot1 = px.bar(data_frame=df_grd,x="Grade", y="Total_Infractions", title="Grade vs Total_Infractions")
plot1.show()
"*****************************************************************"
df_av = df.groupby(["species"]).mean().reset_index()
print(df_av)

plot = px.bar(data_frame=df_av,
              x="species", y="petal_width",
              title=" Bar chart showing average peral width across species")
plot.show()