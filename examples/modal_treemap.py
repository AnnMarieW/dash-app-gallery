
import pandas as pd
from dash import Dash, Input, Output, callback, dcc, html, State
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv')


df['profit_derived'] = df['Profit'].str.replace(',', '.').astype('float')

# Hierarchical charts work only with positive aggregate values
# In this step, we ensure that aggregated values will be positive
df = df.query(expr="profit_derived >= 0")

df = df[['profit_derived', 'Segment', 'Region']]


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([

    dbc.NavbarSimple(
        children=[],
        brand="Dash is awesom!",
        brand_href="#",
        color="primary",
        dark=True,
    ),

    html.Br(),
    html.Br(),

    html.Div(
        [
            dbc.Button("Open modal", id="open", n_clicks=0),
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Filters")),
                    dbc.ModalBody([
                        # Filter within dbc Modal
                        dcc.Dropdown(
                            id='dynamic_callback_dropdown_region',
                            options=[{'label': x, 'value': x} for x in sorted(df['Region'].unique())]
                        )
                    ]),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal",
                is_open=False,
            ),
        ]
    ),

    html.Br(),
    html.Br(),

    dcc.Graph(
        id='line_chart'
    ),

    html.Br(),
    html.Br()

])


@callback(
    Output(component_id='line_chart', component_property='figure'),
    Input(component_id='dynamic_callback_dropdown_region', component_property='value')
)
def line_chart(
        region
):
    dff = df.copy()

    if region is not None:
        dff = dff.query('Region == @region')

    dff = dff.groupby(by=['Segment', 'Region']).sum().reset_index()

    fig = px.treemap(dff, path=[px.Constant("all"), 'Segment', 'Region'], values='profit_derived')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig


@callback(
    Output("modal", "is_open"),
    Input("open", "n_clicks"),
    Input("close", "n_clicks"),
    State("modal", "is_open"),
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()
