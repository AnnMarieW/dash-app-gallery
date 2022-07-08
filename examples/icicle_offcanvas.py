
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


app.layout = dbc.Container([

    html.H4('Where does profit come from? - Looking at profit through segment and region dimension.'),

    dbc.NavbarSimple(
        children=[],
        brand="Dash is awesom!",
        brand_href="#",
        color="primary",
        dark=True,
        className='mb-2'
    ),


    html.Div(
        [
            dbc.Button("Open Filters", id="icicle_offCanvas_open-offcanvas", n_clicks=0),
            dbc.Offcanvas([

                dcc.Dropdown(
                    id='icicle_offCanvas_dynamic_callback_dropdown_region',
                    options=[{'label': x, 'value': x} for x in sorted(df['Region'].unique())]
                )],
                id="icicle_offCanvas_offcanvas",
                title="Filters",
                is_open=False,
            )
        ]
    ),

    dcc.Graph(
        id='icicle_offCanvas_line_chart',
        className='mt-2 mb-4'
    )

], fluid=True)


@callback(
    Output('icicle_offCanvas_line_chart', 'figure'),
    Input('icicle_offCanvas_dynamic_callback_dropdown_region', 'value')
)
def line_chart(
        region
):
    # This is necessary because of local-global variable scoping
    # i.e. if local variable (with name same as global variable name) is defined within
    # inner/local scope, then global variable can't be accessed.
    # Place where local variable with global name is defined is not important.
    # If local variable with global variable name is defined SOMEWHERE within local
    # scope, global variable can't be accessed.
    dff = df.copy()

    if region is not None:
        dff = dff.query('Region == @region')

    dff = dff.groupby(by=['Segment', 'Region']).sum().reset_index()

    fig = px.icicle(dff, path=[px.Constant("all"), 'Segment', 'Region'], values='profit_derived')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig


@callback(
    Output("icicle_offCanvas_offcanvas", "is_open"),
    Input("icicle_offCanvas_open-offcanvas", "n_clicks"),
    State("icicle_offCanvas_offcanvas", "is_open"),
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()

