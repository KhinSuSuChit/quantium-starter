# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("data/pink_morsel_data.csv")
df['date'] = pd.to_datetime(df['date'])
df_2021 = df[(df['date'].dt.year == 2021) & (df['date'].dt.month == 1)]
df_daily = df_2021.groupby("date")["sales"].sum().reset_index()

fig = px.line(df_daily, x="date", y="sales", title="Pink Morsel Sales")
fig.update_xaxes(
    tickangle=45,
    dtick='D1'
)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Pink Morsel Sales Dashboard
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
