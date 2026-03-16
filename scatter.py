import pandas as pd
import plotly.express as px

df = pd.read_csv("dataset/iris.csv")
df1 = pd.read_csv("abr/MASTER.csv")
print(df.columns)
print(df1.columns)


plot = px.scatter(data_frame=df, x="sepal_length" ,y="petal_length",
                  color="species",
                  facet_col="species",
                  title="sepal vs petal lenth")
plot.show()

# plot1 = px.scatter(data_frame=df1, x="sepal_length" ,y="petal_length",
#                   color="species",
#                   facet_col="species",
#                   title="sepal vs petal lenth")
# plot1.show()