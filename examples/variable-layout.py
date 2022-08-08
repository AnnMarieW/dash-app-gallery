

from dash import Dash, html, dcc, Input, Output, dash_table, callback
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd


data = px.data.stocks()
data['date'] = pd.to_datetime(data['date'])


app = Dash(__name__)


app.layout = dmc.Container([

    dmc.Container([
        html.H4('Equity prices - Line chart and Table data', style={'textAlign': 'center'}),

        dcc.Dropdown(
            ['Row oriented', 'Column oriented'],
            value='Row oriented',
            id='variable-layout-x-layout-dropdown'
        ),

        html.Br(),
        html.Br(),

        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in data.columns[1:]],
            # value='',
            id='variable-layout-x-stock-dropdown',
            multi=True
        ),

        html.Br(),
        html.Br(),


    ], fluid=True),



    dmc.SimpleGrid([

        dcc.Graph(id='variable-layout-x-line_chart'),

        dmc.Container(

            dash_table.DataTable(
                data.to_dict('records'),
                [{"name": i, "id": i} for i in data.columns],
                page_size=10
            ),
            style={'overflow-x': 'auto'},
            fluid=True,
        ),


    ],
        cols=1,
        id='variable-layout-x-simple_grid_layout',
        breakpoints=[
                {"maxWidth": 980, "cols": 2, "spacing": "sm"},
                {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                {"maxWidth": 600, "cols": 1, "spacing": "sm"},
    ]

    )
],
    # fluid=True
)


@callback(
    Output('variable-layout-x-line_chart', 'figure'),
    Input('variable-layout-x-stock-dropdown', 'value')
)
def select_stocks(stocks):

    # Stacking df i.e. transforming 'wide' into 'long' df
    data_stacked = data.set_index('date').stack().reset_index()

    if stocks is not None and stocks != []:
        data_stacked = data_stacked.query("level_1 in @stocks")

    fig = px.line(
        data_frame=data_stacked,
        x='date',
        y=0,
        color='level_1',
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title='Price',
        xaxis_title='Date'
    )

    return fig


@callback(
    Output('variable-layout-x-simple_grid_layout', 'cols'),
    Input('variable-layout-x-layout-dropdown', 'value')
)
def grid_layout(value):
    if value == 'Row oriented':
        return 2
    else:
        return 1


if __name__ == '__main__':
    app.run_server(debug=True)


