# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv("data/pink_morsel_data.csv")
df['date'] = pd.to_datetime(df['date'])
df_2021 = df[(df['date'].dt.year == 2021) & (df['date'].dt.month == 1)]

region_colors = {
    'north' : 'red',
    'south' : 'green',
    'east' : 'blue',
    'west' : 'orange',
    'all' : 'purple'
}

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Pink Morsel Sales Dashboard
    '''),

    dcc.Graph(
        id='sales-graph'
    ),
    html.Div(
            dcc.RadioItems(
                 options=[{'label': html.Span("North", style={'color': region_colors['north']}), 'value': 'north'},
                        {'label': html.Span("South", style={'color': region_colors['south']}), 'value': 'south'},
                        {'label': html.Span("East", style={'color': region_colors['east']}), 'value': 'east'},
                        {'label': html.Span("West", style={'color': region_colors['west']}), 'value': 'west'},
                        {'label': html.Span("All Regions", style={'color': region_colors['all']}), 'value': 'all'}
                          ],
                value = 'all', id='radio_items', inline = True
            )
            ,style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        ),
    ])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('radio_items', 'value'),
)

def update_graph(selected_region):
    color = region_colors[selected_region]
    if selected_region == 'all':
        df_daily = df_2021.groupby("date")["sales"].sum().reset_index()
        fig = px.line(df_daily, x = "date", y = "sales", title="All Regions")
    else:
        df_region = df_2021[df_2021['region'] == selected_region]
        df_daily = df_region.groupby("date")["sales"].sum().reset_index()
        fig = px.line(df_daily, x="date", y="sales", title=f"{selected_region.capitalize()}")
    fig.update_traces(line = dict(color = color, width = 3))
    fig.update_xaxes(tickangle=45, dtick='D1')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
