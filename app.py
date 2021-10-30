import pandas as pd
import plotly.express as pl

data = pd.read_csv('data.csv')
fig = pl.scatter(data,x="date",y="cases",color="country")

fig.show()